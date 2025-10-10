# CogVideoX-3 Worker Deployment Guide

## Issue

Cloudflare Workers API requires **API Token** authentication (OAuth), not the legacy API Key.

The `cloudflare_manager.py` script uses API Key auth which works for DNS/zones but NOT for Workers.

## Solution 1: Deploy via Wrangler CLI (Recommended)

### Step 1: Get API Token

1. Go to: https://dash.cloudflare.com/profile/api-tokens
2. Click "Create Token"
3. Use template: "Edit Cloudflare Workers"
4. Copy the token

### Step 2: Deploy

```bash
export CLOUDFLARE_API_TOKEN='your-token-here'
cd /home/dev/Projects/ai-video-gen/cloudflare-worker
wrangler deploy --env=""
```

## Solution 2: Deploy via Dashboard (Easy)

1. Go to: https://dash.cloudflare.com → Workers & Pages
2. Click "Create" → "Create Worker"
3. Name it: `cogvideox3-generator`
4. Replace the default code with content from `worker.js`
5. Click "Save and Deploy"

## Solution 3: Manual API Call

If you have the API token:

```bash
# Set your API token
export CF_API_TOKEN="your-token-here"
export CF_ACCOUNT_ID="8a7fea5d8c50d36939e6aea9279c3cbf"

# Deploy worker
curl -X PUT "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/workers/scripts/cogvideox3-generator" \
  -H "Authorization: Bearer $CF_API_TOKEN" \
  -H "Content-Type: application/javascript" \
  --data-binary "@worker.js"
```

## After Deployment

Your CogVideoX-3 UI will be available at:
- `https://cogvideox3-generator.<your-subdomain>.workers.dev`

Check your Cloudflare dashboard for the exact URL.

## Local Testing (No Auth Required)

```bash
wrangler dev --env=""
```

Access at: http://localhost:8787

---

## Why This Happened

- **API Key (X-Auth-Key + X-Auth-Email)**: Legacy auth, works for zones/DNS/firewall
- **API Token (Bearer token)**: Modern auth, REQUIRED for Workers/Pages

The `cloudflare_manager.py` uses API Key which can't access Workers endpoints.
