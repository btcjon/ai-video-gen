/**
 * Cloudflare Worker for CogVideoX-3 Video Generation
 * Proxies requests to Z.AI API and saves outputs locally
 */

const ZAI_API_KEY = '63e0189e8180410ca2ee151d2c020e31.Cd0DIl75hBTd9UpM';
const ZAI_API_URL = 'https://api.z.ai/api/paas/v4/videos/generations';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // Serve favicon
    if (request.method === "GET" && url.pathname === "/favicon.ico") {
      return new Response("🎬", {
        headers: { "Content-Type": "text/plain", ...corsHeaders }
      });
    }

    // Serve UI
    if (request.method === 'GET' && url.pathname === '/') {
      return new Response(HTML_UI, {
        headers: { 'Content-Type': 'text/html', ...corsHeaders }
      });
    }

    // Generate video
    if (request.method === 'POST' && url.pathname === '/generate') {
      try {
        const body = await request.json();

        // Build Z.AI request
        const zaiRequest = {
          model: 'cogvideox-3',
          prompt: body.prompt,
          quality: body.quality || 'quality',
          with_audio: body.with_audio !== false,
          size: body.size || '1920x1080',
          fps: body.fps || 30
        };

        // Support single image, start frame, or start+end frames
        if (body.start_image && body.end_image) {
          // Start and end frame generation
          zaiRequest.image_url = [body.start_image, body.end_image];
        } else if (body.start_image) {
          // Single start frame
          zaiRequest.image_url = body.start_image;
        } else if (body.image_url) {
          // Legacy support
          zaiRequest.image_url = body.image_url;
        }

        // Log request for debugging
        console.log('Z.AI Request:', JSON.stringify(zaiRequest, null, 2));

        // Call Z.AI API
        const response = await fetch(ZAI_API_URL, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${ZAI_API_KEY}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(zaiRequest)
        });

        const contentType = response.headers.get('content-type');
        let result;

        if (contentType && contentType.includes('application/json')) {
          result = await response.json();
        } else {
          // Got HTML or other non-JSON response (likely error page)
          const text = await response.text();
          throw new Error(`API error (${response.status}): ${text.substring(0, 200)}`);
        }

        if (!response.ok) {
          throw new Error(result.error?.message || result.message || 'API request failed');
        }

        // Log the full response for debugging
        console.log('Z.AI Response:', JSON.stringify(result, null, 2));

        // Z.AI returns the result in a 'data' field
        const videoData = result.data || result;

        // Return video URL and metadata
        return new Response(JSON.stringify({
          success: true,
          video_url: videoData.video_url || videoData.url,
          id: videoData.id || videoData.task_id,
          status: videoData.status,
          data: videoData,
          metadata: {
            prompt: body.prompt,
            size: zaiRequest.size,
            fps: zaiRequest.fps,
            quality: zaiRequest.quality,
            with_audio: zaiRequest.with_audio,
            timestamp: new Date().toISOString()
          }
        }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });

      } catch (error) {
        return new Response(JSON.stringify({
          success: false,
          error: error.message
        }), {
          status: 500,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }
    }

    // Upload image endpoint (convert to base64 data URL)
    if (request.method === 'POST' && url.pathname === '/upload') {
      try {
        const formData = await request.formData();
        const file = formData.get('file');

        if (!file) {
          throw new Error('No file provided');
        }

        const arrayBuffer = await file.arrayBuffer();
        const base64 = btoa(String.fromCharCode(...new Uint8Array(arrayBuffer)));
        const mimeType = file.type || 'image/jpeg';
        const dataUrl = `data:${mimeType};base64,${base64}`;

        return new Response(JSON.stringify({
          success: true,
          data_url: dataUrl,
          filename: file.name,
          size: file.size
        }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      } catch (error) {
        return new Response(JSON.stringify({
          success: false,
          error: error.message
        }), {
          status: 500,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }
    }

    // Download video endpoint (proxy to save locally)
    if (request.method === 'POST' && url.pathname === '/download') {
      try {
        const { video_url, filename } = await request.json();

        const videoResponse = await fetch(video_url);
        const videoData = await videoResponse.arrayBuffer();

        return new Response(videoData, {
          headers: {
            'Content-Type': 'video/mp4',
            'Content-Disposition': `attachment; filename="${filename || 'video.mp4'}"`,
            ...corsHeaders
          }
        });
      } catch (error) {
        return new Response(JSON.stringify({
          success: false,
          error: error.message
        }), {
          status: 500,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }
    }

    return new Response('Not Found', { status: 404, headers: corsHeaders });
  }
};

const HTML_UI = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CogVideoX-3 Generator</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      padding: 20px;
      color: #333;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
      background: white;
      border-radius: 16px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.3);
      overflow: hidden;
    }
    .header {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 30px;
      text-align: center;
    }
    .header h1 {
      font-size: 32px;
      margin-bottom: 10px;
    }
    .header p {
      opacity: 0.9;
      font-size: 14px;
    }
    .content {
      padding: 30px;
    }
    .form-group {
      margin-bottom: 20px;
    }
    label {
      display: block;
      font-weight: 600;
      margin-bottom: 8px;
      color: #444;
      font-size: 14px;
    }
    textarea, input, select {
      width: 100%;
      padding: 12px;
      border: 2px solid #e0e0e0;
      border-radius: 8px;
      font-size: 14px;
      transition: border-color 0.3s;
      font-family: inherit;
    }
    textarea {
      resize: vertical;
      min-height: 100px;
    }
    input:focus, textarea:focus, select:focus {
      outline: none;
      border-color: #667eea;
    }
    .settings-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 15px;
    }
    .checkbox-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .checkbox-group input[type="checkbox"] {
      width: auto;
    }
    button {
      width: 100%;
      padding: 16px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    button:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }
    .status {
      margin-top: 20px;
      padding: 15px;
      border-radius: 8px;
      display: none;
    }
    .status.show {
      display: block;
    }
    .status.loading {
      background: #e3f2fd;
      color: #1976d2;
      border-left: 4px solid #1976d2;
    }
    .status.success {
      background: #e8f5e9;
      color: #2e7d32;
      border-left: 4px solid #2e7d32;
    }
    .status.error {
      background: #ffebee;
      color: #c62828;
      border-left: 4px solid #c62828;
    }
    .video-preview {
      margin-top: 20px;
      display: none;
    }
    .video-preview.show {
      display: block;
    }
    .video-preview video {
      width: 100%;
      border-radius: 8px;
      margin-bottom: 15px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .download-btn {
      background: linear-gradient(135deg, #2e7d32 0%, #388e3c 100%);
      margin-top: 10px;
    }
    .spinner {
      display: inline-block;
      width: 16px;
      height: 16px;
      border: 3px solid rgba(255,255,255,0.3);
      border-radius: 50%;
      border-top-color: white;
      animation: spin 1s linear infinite;
      margin-right: 8px;
    }
    @keyframes spin {
      to { transform: rotate(360deg); }
    }
    .hint {
      font-size: 12px;
      color: #666;
      margin-top: 4px;
    }
    .upload-zone {
      border: 2px dashed #ccc;
      border-radius: 8px;
      padding: 30px;
      text-align: center;
      cursor: pointer;
      transition: all 0.3s;
      position: relative;
      min-height: 150px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .upload-zone:hover {
      border-color: #667eea;
      background: #f8f9ff;
    }
    .upload-zone.drag-over {
      border-color: #667eea;
      background: #e3f2fd;
      transform: scale(1.02);
    }
    .upload-content {
      pointer-events: none;
    }
    .upload-icon {
      font-size: 48px;
      display: block;
      margin-bottom: 10px;
    }
    .upload-zone p {
      margin: 0;
      color: #666;
      font-weight: 500;
    }
    .upload-zone small {
      color: #999;
      font-size: 12px;
    }
    .preview-img {
      max-width: 100%;
      max-height: 200px;
      border-radius: 8px;
      object-fit: contain;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>🎬 CogVideoX-3 Generator</h1>
      <p>AI Video Generation • Up to 4K • 30/60 fps • With Audio</p>
    </div>

    <div class="content">
      <form id="videoForm">
        <div class="form-group">
          <label for="prompt">Video Prompt *</label>
          <textarea
            id="prompt"
            name="prompt"
            required
            placeholder="Describe the video you want to generate... e.g., 'A serene sunrise over misty mountains, camera slowly panning right revealing a crystal clear lake'"
          ></textarea>
          <div class="hint">Be specific and descriptive for best results</div>
        </div>

        <div class="form-group">
          <label>Start Frame (Optional)</label>
          <div class="upload-zone" id="startUpload" data-target="start">
            <input type="file" id="startFile" accept="image/*" hidden>
            <div class="upload-content">
              <span class="upload-icon">📸</span>
              <p>Drop image or click to upload</p>
              <small>Supports: JPG, PNG, WebP</small>
            </div>
            <img class="preview-img" id="startPreview" style="display:none">
          </div>
          <input type="url" id="start_url" placeholder="Or paste image URL" style="margin-top: 10px">
        </div>

        <div class="form-group">
          <label>End Frame (Optional)</label>
          <div class="upload-zone" id="endUpload" data-target="end">
            <input type="file" id="endFile" accept="image/*" hidden>
            <div class="upload-content">
              <span class="upload-icon">📸</span>
              <p>Drop image or click to upload</p>
              <small>For precise start→end control</small>
            </div>
            <img class="preview-img" id="endPreview" style="display:none">
          </div>
          <input type="url" id="end_url" placeholder="Or paste image URL" style="margin-top: 10px">
        </div>

        <div class="settings-grid">
          <div class="form-group">
            <label for="size">Resolution</label>
            <select id="size" name="size">
              <option value="1920x1080">1080p (1920x1080)</option>
              <option value="1280x720">720p (1280x720)</option>
              <option value="3840x2160">4K (3840x2160)</option>
              <option value="720x1280">720p Vertical (720x1280)</option>
              <option value="1080x1920">1080p Vertical (1080x1920)</option>
            </select>
          </div>

          <div class="form-group">
            <label for="fps">Frame Rate</label>
            <select id="fps" name="fps">
              <option value="30">30 fps</option>
              <option value="60">60 fps</option>
            </select>
          </div>

          <div class="form-group">
            <label for="quality">Quality</label>
            <select id="quality" name="quality">
              <option value="quality">Quality (Slower)</option>
              <option value="speed">Speed (Faster)</option>
            </select>
          </div>

          <div class="form-group">
            <label>Audio</label>
            <div class="checkbox-group">
              <input type="checkbox" id="with_audio" name="with_audio" checked>
              <label for="with_audio" style="margin: 0;">Include Audio</label>
            </div>
          </div>
        </div>

        <button type="submit" id="generateBtn">
          Generate Video ($0.20)
        </button>
      </form>

      <div id="status" class="status"></div>

      <div id="videoPreview" class="video-preview">
        <video id="generatedVideo" controls></video>
        <button type="button" id="downloadBtn" class="download-btn">
          Download Video
        </button>
      </div>
    </div>
  </div>

  <script>
    const form = document.getElementById('videoForm');
    const generateBtn = document.getElementById('generateBtn');
    const status = document.getElementById('status');
    const videoPreview = document.getElementById('videoPreview');
    const generatedVideo = document.getElementById('generatedVideo');
    const downloadBtn = document.getElementById('downloadBtn');

    let currentVideoUrl = null;
    let currentMetadata = null;
    let startImageData = null;
    let endImageData = null;

    // File upload handlers
    function setupUploadZone(zoneId, fileInputId, previewId, targetType) {
      const zone = document.getElementById(zoneId);
      const fileInput = document.getElementById(fileInputId);
      const preview = document.getElementById(previewId);

      zone.addEventListener('click', () => fileInput.click());

      zone.addEventListener('dragover', (e) => {
        e.preventDefault();
        zone.classList.add('drag-over');
      });

      zone.addEventListener('dragleave', () => {
        zone.classList.remove('drag-over');
      });

      zone.addEventListener('drop', async (e) => {
        e.preventDefault();
        zone.classList.remove('drag-over');
        const file = e.dataTransfer.files[0];
        if (file && file.type.startsWith('image/')) {
          await handleFileUpload(file, preview, targetType);
        }
      });

      fileInput.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (file) {
          await handleFileUpload(file, preview, targetType);
        }
      });
    }

    async function handleFileUpload(file, previewEl, targetType) {
      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await fetch('/upload', {
          method: 'POST',
          body: formData
        });

        const result = await response.json();

        if (result.success) {
          // Show preview
          previewEl.src = result.data_url;
          previewEl.style.display = 'block';
          previewEl.previousElementSibling.style.display = 'none';

          // Store data URL
          if (targetType === 'start') {
            startImageData = result.data_url;
          } else {
            endImageData = result.data_url;
          }
        }
      } catch (error) {
        showStatus('error', \`Upload failed: \${error.message}\`);
      }
    }

    // Setup upload zones
    setupUploadZone('startUpload', 'startFile', 'startPreview', 'start');
    setupUploadZone('endUpload', 'endFile', 'endPreview', 'end');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const formData = new FormData(form);

      // Get start and end images from uploads or URLs
      const startUrl = document.getElementById('start_url').value;
      const endUrl = document.getElementById('end_url').value;

      const data = {
        prompt: formData.get('prompt'),
        start_image: startImageData || startUrl || undefined,
        end_image: endImageData || endUrl || undefined,
        size: formData.get('size'),
        fps: parseInt(formData.get('fps')),
        quality: formData.get('quality'),
        with_audio: formData.get('with_audio') === 'on'
      };

      // Show loading
      generateBtn.disabled = true;
      generateBtn.innerHTML = '<span class="spinner"></span>Generating Video...';
      showStatus('loading', 'Sending request to CogVideoX-3... This may take 1-2 minutes.');
      videoPreview.classList.remove('show');

      try {
        const response = await fetch('/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!result.success) {
          throw new Error(result.error || 'Generation failed');
        }

        // Check if video is ready or still processing
        if (!result.video_url) {
          // Video is being generated - show the full response for debugging
          showStatus('loading', \`Video generation started. Status: \${result.status || 'processing'}. Task ID: \${result.id}. Response: \${JSON.stringify(result.data)}\`);
          return;
        }

        currentVideoUrl = result.video_url;
        currentMetadata = result.metadata;

        // Show success
        showStatus('success', \`Video generated successfully! ID: \${result.id}\`);

        // Load video
        generatedVideo.src = currentVideoUrl;
        videoPreview.classList.add('show');

      } catch (error) {
        showStatus('error', \`Error: \${error.message}\`);
      } finally {
        generateBtn.disabled = false;
        generateBtn.innerHTML = 'Generate Video ($0.20)';
      }
    });

    downloadBtn.addEventListener('click', async () => {
      if (!currentVideoUrl) return;

      try {
        downloadBtn.disabled = true;
        downloadBtn.innerHTML = '<span class="spinner"></span>Downloading...';

        const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, -5);
        const filename = \`cogvideox3_\${timestamp}.mp4\`;

        const response = await fetch('/download', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ video_url: currentVideoUrl, filename })
        });

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);

        showStatus('success', 'Video downloaded successfully!');
      } catch (error) {
        showStatus('error', \`Download failed: \${error.message}\`);
      } finally {
        downloadBtn.disabled = false;
        downloadBtn.innerHTML = 'Download Video';
      }
    });

    function showStatus(type, message) {
      status.className = \`status show \${type}\`;
      status.textContent = message;
    }
  </script>
</body>
</html>`;
