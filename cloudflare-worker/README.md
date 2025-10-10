# CogVideoX-3 Generator - Cloudflare Worker

Simple UI for generating videos with CogVideoX-3 via Z.AI API.

## Features

- **Text-to-Video** generation
- **Image-to-Video** with start frame
- **Start + End Frame** control for precise video generation
- **Drag & Drop** file upload for images
- **URL input** for remote images
- Up to **4K resolution** (3840x2160)
- **30/60 fps** support
- Optional **audio generation**
- Multiple **aspect ratios** (16:9, 9:16, 1:1)
- Local video download and saving

## Live URL

🎬 **https://cogvideox3-generator.thesystem.workers.dev**

## Deployment

### Prerequisites

```bash
npm install -g wrangler
```

### Deploy to Cloudflare

```bash
# Login to Cloudflare
wrangler login

# Deploy worker
cd /home/dev/Projects/ai-video-gen/cloudflare-worker
wrangler deploy --env=""
```

### Alternative: Using API Token

If you can't use OAuth login:

1. Get API token from: https://dash.cloudflare.com/profile/api-tokens
2. Set environment variable:

```bash
export CLOUDFLARE_API_TOKEN="your-token-here"
wrangler deploy --env=""
```

## Local Development

Run locally with Wrangler:

```bash
wrangler dev --env=""
```

Access at: http://localhost:8787

## Configuration

The worker is configured with:
- **Z.AI API Key**: `63e0189e8180410ca2ee151d2c020e31.Cd0DIl75hBTd9UpM`
- **Model**: CogVideoX-3
- **Cost**: $0.20 per video

## Saving Videos Locally

Use the included Node.js script:

```bash
node /home/dev/Projects/ai-video-gen/save-video.js <video_url> [filename]
```

Videos are saved to: `/home/dev/Projects/ai-video-gen/docs/output/`

## API Endpoints

### GET /
Returns the HTML UI

### POST /generate
Generate a video

**Request:**
```json
{
  "prompt": "A serene sunrise over mountains...",
  "image_url": "https://example.com/image.jpg", // optional
  "size": "1920x1080",
  "fps": 30,
  "quality": "quality",
  "with_audio": true
}
```

**Response:**
```json
{
  "success": true,
  "video_url": "https://...",
  "id": "...",
  "metadata": { ... }
}
```

### POST /download
Download video through proxy

**Request:**
```json
{
  "video_url": "https://...",
  "filename": "video.mp4"
}
```

## Usage

1. Open the deployed Worker URL in your browser
2. Enter a detailed video prompt
3. Optional: Add image URL for image-to-video
4. Configure settings (resolution, FPS, quality, audio)
5. Click "Generate Video"
6. Download the generated video

## Resolution Options

- **1080p**: 1920x1080 (landscape)
- **720p**: 1280x720 (landscape)
- **4K**: 3840x2160 (landscape)
- **720p Vertical**: 720x1280 (portrait)
- **1080p Vertical**: 1080x1920 (portrait)

## Quality Modes

- **Quality**: Slower generation, higher quality
- **Speed**: Faster generation, good quality

## Tips

- Be specific and descriptive in prompts
- Use 4K for final outputs, 720p for testing
- Audio adds realism but increases generation time
- Test with "speed" mode first, then use "quality" for finals
