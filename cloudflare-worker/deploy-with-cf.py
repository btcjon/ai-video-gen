#!/usr/bin/env python3
"""Deploy CogVideoX-3 Worker using CloudflareManager"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.append('/home/dev/.claude/scripts')
from cloudflare_manager import CloudflareManager

def deploy_worker():
    # Initialize Cloudflare manager
    cf = CloudflareManager()

    # Read worker code
    worker_path = Path(__file__).parent / "worker.js"
    with open(worker_path) as f:
        worker_code = f.read()

    # Upload worker
    print("🚀 Deploying CogVideoX-3 Worker to Cloudflare...")
    result = cf.upload_worker("cogvideox3-generator", worker_code)

    if result.get("success"):
        print("\n✅ Worker deployed successfully!")
        print("\nYour CogVideoX-3 UI is available at:")
        print("https://cogvideox3-generator.<your-subdomain>.workers.dev")
        print("\nOr check your Cloudflare dashboard for the exact URL.")
    else:
        print("\n❌ Deployment failed:")
        print(result)

if __name__ == "__main__":
    deploy_worker()
