#!/usr/bin/env python3
"""
H2O Pure Prepper Campaign Generation Script
VEO 3 API Optimizer - Self-Contained Generation
"""

import requests
import json
import time
from datetime import datetime

# Kie.ai API Configuration
KIE_API_KEY = "20108f4bba626227a1bb5e281d1e5a64"
KIE_BASE_URL = "https://api.kie.ai/api/v1/veo"
KIE_HEADERS = {
    'Authorization': f'Bearer {KIE_API_KEY}',
    'Content-Type': 'application/json'
}

# Load prompts
with open('/home/dev/Projects/ai-video-gen/production-plans/h2o-pure-prepper/prompts/final-prompts.json', 'r') as f:
    prompts_data = json.load(f)

# Campaign tracking
tracking_data = {
    "campaign": "H2O Pure Prepper",
    "generation_started": datetime.now().isoformat(),
    "model": "veo3_fast",
    "total_cost_estimate": "$2.66",
    "quality_score": "9.5/10",
    "user_approval": "CONFIRMED",
    "aspect_ratio": "16:9",
    "scenes": {},
    "task_ids": {},
    "status": "GENERATING"
}

def generate_video(scene_data, scene_num):
    """Generate a single video scene using VEO 3 API"""
    print(f"\n=== Generating Scene {scene_num}: {scene_data['name']} ===")

    request_data = {
        "prompt": scene_data["prompt"],
        "model": "veo3_fast",
        "aspectRatio": "16:9",
        "enableFallback": True,
        "enableTranslation": True
    }

    try:
        print("Sending request to Kie.ai VEO 3 API...")
        response = requests.post(
            f"{KIE_BASE_URL}/generate",
            headers=KIE_HEADERS,
            json=request_data,
            timeout=30
        )

        print(f"Response Status: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")

        if response.status_code == 200:
            result = response.json()
            print(f"Success! Response: {json.dumps(result, indent=2)}")

            if 'data' in result and 'taskId' in result['data']:
                task_id = result['data']['taskId']
                tracking_data['task_ids'][f'scene_{scene_num}'] = task_id
                tracking_data['scenes'][f'scene_{scene_num}'] = {
                    'name': scene_data['name'],
                    'task_id': task_id,
                    'generation_method': scene_data['generation_method'],
                    'status': 'submitted',
                    'timestamp': datetime.now().isoformat()
                }
                print(f"Task ID: {task_id}")
                return task_id
            else:
                print(f"Unexpected response format: {result}")
                return None
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def main():
    """Generate all scenes for H2O Pure Prepper campaign"""
    print("🎬 H2O Pure Prepper Campaign Generation")
    print("=" * 50)
    print(f"Quality Score: {tracking_data['quality_score']} ✓")
    print(f"Model: {tracking_data['model']} ($0.38 per scene)")
    print(f"Aspect Ratio: {tracking_data['aspect_ratio']}")
    print(f"Total Scenes: {len(prompts_data['scenes'])}")
    print(f"Estimated Cost: {tracking_data['total_cost_estimate']}")

    # Generate all scenes
    for i, scene in enumerate(prompts_data['scenes'], 1):
        task_id = generate_video(scene, i)
        if task_id:
            print(f"✅ Scene {i} submitted successfully - Task ID: {task_id}")
        else:
            print(f"❌ Scene {i} failed to submit")

        # Brief pause between requests
        time.sleep(2)

    # Save tracking data
    tracking_file = '/home/dev/Projects/ai-video-gen/production-plans/h2o-pure-prepper/tasks/generation-tracking.json'
    with open(tracking_file, 'w') as f:
        json.dump(tracking_data, f, indent=2)

    print("\n" + "=" * 50)
    print("🎯 GENERATION SUMMARY")
    print("=" * 50)
    print(f"Campaign: {tracking_data['campaign']}")
    print(f"Scenes Submitted: {len(tracking_data['task_ids'])}")
    print(f"Expected Duration: 56 seconds (7 × 8s)")
    print(f"Completion Time: 10-15 minutes")
    print(f"Dashboard: https://kie.ai/dashboard")
    print(f"Tracking File: {tracking_file}")

    if tracking_data['task_ids']:
        print("\n📋 TASK IDS:")
        for scene, task_id in tracking_data['task_ids'].items():
            print(f"  {scene}: {task_id}")

    print("\n⏰ Next Steps:")
    print("1. Monitor generation at https://kie.ai/dashboard")
    print("2. Videos will be ready in 10-15 minutes")
    print("3. Download videos when complete")
    print("4. Add product images to scenes 3-7 if needed")
    print("5. Add post-production voiceover")

if __name__ == "__main__":
    main()