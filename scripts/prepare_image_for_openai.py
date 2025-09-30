#!/usr/bin/env python3
"""
Prepare image for OpenAI editing - ensure PNG format and <4MB
"""

import os
from PIL import Image

def prepare_image_for_openai(input_path, output_path=None):
    """Convert image to PNG format suitable for OpenAI editing"""

    if not os.path.exists(input_path):
        print(f"❌ Input image not found: {input_path}")
        return False

    try:
        with Image.open(input_path) as img:
            print(f"📸 Original image: {img.format}, {img.size}, {img.mode}")

            # Convert to RGB if needed (for PNG compatibility)
            if img.mode not in ('RGB', 'RGBA'):
                print(f"🔄 Converting from {img.mode} to RGB")
                img = img.convert('RGB')

            # Generate output path if not provided
            if not output_path:
                base_name = os.path.splitext(os.path.basename(input_path))[0]
                output_path = f"docs/images/{base_name}_openai_ready.png"

            # Save as PNG
            img.save(output_path, 'PNG', optimize=True)

            # Check file size
            size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"✅ Converted image saved: {output_path}")
            print(f"📊 Size: {size_mb:.2f} MB")

            if size_mb > 4:
                print(f"⚠️  Warning: File size ({size_mb:.2f} MB) exceeds 4MB limit")
                print("   Consider resizing the image")
                return False

            return output_path

    except Exception as e:
        print(f"❌ Error preparing image: {e}")
        return False

if __name__ == "__main__":
    input_file = "docs/images/6mL H2O Pure_square.png"
    result = prepare_image_for_openai(input_file)
    if result:
        print(f"🎯 Ready for OpenAI: {result}")
    else:
        print("❌ Failed to prepare image")