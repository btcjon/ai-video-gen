#!/usr/bin/env python3
"""
OpenAI GPT-Image-1 Complete Implementation
Battle-tested patterns for H2O Pure product photography workflow
"""

import os
import sys
import argparse
import requests
import base64
import json
import tempfile
from datetime import datetime
from pathlib import Path

class OpenAIImageGenerator:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            print('❌ Error: OPENAI_API_KEY environment variable not set')
            print('   Get your key from: https://platform.openai.com/api-keys')
            sys.exit(1)

        self.model = "gpt-image-1"
        self.api_url = "https://api.openai.com/v1/images/generations"
        self.edit_url = "https://api.openai.com/v1/images/edits"

        # Correct size mappings (learned through trial & error)
        self.size_map = {
            '1:1': '1024x1024',
            '16:9': '1536x1024',  # NOT 1792x1024!
            'portrait': '1024x1536',
            'landscape': '1536x1024'
        }

        self.headers = {'Authorization': f'Bearer {self.api_key}'}

    def generate_image(self, prompt, quality='low', size='1024x1024', n=1,
                      output_file=None):
        """Generate image with basic supported parameters for gpt-image-1"""

        print(f'🎨 Generating image with GPT-Image-1...')
        print(f'   Model: {self.model}')
        print(f'   Prompt: {prompt}')
        print(f'   Quality: {quality} | Size: {size} | Count: {n}')
        print()

        # Minimal payload for gpt-image-1 (testing what actually works)
        data = {
            "model": self.model,
            "prompt": prompt,
            "n": n,
            "size": size,
            "quality": quality
        }

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=data,
                timeout=120
            )

            return self._process_generation_response(response, output_file, format)

        except requests.RequestException as e:
            print(f'❌ Network error: {e}')
            return False
        except Exception as e:
            print(f'❌ Unexpected error: {e}')
            return False

    def edit_image(self, image_path, prompt, quality='low', size='1024x1024',
                   output_file=None):
        """Note: gpt-image-1 may not support direct image editing.
        This will attempt but may need alternative approach."""

        if not self._validate_file_size(image_path):
            return False

        print(f'✏️  Attempting image editing with GPT-Image-1...')
        print(f'   Input: {image_path}')
        print(f'   Prompt: {prompt}')
        print(f'   Quality: {quality}')
        print(f'   Note: gpt-image-1 may not support traditional image editing')
        print()

        try:
            with open(image_path, 'rb') as f:
                files = {'image': f}
                data = {
                    'model': self.model,
                    'prompt': prompt,
                    'quality': quality,
                    'size': size
                }

                response = requests.post(
                    self.edit_url,
                    headers=self.headers,
                    files=files,
                    data=data,
                    timeout=120
                )

                return self._process_generation_response(response, output_file)

        except Exception as e:
            print(f'❌ Edit error: {e}')
            print(f'   Note: gpt-image-1 might not support image editing endpoint')
            return False

    def _validate_file_size(self, image_path):
        """Validate file exists and is within size limits"""
        if not os.path.exists(image_path):
            print(f"❌ Image file not found: {image_path}")
            return False

        size_mb = os.path.getsize(image_path) / (1024 * 1024)
        if size_mb > 50:
            print(f"⚠️  Warning: Image size ({size_mb:.1f} MB) exceeds 50 MB limit")
            return False

        print(f"✅ File size OK: {size_mb:.1f} MB")
        return True

    def _process_generation_response(self, response, output_file=None, format='jpeg'):
        """Process generation response with comprehensive error handling"""

        print(f'Response Status: {response.status_code}')

        if response.status_code != 200:
            try:
                error_data = response.json()
                error_msg = error_data.get('error', {}).get('message', 'Unknown error')

                # Common error guidance
                if 'rate_limit' in error_msg.lower():
                    print('❌ Rate limit exceeded. Wait a moment and try again.')
                elif 'insufficient_quota' in error_msg.lower():
                    print('❌ Insufficient OpenAI credits. Check your account balance.')
                elif 'invalid value' in error_msg.lower():
                    print(f'❌ Invalid parameter: {error_msg}')
                    print('   Common fixes: Use "high" not "hd", check size format')
                else:
                    print(f'❌ API Error: {error_msg}')
            except:
                print(f'❌ HTTP Error: {response.status_code}')
                print(f'Response: {response.text[:500]}')
            return False

        try:
            result = response.json()
            images = result.get('data', [])

            if not images:
                print('❌ No images generated')
                return False

            # Create docs/images directory if it doesn't exist
            os.makedirs('/home/dev/Projects/ai-video-gen/docs/images', exist_ok=True)

            count = 0
            success = True
            generated_files = []

            for image_data in images:
                if 'b64_json' in image_data:
                    if output_file and count == 0:
                        filename = output_file
                    else:
                        filename = f"/home/dev/Projects/ai-video-gen/docs/images/openai_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{count}.{format}"

                    if self._save_base64_image(image_data['b64_json'], filename):
                        generated_files.append(filename)
                        count += 1
                    else:
                        success = False

                elif 'url' in image_data:
                    if output_file and count == 0:
                        filename = output_file
                    else:
                        filename = f"/home/dev/Projects/ai-video-gen/docs/images/openai_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{count}.{format}"

                    if self._save_url_image(image_data['url'], filename):
                        generated_files.append(filename)
                        count += 1
                    else:
                        success = False

            # Show revised prompt if available
            revised_prompt = result.get('revised_prompt')
            if revised_prompt:
                print(f'📝 Revised Prompt: {revised_prompt}')

            return generated_files if success else False

        except json.JSONDecodeError:
            print('❌ Invalid JSON response from OpenAI')
            return False

    def _save_base64_image(self, b64_data, filename):
        """Save base64 encoded image data"""
        try:
            image_bytes = base64.b64decode(b64_data)

            with open(filename, 'wb') as f:
                f.write(image_bytes)

            file_size = len(image_bytes) / (1024 * 1024)
            print(f'✅ Image saved: {filename} ({file_size:.2f} MB)')

            # Get image dimensions if possible
            try:
                from PIL import Image
                with Image.open(filename) as img:
                    width, height = img.size
                    print(f'📐 Dimensions: {width}x{height}')
            except ImportError:
                pass

            print(f'   Full path: {os.path.abspath(filename)}')
            return True

        except Exception as e:
            print(f'❌ Failed to save base64 image: {e}')
            return False

    def _save_url_image(self, image_url, filename):
        """Download and save image from URL"""
        print(f'Downloading image from URL...')

        try:
            img_response = requests.get(image_url, timeout=30)
            if img_response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(img_response.content)

                file_size = len(img_response.content) / (1024 * 1024)
                print(f'✅ Image saved: {filename} ({file_size:.2f} MB)')
                print(f'   Full path: {os.path.abspath(filename)}')
                return True
            else:
                print(f'❌ Failed to download image: HTTP {img_response.status_code}')
                return False
        except Exception as e:
            print(f'❌ Failed to download image: {e}')
            return False


