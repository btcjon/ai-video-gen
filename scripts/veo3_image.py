#!/usr/bin/env python3
"""
H2O Pure Scene 3 - Fixed Image-to-Video Generation
Using reliable free image hosting
"""

import json
import requests
import base64
import os
from datetime import datetime

# Kie.ai API Configuration
KIE_API_KEY = "20108f4bba626227a1bb5e281d1e5a64"
KIE_BASE_URL = "https://api.kie.ai/api/v1/veo"

HEADERS = {
    'Authorization': f'Bearer {KIE_API_KEY}',
    'Content-Type': 'application/json'
}

def upload_to_tmpfiles(image_path):
    """Upload to tmpfiles.org - Simple, reliable, no API key needed"""

    print("📤 Uploading image to tmpfiles.org...")

    try:
        with open(image_path, 'rb') as file:
            files = {'file': ('h2o_pure.png', file, 'image/png')}
            response = requests.post(
                'https://tmpfiles.org/api/v1/upload',
                files=files,
                timeout=30
            )

        if response.status_code == 200:
            result = response.json()
            if result['status'] == 'success':
                # Convert download URL to direct link
                url = result['data']['url']
                # Replace tmpfiles.org with dl.tmpfiles.org for direct access
                direct_url = url.replace('tmpfiles.org/', 'tmpfiles.org/dl/')
                print(f"✅ Image uploaded: {direct_url}")
                return direct_url

    except Exception as e:
        print(f"❌ Upload error: {str(e)}")

    return None

def upload_to_0x0(image_path):
    """Alternative: Upload to 0x0.st - Simple curl-like service"""

    print("📤 Uploading image to 0x0.st...")

    try:
        with open(image_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(
                'https://0x0.st',
                files=files,
                timeout=30
            )

        if response.status_code == 200:
            image_url = response.text.strip()
            print(f"✅ Image uploaded: {image_url}")
            return image_url

    except Exception as e:
        print(f"❌ Upload error: {str(e)}")

    return None

def generate_with_exact_product(image_url):
    """Generate Scene 3 using actual H2O Pure product image"""

    print("\n" + "=" * 60)
    print("IMAGE-TO-VIDEO WITH YOUR EXACT PRODUCT")
    print("=" * 60)

    # Shorter, clearer prompt for 8-second video
    prompt = """Male hands demonstrate this exact H2O Pure bottle. Deep male voice:
    "8 drops per gallon. Destroys bacteria. 99% natural. One hour."
    Show counting 8 drops into murky water. Water clears. Professional lighting."""

    request_body = {
        "prompt": prompt,
        "imageUrls": [image_url],
        "model": "veo3_fast",
        "aspectRatio": "16:9",
        "enableFallback": True,
        "watermark": "H2O Pure"
    }

    print(f"🖼️ Product image: {image_url}")
    print("🎯 Your exact bottle will appear")
    print("🎤 Voice: Deep male narrator")
    print("-" * 60)

    try:
        print("\n📤 Sending request to Kie.ai...")
        response = requests.post(
            f"{KIE_BASE_URL}/generate",
            headers=HEADERS,
            json=request_body,
            timeout=30
        )

        result = response.json()

        if response.status_code == 200 and result.get("code") == 200:
            task_id = result["data"]["taskId"]
            print(f"✅ SUCCESS! Generation started")
            print(f"📋 Task ID: {task_id}")

            # Save for tracking
            with open("scene3_final_task.json", "w") as f:
                json.dump({
                    "task_id": task_id,
                    "type": "image-to-video",
                    "image_url": image_url,
                    "timestamp": datetime.now().isoformat(),
                    "voice_note": "Deep male narrator - use same description for all scenes"
                }, f, indent=2)

            return task_id
        else:
            print(f"❌ API Error: {result}")
            return None

    except Exception as e:
        print(f"❌ Request failed: {str(e)}")
        return None

def generate_all_scenes_batch():
    """Generate all 4 scenes with consistent voice description"""

    print("\n" + "=" * 60)
    print("BATCH GENERATION - ALL 4 SCENES")
    print("=" * 60)

    scenes = [
        {
            "name": "Scene 1 - Grid Down",
            "prompt": """Power grid failure at dusk. Suburban street lights shutting off.
            Deep male narrator voice: "When the grid fails, water stops flowing."
            Man 45 years old watches through window. Emergency preparedness setting.""",
            "cost": "$0.38"
        },
        {
            "name": "Scene 2 - Traditional Fails",
            "prompt": """Man struggling with heavy 50-pound water filter in garage.
            Deep male narrator: "Thousand dollar filters need power we don't have."
            Show contrast with tiny H2O Pure bottle in hand.""",
            "cost": "$0.38"
        },
        {
            "name": "Scene 4 - Family Safe",
            "prompt": """Family with clean water, H2O Pure bottles visible.
            Deep male narrator: "One bottle, 15 gallons. Family protected."
            Parents and teen son drinking purified water. Calm confidence.""",
            "cost": "$0.38"
        }
    ]

    print("Using consistent 'deep male narrator voice' across all scenes")
    print("Total cost: $1.14 for remaining 3 scenes")
    print("-" * 60)

    return scenes

def main():
    """Main workflow"""

    print("=" * 60)
    print("H2O PURE SCENE 3 - FINAL VERSION")
    print("=" * 60)

    # Your product image
    image_path = "/home/dev/Projects/ai-video-gen/images/6mL H2O Pure_square.png"

    # Check file exists
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        return

    # Try multiple upload services
    image_url = upload_to_tmpfiles(image_path)

    if not image_url:
        image_url = upload_to_0x0(image_path)

    if image_url:
        # Generate with exact product
        task_id = generate_with_exact_product(image_url)

        if task_id:
            print("\n" + "=" * 60)
            print("✅ SCENE 3 FINAL VERSION GENERATING")
            print("=" * 60)
            print(f"Task ID: {task_id}")
            print("Time: 10-15 minutes")
            print("\n📝 VOICE CONSISTENCY NOTES:")
            print("- Using 'deep male narrator voice' description")
            print("- Apply same to all 4 scenes for consistency")
            print("- Alternative: Post-production voiceover")
            print("=" * 60)

            # Show other scenes ready to generate
            scenes = generate_all_scenes_batch()
            print("\n🎬 Ready to generate remaining scenes?")
            print("Run: python3 generate_all_scenes.py")

    else:
        print("\n❌ Auto-upload failed")
        print("\n📝 MANUAL OPTION:")
        print("1. Go to: https://imgur.com/upload")
        print("2. Upload: 6mL H2O Pure_square.png")
        print("3. Get direct image URL")
        print("4. Use in imageUrls parameter")

if __name__ == "__main__":
    main()