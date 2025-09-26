#!/usr/bin/env python3
"""
Unified VEO 3 Video Generator - Simplified workflow for all video generation needs
Consolidates all scene generation scripts into one flexible tool
"""

import json
import requests
import argparse
import os
import base64
from datetime import datetime
from pathlib import Path

# Kie.ai API Configuration
KIE_API_KEY = "20108f4bba626227a1bb5e281d1e5a64"
KIE_BASE_URL = "https://api.kie.ai/api/v1/veo"

HEADERS = {
    'Authorization': f'Bearer {KIE_API_KEY}',
    'Content-Type': 'application/json'
}

def upload_image_to_kie(image_path):
    """Upload image to Kie.ai using their native File Upload API

    Kie.ai File Upload Strategy:
    - Small files (≤1MB): Base64
    - Medium files (1-10MB): File Stream
    - Large files (>10MB): File Stream
    - Remote URLs: URL Upload
    - Files auto-deleted after 3 days
    """

    print(f"📤 Uploading image to Kie.ai: {image_path}")

    # Check if it's already a URL
    if image_path.startswith('http'):
        # Use URL upload method for remote files
        try:
            response = requests.post(
                'https://api.kie.ai/api/file-url-upload',
                headers=HEADERS,
                json={
                    'fileUrl': image_path,
                    'uploadPath': 'veo3-images',
                    'fileName': os.path.basename(image_path)
                },
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 200:
                    file_url = result['data']['fileUrl']
                    print(f"✅ URL uploaded to Kie.ai: {file_url}")
                    return file_url

            print(f"❌ URL upload failed: {response.json()}")
            return None

        except Exception as e:
            print(f"❌ URL upload error: {str(e)}")
            return None

    # For local files, check size to determine method
    file_size = os.path.getsize(image_path)
    file_size_mb = file_size / (1024 * 1024)

    print(f"📊 File size: {file_size_mb:.2f}MB")

    try:
        if file_size_mb <= 1:
            # Use Base64 for small files (≤1MB)
            import base64

            with open(image_path, 'rb') as file:
                file_data = file.read()
                base64_data = base64.b64encode(file_data).decode('utf-8')

            response = requests.post(
                'https://api.kie.ai/api/file-base64-upload',
                headers=HEADERS,
                json={
                    'fileBase64': f"data:image/png;base64,{base64_data}",
                    'uploadPath': 'veo3-images',
                    'fileName': os.path.basename(image_path)
                },
                timeout=30
            )

            print(f"📤 Using Base64 upload (file ≤1MB)")

        else:
            # Use File Stream for larger files (>1MB)
            with open(image_path, 'rb') as file:
                files = {'file': (os.path.basename(image_path), file, 'image/png')}

                # File stream upload requires multipart form data
                stream_headers = {'Authorization': f'Bearer {KIE_API_KEY}'}

                response = requests.post(
                    'https://api.kie.ai/api/file-stream-upload',
                    headers=stream_headers,
                    files=files,
                    data={
                        'uploadPath': 'veo3-images',
                        'fileName': os.path.basename(image_path)
                    },
                    timeout=60  # Longer timeout for larger files
                )

            print(f"📤 Using File Stream upload (file >{1 if file_size_mb > 1 else 10}MB)")

        if response.status_code == 200:
            result = response.json()
            if result.get('code') == 200:
                file_url = result['data']['fileUrl']
                expires_at = result['data'].get('expiresAt', 'unknown')
                print(f"✅ Image uploaded to Kie.ai: {file_url}")
                print(f"⏰ Expires: {expires_at} (auto-deleted after 3 days)")
                return file_url

        print(f"❌ Upload failed: {response.json()}")
        return None

    except Exception as e:
        print(f"❌ Upload error: {str(e)}")
        # Fallback to tmpfiles.org if Kie.ai upload fails
        print(f"🔄 Falling back to tmpfiles.org...")
        return upload_image_tmpfiles(image_path)

def upload_image_tmpfiles(image_path):
    """Fallback upload to tmpfiles.org if Kie.ai upload fails"""

    try:
        with open(image_path, 'rb') as file:
            files = {'file': (os.path.basename(image_path), file, 'image/png')}
            response = requests.post(
                'https://tmpfiles.org/api/v1/upload',
                files=files,
                timeout=30
            )

        if response.status_code == 200:
            result = response.json()
            if result['status'] == 'success':
                url = result['data']['url']
                direct_url = url.replace('tmpfiles.org/', 'tmpfiles.org/dl/')
                print(f"✅ Fallback upload successful: {direct_url}")
                return direct_url

    except Exception as e:
        print(f"❌ Fallback upload error: {str(e)}")

    return None

def generate_video(prompt, image_path=None, model="veo3_fast", aspect_ratio="16:9",
                   watermark=None, campaign=None, scene_name=None, continue_from_task=None,
                   quality_score=None):
    """Generate a single video with VEO 3

    Args:
        continue_from_task: Task ID to extract last frame from for scene continuation
        quality_score: Quality review score (8-10 required for generation)
    """

    # Quality gate check
    if quality_score is not None:
        if quality_score < 8.0:
            print(f"❌ QUALITY GATE FAILED: Score {quality_score}/10 (minimum 8.0 required)")
            print(f"⚠️ Prompt must be revised before generation")
            return None
        else:
            print(f"✅ Quality Score: {quality_score}/10 - Approved for generation")

    request_body = {
        "prompt": prompt,
        "model": model,
        "aspectRatio": aspect_ratio,
        "enableFallback": True,
        "enableTranslation": True
    }

    # Add watermark if provided
    if watermark:
        request_body["watermark"] = watermark

    # Handle image-to-video if image provided
    if image_path:
        if image_path.startswith("http"):
            # For URLs, we can either use directly or re-upload to Kie.ai
            # Re-uploading to Kie.ai ensures consistent handling
            print(f"🔗 Re-uploading URL to Kie.ai for consistency...")
            image_url = upload_image_to_kie(image_path)
            if not image_url:
                # If Kie.ai upload fails, use original URL
                print(f"⚠️ Using original URL: {image_path}")
                image_url = image_path
        else:
            # Upload local file to Kie.ai
            image_url = upload_image_to_kie(image_path)
            if not image_url:
                print("❌ Failed to upload image")
                return None

        request_body["imageUrls"] = [image_url]
        print(f"🖼️ Using image-to-video mode with: {image_url[:50]}...")

    # Handle frame continuation from previous scene
    elif continue_from_task:
        print(f"🔗 Scene continuation from task: {continue_from_task[:8]}...")
        # Note: This would require implementing video download and frame extraction
        # For now, this is a placeholder showing the intended workflow
        print("⚠️ Frame extraction not yet implemented - using text-to-video")
        print("💡 TIP: Manually extract last frame and use --image flag for now")

    print(f"🎬 Generating with model: {model} (${1.50 if model == 'veo3' else 0.38})")

    try:
        response = requests.post(
            f"{KIE_BASE_URL}/generate",
            headers=HEADERS,
            json=request_body,
            timeout=30
        )

        result = response.json()

        if response.status_code == 200 and result.get("code") == 200:
            task_id = result["data"]["taskId"]
            print(f"✅ Generation started - Task ID: {task_id}")

            # Save task info
            save_task_info(task_id, prompt, campaign, scene_name, model, image_path, quality_score)

            return task_id
        else:
            print(f"❌ API Error: {result}")
            return None

    except Exception as e:
        print(f"❌ Request failed: {str(e)}")
        return None

def save_task_info(task_id, prompt, campaign, scene_name, model, image_path, quality_score=None):
    """Save task information for tracking with quality metrics"""

    # Determine save path
    if campaign:
        save_dir = Path(f"production-plans/{campaign}/tasks")
    else:
        save_dir = Path("data")

    save_dir.mkdir(parents=True, exist_ok=True)

    task_info = {
        "task_id": task_id,
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "model": model,
        "cost": 1.50 if model == "veo3" else 0.38,
        "scene_name": scene_name or "untitled",
        "campaign": campaign,
        "image_used": bool(image_path),
        "quality_score": quality_score,
        "quality_status": "approved" if quality_score and quality_score >= 8.0 else "pending_review"
    }

    filename = f"{scene_name or 'video'}_{task_id[:8]}.json" if scene_name else f"task_{task_id}.json"
    save_path = save_dir / filename

    with open(save_path, "w") as f:
        json.dump(task_info, f, indent=2)

    print(f"📝 Task saved: {save_path}")

def load_campaign_prompts(campaign, format_type="json"):
    """Load prompts from campaign folder"""

    # Try commercial JSON format first (recommended)
    prompts_file = Path(f"production-plans/{campaign}/prompts/{campaign}-commercial-json.json")

    if not prompts_file.exists():
        prompts_file = Path(f"production-plans/{campaign}/prompts/final-prompts.json")

    if not prompts_file.exists():
        # Try legacy location
        prompts_file = Path(f"production-plans/{campaign}/prompts/h2o-pure-no-narration-prompts.json")

    if prompts_file.exists():
        with open(prompts_file) as f:
            return json.load(f)

    return None

def batch_generate(campaign, model="veo3_fast"):
    """Generate all scenes for a campaign"""

    prompts = load_campaign_prompts(campaign)

    if not prompts:
        print(f"❌ No prompts found for campaign: {campaign}")
        return

    print(f"\n{'='*60}")
    print(f"BATCH GENERATION: {campaign.upper()}")
    print(f"{'='*60}")
    print(f"Scenes: {len(prompts['scenes'])}")
    print(f"Model: {model}")
    print(f"Total cost: ${(1.50 if model == 'veo3' else 0.38) * len(prompts['scenes']):.2f}")
    print(f"{'='*60}\n")

    task_ids = []

    for scene in prompts['scenes']:
        print(f"\n🎬 {scene['name']}")
        print("-" * 40)

        # Check if scene needs image-to-video
        image_path = scene.get('image_path')

        # Check for scene continuation
        continue_from = scene.get('continue_from')
        continue_task = None

        # If this scene continues from another, find the previous task ID
        if continue_from and task_ids:
            for i, prev_scene in enumerate(prompts['scenes'][:len(task_ids)]):
                if prev_scene.get('name') == continue_from:
                    continue_task = task_ids[i]
                    print(f"🔗 Continuing from: {continue_from}")
                    break

        # Handle JSON format prompts (commercial quality)
        if 'json_prompt' in scene:
            prompt = json.dumps(scene['json_prompt'], separators=(',', ':'))
        else:
            prompt = scene.get('prompt_text') or scene.get('prompt')

        task_id = generate_video(
            prompt=prompt,
            image_path=image_path,
            model=model,
            aspect_ratio=scene.get('aspect_ratio', '16:9'),
            watermark=prompts.get('watermark'),
            campaign=campaign,
            scene_name=scene['name'],
            continue_from_task=continue_task,
            quality_score=scene.get('quality_score')
        )

        if task_id:
            task_ids.append(task_id)

    print(f"\n{'='*60}")
    print(f"✅ BATCH COMPLETE")
    print(f"{'='*60}")
    print(f"Generated: {len(task_ids)}/{len(prompts['scenes'])} scenes")
    print(f"Time: 10-15 minutes per video")
    print(f"Check status: https://kie.ai/dashboard")
    print(f"{'='*60}")

    return task_ids

def check_status(task_id=None, campaign=None):
    """Check status of video generation tasks"""

    if task_id:
        # Check specific task
        print(f"Checking task: {task_id}")
        # Note: Status endpoint may not be available, use dashboard
        print(f"Check at: https://kie.ai/dashboard")
    elif campaign:
        # Check all tasks for campaign
        task_dir = Path(f"production-plans/{campaign}/tasks")
        if task_dir.exists():
            tasks = list(task_dir.glob("*.json"))
            print(f"\n{campaign.upper()} Campaign Tasks:")
            for task_file in tasks:
                with open(task_file) as f:
                    data = json.load(f)
                    print(f"  • {data['scene_name']}: {data['task_id'][:8]}... ({data['timestamp']})")
        else:
            print(f"No tasks found for campaign: {campaign}")
    else:
        # Show recent tasks
        data_dir = Path("data")
        if data_dir.exists():
            tasks = sorted(data_dir.glob("task_*.json"), key=lambda x: x.stat().st_mtime, reverse=True)[:5]
            print("\nRecent Tasks:")
            for task_file in tasks:
                with open(task_file) as f:
                    data = json.load(f)
                    print(f"  • {data['task_id'][:8]}... ({data['timestamp']})")

def main():
    parser = argparse.ArgumentParser(description='VEO 3 Video Generator - Unified Interface')

    # Main commands
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Generate command
    gen_parser = subparsers.add_parser('generate', help='Generate a video')
    gen_parser.add_argument('--prompt', '-p', required=True, help='Video prompt')
    gen_parser.add_argument('--image', '-i', help='Image path for image-to-video')
    gen_parser.add_argument('--model', '-m', choices=['veo3', 'veo3_fast'], default='veo3_fast')
    gen_parser.add_argument('--aspect', '-a', choices=['16:9', '9:16', '1:1', 'Auto'], default='16:9')
    gen_parser.add_argument('--watermark', '-w', help='Watermark text')
    gen_parser.add_argument('--campaign', '-c', help='Campaign name for organization')
    gen_parser.add_argument('--scene', '-s', help='Scene name for tracking')
    gen_parser.add_argument('--continue-from', help='Task ID to continue from (frame continuation)')
    gen_parser.add_argument('--quality-score', '-q', type=float, help='Quality review score (8.0 minimum required)')

    # Batch command
    batch_parser = subparsers.add_parser('batch', help='Generate all scenes for a campaign')
    batch_parser.add_argument('campaign', help='Campaign name')
    batch_parser.add_argument('--model', '-m', choices=['veo3', 'veo3_fast'], default='veo3_fast')

    # Status command
    status_parser = subparsers.add_parser('status', help='Check generation status')
    status_parser.add_argument('--task', '-t', help='Specific task ID')
    status_parser.add_argument('--campaign', '-c', help='Campaign name')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == 'generate':
        task_id = generate_video(
            prompt=args.prompt,
            image_path=args.image,
            model=args.model,
            aspect_ratio=args.aspect,
            watermark=args.watermark,
            campaign=args.campaign,
            scene_name=args.scene,
            continue_from_task=getattr(args, 'continue_from', None),
            quality_score=getattr(args, 'quality_score', None)
        )

        if task_id:
            print(f"\n✅ Success! Check status in 10-15 minutes")
            print(f"Dashboard: https://kie.ai/dashboard")

    elif args.command == 'batch':
        batch_generate(args.campaign, args.model)

    elif args.command == 'status':
        check_status(args.task, args.campaign)

if __name__ == "__main__":
    main()