def test_h2o_pure_workflow():
    """Test H2O Pure product photography workflow - focusing on what gpt-image-1 can do"""

    generator = OpenAIImageGenerator()

    print("=" * 80)
    print("OPENAI GPT-IMAGE-1 H2O PURE PRODUCT PHOTOGRAPHY TEST")
    print("=" * 80)
    print()

    # Test 1: Text-to-image generation - square format
    print("🧪 TEST 1: Text-to-image product generation (square 1:1)")
    print("-" * 50)

    result1 = generator.generate_image(
        prompt="Professional product photography of H2O Pure water treatment drops bottle. 6mL bottle with white dropper cap, blue and white label design with 'H2O PURE' text, water droplet graphics. Clean white background, studio lighting, commercial photography style. Sharp focus, high detail.",
        quality="low",
        size="1024x1024",
        output_file="/home/dev/Projects/ai-video-gen/docs/images/h2o_pure_square_openai.png"
    )

    if result1:
        print("✅ Square product generation successful")
    else:
        print("❌ Square product generation failed")

    print()

    # Test 2: Text-to-image generation - 16:9 format
    print("🧪 TEST 2: Text-to-image product generation (16:9 landscape)")
    print("-" * 50)

    result2 = generator.generate_image(
        prompt="Professional product photography of H2O Pure water treatment drops bottle in 16:9 landscape format. 6mL bottle with white dropper cap, blue and white label with 'H2O PURE' branding, positioned center-left with copy space on right. Clean white background, studio lighting, commercial style.",
        quality="medium",
        size="1536x1024",
        output_file="/home/dev/Projects/ai-video-gen/docs/images/h2o_pure_16x9_openai.png"
    )

    if result2:
        print("✅ 16:9 product generation successful")
    else:
        print("❌ 16:9 product generation failed")

    print()

    # Test 3: Enhanced product photography
    print("🧪 TEST 3: Enhanced professional product photography")
    print("-" * 50)

    result3 = generator.generate_image(
        prompt="Premium e-commerce product photography of H2O Pure water treatment drops. 6mL bottle with white dropper cap, professional studio lighting with soft shadows and gradient background. Blue and white label design, water treatment branding. High-end commercial photography, subtle reflections, perfect product presentation.",
        quality="medium",
        size="1024x1024",
        output_file="/home/dev/Projects/ai-video-gen/docs/images/h2o_pure_enhanced_openai.png"
    )

    if result3:
        print("✅ Enhanced photography successful")
    else:
        print("❌ Enhanced photography failed")

    print()

    # Test 4: Marketing lifestyle image
    print("🧪 TEST 4: Marketing lifestyle hero image")
    print("-" * 50)

    result4 = generator.generate_image(
        prompt="Marketing lifestyle image featuring H2O Pure water treatment drops in modern kitchen setting. Clean white countertop, natural lighting, bottle positioned prominently with kitchen background blur. Premium lifestyle photography, clean aesthetic, commercial appeal.",
        quality="medium",
        size="1536x1024",
        output_file="/home/dev/Projects/ai-video-gen/docs/images/h2o_pure_lifestyle_openai.png"
    )

    if result4:
        print("✅ Lifestyle marketing image successful")
    else:
        print("❌ Lifestyle marketing image failed")

    print()

    # Test 5: Attempt image editing (may not work with gpt-image-1)
    print("🧪 TEST 5: Image editing attempt (experimental)")
    print("-" * 50)

    source_image = "/home/dev/Projects/ai-video-gen/docs/images/6mL H2O Pure_square.png"
    result5 = generator.edit_image(
        image_path=source_image,
        prompt="Transform this product image to 16:9 aspect ratio while maintaining product clarity",
        quality="medium",
        size="1536x1024",
        output_file="/home/dev/Projects/ai-video-gen/docs/images/h2o_pure_edited_openai.png"
    )

    if result5:
        print("✅ Image editing successful")
    else:
        print("❌ Image editing failed (expected - gpt-image-1 may not support editing)")

    print()
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)

    tests = [
        ("Square Product (1:1)", result1),
        ("Landscape Product (16:9)", result2),
        ("Enhanced Photography", result3),
        ("Lifestyle Marketing", result4),
        ("Image Editing", result5)
    ]

    for test_name, result in tests:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:<25} | {status}")

    print()
    print("Generated files in /home/dev/Projects/ai-video-gen/docs/images/:")
    print("- h2o_pure_square_openai.png (1:1 product)")
    print("- h2o_pure_16x9_openai.png (16:9 product)")
    print("- h2o_pure_enhanced_openai.png (enhanced photography)")
    print("- h2o_pure_lifestyle_openai.png (lifestyle marketing)")
    print("- h2o_pure_edited_openai.png (image editing attempt)")

    print()
    print("COMPARISON NOTES:")
    print("- OpenAI gpt-image-1 focuses on text-to-image generation")
    print("- May not support traditional image editing endpoints")
    print("- Compare results with nano-banana outputs for quality assessment")
    print("- Check file sizes, detail quality, and brand consistency")

    return tests


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='OpenAI GPT-Image-1 H2O Pure Testing')
    parser.add_argument('--test', action='store_true', help='Run H2O Pure workflow tests')
    parser.add_argument('--prompt', type=str, help='Custom prompt for generation')
    parser.add_argument('--edit', type=str, help='Image path for editing')
    parser.add_argument('--quality', type=str, default='low', choices=['low', 'medium', 'high'], help='Generation quality')
    parser.add_argument('--size', type=str, default='1024x1024', help='Image size')
    parser.add_argument('--format', type=str, default='png', choices=['png', 'jpeg', 'webp'], help='Output format')

    args = parser.parse_args()

    if args.test:
        test_h2o_pure_workflow()
    elif args.prompt:
        generator = OpenAIImageGenerator()
        if args.edit:
            # Image editing mode
            generator.edit_image(
                image_path=args.edit,
                prompt=args.prompt,
                quality=args.quality,
                size=args.size
            )
        else:
            # Text-to-image mode
            generator.generate_image(
                prompt=args.prompt,
                quality=args.quality,
                size=args.size,
                format=args.format
            )
    else:
        print("Use --test to run H2O Pure workflow tests")
        print("Use --prompt with optional --edit for custom generation")