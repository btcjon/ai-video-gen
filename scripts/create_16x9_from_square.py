#!/usr/bin/env python3
"""
Convert Square Nano-Banana Output to True 16:9 Format
Post-processing solution for aspect ratio control
"""

import os
from PIL import Image, ImageDraw
from datetime import datetime

def create_16x9_from_square(input_path, output_path=None, background_color=(255, 255, 255)):
    """
    Convert square image to 16:9 format by adding background or cropping intelligently
    """
    if not os.path.exists(input_path):
        print(f"❌ Input image not found: {input_path}")
        return None

    # Open the square image
    with Image.open(input_path) as img:
        width, height = img.size
        print(f"📐 Input dimensions: {width}x{height}")

        # Calculate 16:9 dimensions
        if width >= height:
            # Use width as base, calculate height for 16:9
            new_width = width
            new_height = int(width * 9 / 16)
        else:
            # Use height as base, calculate width for 16:9
            new_height = height
            new_width = int(height * 16 / 9)

        print(f"📐 Target 16:9 dimensions: {new_width}x{new_height}")

        # Create new 16:9 canvas
        new_img = Image.new('RGB', (new_width, new_height), background_color)

        # Center the original image on the new canvas
        paste_x = (new_width - width) // 2
        paste_y = (new_height - height) // 2

        # If original has transparency, handle it properly
        if img.mode in ('RGBA', 'LA'):
            new_img.paste(img, (paste_x, paste_y), img)
        else:
            new_img.paste(img, (paste_x, paste_y))

        # Generate output filename if not provided
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            output_path = f"/home/dev/Projects/ai-video-gen/docs/images/{base_name}_16x9_{timestamp}.png"

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save the 16:9 image
        new_img.save(output_path, 'PNG')

        # Calculate final ratio
        final_ratio = new_width / new_height
        target_ratio = 16 / 9

        file_size = os.path.getsize(output_path) / (1024 * 1024)
        print(f"✅ 16:9 image created: {output_path}")
        print(f"📐 Final dimensions: {new_width}x{new_height}")
        print(f"📊 Aspect ratio: {final_ratio:.3f} (Target: {target_ratio:.3f})")
        print(f"💾 File size: {file_size:.1f}MB")

        return {
            "output_path": output_path,
            "dimensions": f"{new_width}x{new_height}",
            "aspect_ratio": final_ratio,
            "file_size": f"{file_size:.1f}MB"
        }

def main():
    """Convert the best H2O Pure image to 16:9 format"""
    print("🎬 Converting H2O Pure to True 16:9 Format")
    print("=" * 50)

    # Use the best generated image (first one had good quality)
    input_image = "/home/dev/Projects/ai-video-gen/docs/images/h2o_pure_scale_demo_16x9.png"

    # Convert to true 16:9
    result = create_16x9_from_square(
        input_path=input_image,
        output_path="/home/dev/Projects/ai-video-gen/docs/images/h2o_pure_TRUE_16x9_FINAL.png",
        background_color=(248, 248, 248)  # Light gray background
    )

    if result:
        print("\n🎉 16:9 CONVERSION COMPLETE!")
        print("This image is now ready for video compatibility")
        return result["output_path"]
    else:
        print("❌ Conversion failed")
        return None

if __name__ == "__main__":
    main()