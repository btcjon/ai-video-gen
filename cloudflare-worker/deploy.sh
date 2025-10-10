#!/bin/bash

# CogVideoX-3 Worker Deployment Script
# Requires Cloudflare API Token

set -e

echo "🚀 Deploying CogVideoX-3 Worker to Cloudflare..."

# Check if API token is set
if [ -z "$CLOUDFLARE_API_TOKEN" ]; then
  echo ""
  echo "⚠️  CLOUDFLARE_API_TOKEN not set"
  echo ""
  echo "Get your API token from:"
  echo "https://dash.cloudflare.com/profile/api-tokens"
  echo ""
  echo "Then run:"
  echo "export CLOUDFLARE_API_TOKEN='your-token-here'"
  echo "./deploy.sh"
  exit 1
fi

# Deploy worker
cd "$(dirname "$0")"
wrangler deploy --env=""

echo ""
echo "✅ Deployment complete!"
echo ""
echo "Your worker will be available at:"
echo "https://cogvideox3-generator.<your-subdomain>.workers.dev"
