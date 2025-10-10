/**
 * CogVideoX-3 & Vidu Q1 Video Generator
 * Modern dark UI with shadcn components
 */

const ZAI_API_KEY = '63e0189e8180410ca2ee151d2c020e31.Cd0DIl75hBTd9UpM';
const ZAI_BASE_URL = 'https://api.z.ai/api/paas/v4';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    if (url.pathname === '/favicon.ico') {
      return new Response('🎬', {
        headers: { 'Content-Type': 'text/plain', ...corsHeaders }
      });
    }

    if (request.method === 'GET' && url.pathname === '/') {
      return new Response(HTML_UI, {
        headers: { 'Content-Type': 'text/html', ...corsHeaders }
      });
    }

    // Upload image
    if (request.method === 'POST' && url.pathname === '/upload') {
      try {
        const formData = await request.formData();
        const file = formData.get('file');
        if (!file) throw new Error('No file provided');

        const arrayBuffer = await file.arrayBuffer();
        const base64 = btoa(String.fromCharCode(...new Uint8Array(arrayBuffer)));
        const dataUrl = `data:${file.type || 'image/jpeg'};base64,${base64}`;

        return new Response(JSON.stringify({ success: true, data_url: dataUrl }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      } catch (error) {
        return new Response(JSON.stringify({ success: false, error: error.message }), {
          status: 500,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }
    }

    // Generate video
    if (request.method === 'POST' && url.pathname === '/generate') {
      try {
        const body = await request.json();

        const zaiRequest = { model: body.model || 'cogvideox-3', prompt: body.prompt };

        if (body.model?.startsWith('viduq1')) {
          zaiRequest.duration = 5;
          zaiRequest.aspect_ratio = body.aspect_ratio || '16:9';
          if (body.style) zaiRequest.style = body.style;
        } else {
          zaiRequest.quality = body.quality || 'quality';
          zaiRequest.with_audio = body.with_audio !== false;
          zaiRequest.size = body.size || '1920x1080';
          zaiRequest.fps = body.fps || 30;
        }

        if (body.start_image && body.end_image) {
          zaiRequest.image_url = [body.start_image, body.end_image];
        } else if (body.start_image) {
          zaiRequest.image_url = body.start_image;
        }

        const response = await fetch(`${ZAI_BASE_URL}/videos/generations`, {
          method: 'POST',
          headers: { 'Authorization': `Bearer ${ZAI_API_KEY}`, 'Content-Type': 'application/json' },
          body: JSON.stringify(zaiRequest)
        });

        const contentType = response.headers.get('content-type');
        let result;

        if (contentType?.includes('application/json')) {
          result = await response.json();
        } else {
          const text = await response.text();
          throw new Error(`API error (${response.status}): ${text.substring(0, 200)}`);
        }

        if (!response.ok) {
          throw new Error(result.error?.message || result.message || 'API request failed');
        }

        const videoData = result.data || result;
        let videoUrl = videoData.video_url;
        if (!videoUrl && videoData.video_result?.[0]) {
          videoUrl = videoData.video_result[0].url;
        }

        return new Response(JSON.stringify({
          success: true,
          task_id: videoData.id || videoData.task_id,
          status: videoData.task_status || videoData.status,
          video_url: videoUrl,
          data: videoData
        }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });

      } catch (error) {
        return new Response(JSON.stringify({ success: false, error: error.message }), {
          status: 500,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }
    }

    // Poll status
    if (request.method === 'GET' && url.pathname.startsWith('/status/')) {
      try {
        const taskId = url.pathname.split('/')[2];

        const response = await fetch(`${ZAI_BASE_URL}/async-result/${taskId}`, {
          headers: { 'Authorization': `Bearer ${ZAI_API_KEY}` }
        });

        const result = await response.json();
        const videoData = result.data || result;

        let videoUrl = videoData.video_url;
        if (!videoUrl && videoData.video_result?.[0]) {
          videoUrl = videoData.video_result[0].url;
        }

        return new Response(JSON.stringify({
          success: true,
          status: videoData.task_status || videoData.status,
          video_url: videoUrl,
          cover_image_url: videoData.video_result?.[0]?.cover_image_url,
          data: videoData
        }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });

      } catch (error) {
        return new Response(JSON.stringify({ success: false, error: error.message }), {
          status: 500,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }
    }

    return new Response('Not Found', { status: 404, headers: corsHeaders });
  }
};

const HTML_UI = `<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Video Generator</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            border: 'hsl(240 3.7% 15.9%)',
            background: 'hsl(240 10% 3.9%)',
            foreground: 'hsl(0 0% 98%)',
            primary: { DEFAULT: 'hsl(0 0% 98%)', foreground: 'hsl(240 5.9% 10%)' },
            secondary: { DEFAULT: 'hsl(240 3.7% 15.9%)', foreground: 'hsl(0 0% 98%)' },
            muted: { DEFAULT: 'hsl(240 3.7% 15.9%)', foreground: 'hsl(240 5% 64.9%)' },
            accent: { DEFAULT: 'hsl(240 3.7% 15.9%)', foreground: 'hsl(0 0% 98%)' },
          }
        }
      }
    }
  </script>
  <style>
    @keyframes spin { to { transform: rotate(360deg); } }
    .spinner {
      display: inline-block; width: 16px; height: 16px;
      border: 2px solid rgba(255,255,255,0.3);
      border-radius: 50%; border-top-color: white;
      animation: spin 0.6s linear infinite; margin-right: 8px;
    }
  </style>
</head>
<body class="bg-background text-foreground min-h-screen">
  <div class="container mx-auto px-4 py-8 max-w-4xl">
    <div class="mb-8">
      <h1 class="text-4xl font-bold mb-2">🎬 AI Video Generator</h1>
      <p class="text-muted-foreground">CogVideoX-3 & Vidu Q1 • Up to 4K • Native Audio</p>
    </div>

    <form id="videoForm" class="space-y-6">
      <!-- Model Selector -->
      <div class="space-y-2">
        <label class="text-sm font-medium">Model</label>
        <div class="grid grid-cols-2 gap-3">
          <button type="button" data-model="cogvideox-3" class="model-btn border-2 border-primary bg-primary/10 rounded-lg p-3 text-left hover:bg-primary/20 transition">
            <div class="font-semibold">CogVideoX-3</div>
            <div class="text-xs text-muted-foreground">Up to 4K • 30/60fps • Audio • $0.20</div>
          </button>
          <button type="button" data-model="viduq1-text" class="model-btn border-2 border-border rounded-lg p-3 text-left hover:bg-accent transition">
            <div class="font-semibold">Vidu Q1</div>
            <div class="text-xs text-muted-foreground">5s • 1080p • General/Anime • $0.40</div>
          </button>
        </div>
      </div>

      <!-- Prompt -->
      <div class="space-y-2">
        <label class="text-sm font-medium">Prompt</label>
        <textarea id="prompt" rows="3" required
          class="w-full bg-secondary border border-input rounded-lg px-4 py-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-ring"
          placeholder="A serene sunrise over misty mountains, camera slowly panning right..."
        ></textarea>
      </div>

      <!-- Image Uploads -->
      <div id="imageUploads" class="grid md:grid-cols-2 gap-4">
        <div class="space-y-2">
          <label class="text-sm font-medium">Start Frame <span class="text-xs text-muted-foreground">(Optional)</span></label>
          <div id="startZone" class="border-2 border-dashed border-border rounded-lg p-6 text-center cursor-pointer hover:border-primary/50 transition min-h-[140px] flex items-center justify-center">
            <input type="file" id="startFile" accept="image/*" class="hidden">
            <div class="upload-content">
              <div class="text-4xl mb-2">📸</div>
              <p class="text-sm text-muted-foreground">Drop or click</p>
            </div>
            <img id="startPreview" class="hidden max-h-[140px] rounded-lg">
          </div>
          <input type="url" id="startUrl" placeholder="Or paste image URL..." 
            class="w-full bg-secondary border border-input rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-ring">
        </div>
        <div id="endFrameContainer" class="space-y-2">
          <label class="text-sm font-medium">
            End Frame <span class="text-xs text-muted-foreground">(Optional - for precise control)</span>
          </label>
          <div id="endZone" class="border-2 border-dashed border-border rounded-lg p-6 text-center cursor-pointer hover:border-primary/50 transition min-h-[140px] flex items-center justify-center">
            <input type="file" id="endFile" accept="image/*" class="hidden">
            <div class="upload-content">
              <div class="text-4xl mb-2">📸</div>
              <p class="text-sm text-muted-foreground">Drop or click</p>
            </div>
            <img id="endPreview" class="hidden max-h-[140px] rounded-lg">
          </div>
          <input type="url" id="endUrl" placeholder="Or paste image URL..." 
            class="w-full bg-secondary border border-input rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-ring">
        </div>
      </div>

      <!-- Settings -->
      <div id="cogvideoxSettings" class="grid grid-cols-2 md:grid-cols-4 gap-3">
        <div class="space-y-2">
          <label class="text-sm font-medium">Resolution</label>
          <select id="size" class="w-full bg-secondary border border-input rounded-lg px-3 py-2 text-sm">
            <option value="1280x720">720p</option>
            <option value="1920x1080" selected>1080p</option>
            <option value="3840x2160">4K</option>
          </select>
        </div>
        <div class="space-y-2">
          <label class="text-sm font-medium">FPS</label>
          <select id="fps" class="w-full bg-secondary border border-input rounded-lg px-3 py-2 text-sm">
            <option value="30" selected>30</option>
            <option value="60">60</option>
          </select>
        </div>
        <div class="space-y-2">
          <label class="text-sm font-medium">Quality</label>
          <select id="quality" class="w-full bg-secondary border border-input rounded-lg px-3 py-2 text-sm">
            <option value="quality" selected>Quality</option>
            <option value="speed">Speed</option>
          </select>
        </div>
        <div class="space-y-2">
          <label class="text-sm font-medium">Audio</label>
          <label class="flex items-center space-x-2 bg-secondary border border-input rounded-lg px-3 py-2 cursor-pointer">
            <input type="checkbox" id="audio" checked class="rounded">
            <span class="text-sm">Enable</span>
          </label>
        </div>
      </div>

      <div id="viduSettings" class="hidden grid grid-cols-2 gap-3">
        <div class="space-y-2">
          <label class="text-sm font-medium">Style</label>
          <select id="style" class="w-full bg-secondary border border-input rounded-lg px-3 py-2 text-sm">
            <option value="general">General</option>
            <option value="anime">Anime</option>
          </select>
        </div>
        <div class="space-y-2">
          <label class="text-sm font-medium">Aspect Ratio</label>
          <select id="aspectRatio" class="w-full bg-secondary border border-input rounded-lg px-3 py-2 text-sm">
            <option value="16:9" selected>16:9</option>
            <option value="9:16">9:16</option>
            <option value="1:1">1:1</option>
          </select>
        </div>
      </div>

      <button type="submit" id="generateBtn"
        class="w-full bg-primary text-primary-foreground font-semibold py-3 px-6 rounded-lg hover:opacity-90 transition">
        Generate Video
      </button>
    </form>

    <!-- Status -->
    <div id="status" class="hidden mt-6 p-4 rounded-lg"></div>

    <!-- Video Preview -->
    <div id="videoPreview" class="hidden mt-6 space-y-4">
      <video id="video" controls class="w-full rounded-lg bg-black"></video>
      <button id="downloadBtn"
        class="w-full bg-secondary hover:bg-accent font-semibold py-3 px-6 rounded-lg transition">
        Download Video
      </button>
    </div>
  </div>

  <script>
    let selectedModel = 'cogvideox-3';
    let startImage = null;
    let endImage = null;
    let currentVideoUrl = null;
    let pollInterval = null;

    // Model selection
    document.querySelectorAll('.model-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.model-btn').forEach(b => {
          b.classList.remove('border-primary', 'bg-primary/10');
          b.classList.add('border-border');
        });
        btn.classList.remove('border-border');
        btn.classList.add('border-primary', 'bg-primary/10');

        selectedModel = btn.dataset.model;

        // Toggle settings
        if (selectedModel.startsWith('viduq1')) {
          document.getElementById('cogvideoxSettings').classList.add('hidden');
          document.getElementById('viduSettings').classList.remove('hidden');
        } else {
          document.getElementById('cogvideoxSettings').classList.remove('hidden');
          document.getElementById('viduSettings').classList.add('hidden');
        }

        updateEndFrameVisibility();
      });
    });

    function updateEndFrameVisibility() {
      const endContainer = document.getElementById('endFrameContainer');
      const hasStartImage = startImage || document.getElementById('startUrl').value;
      
      // Show end frame only if:
      // 1. Model is CogVideoX-3 (supports start+end)
      // 2. OR model is viduq1-start-end
      // 3. AND there's a start image
      
      const supportsEndFrame = selectedModel === 'cogvideox-3' || selectedModel === 'viduq1-start-end';
      
      if (supportsEndFrame && hasStartImage) {
        endContainer.classList.remove('opacity-50', 'pointer-events-none');
      } else {
        endContainer.classList.add('opacity-50', 'pointer-events-none');
      }
    }

    // File upload handlers
    function setupUpload(zoneId, fileId, previewId, urlId, target) {
      const zone = document.getElementById(zoneId);
      const file = document.getElementById(fileId);
      const preview = document.getElementById(previewId);
      const urlInput = document.getElementById(urlId);

      zone.addEventListener('click', () => file.click());
      zone.addEventListener('dragover', (e) => {
        e.preventDefault();
        zone.classList.add('border-primary');
      });
      zone.addEventListener('dragleave', () => {
        zone.classList.remove('border-primary');
      });
      zone.addEventListener('drop', async (e) => {
        e.preventDefault();
        zone.classList.remove('border-primary');
        if (e.dataTransfer.files[0]) await handleFile(e.dataTransfer.files[0], preview, target);
      });
      file.addEventListener('change', async (e) => {
        if (e.target.files[0]) await handleFile(e.target.files[0], preview, target);
      });

      // Handle URL input
      urlInput.addEventListener('input', () => {
        if (urlInput.value) {
          preview.src = urlInput.value;
          preview.classList.remove('hidden');
          preview.previousElementSibling.classList.add('hidden');
          if (target === 'start') startImage = urlInput.value;
          else endImage = urlInput.value;
          updateEndFrameVisibility();
        } else {
          preview.classList.add('hidden');
          preview.previousElementSibling.classList.remove('hidden');
          if (target === 'start') startImage = null;
          else endImage = null;
          updateEndFrameVisibility();
        }
      });
    }

    async function handleFile(file, preview, target) {
      const formData = new FormData();
      formData.append('file', file);

      const res = await fetch('/upload', { method: 'POST', body: formData });
      const result = await res.json();

      if (result.success) {
        preview.src = result.data_url;
        preview.classList.remove('hidden');
        preview.previousElementSibling.classList.add('hidden');
        if (target === 'start') startImage = result.data_url;
        else endImage = result.data_url;
        updateEndFrameVisibility();
      }
    }

    setupUpload('startZone', 'startFile', 'startPreview', 'startUrl', 'start');
    setupUpload('endZone', 'endFile', 'endPreview', 'endUrl', 'end');

    // Form submission
    document.getElementById('videoForm').addEventListener('submit', async (e) => {
      e.preventDefault();

      const data = {
        model: selectedModel,
        prompt: document.getElementById('prompt').value,
        start_image: startImage,
        end_image: endImage
      };

      if (selectedModel.startsWith('viduq1')) {
        data.style = document.getElementById('style').value;
        data.aspect_ratio = document.getElementById('aspectRatio').value;
        
        // Auto-select correct Vidu model based on images
        if (startImage && endImage) {
          data.model = 'viduq1-start-end';
        } else if (startImage) {
          data.model = 'viduq1-image';
        } else {
          data.model = 'viduq1-text';
        }
      } else {
        data.size = document.getElementById('size').value;
        data.fps = parseInt(document.getElementById('fps').value);
        data.quality = document.getElementById('quality').value;
        data.with_audio = document.getElementById('audio').checked;
      }

      const btn = document.getElementById('generateBtn');
      btn.disabled = true;
      btn.innerHTML = '<span class="spinner"></span>Generating...';

      showStatus('loading', 'Starting video generation...');

      try {
        const res = await fetch('/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });

        const result = await res.json();

        if (!result.success) throw new Error(result.error);

        if (result.video_url) {
          showVideo(result.video_url);
        } else {
          pollStatus(result.task_id);
        }

      } catch (error) {
        showStatus('error', error.message);
        btn.disabled = false;
        btn.innerHTML = 'Generate Video';
      }
    });

    function pollStatus(taskId) {
      showStatus('loading', \`Processing... (ID: \${taskId})\`);

      pollInterval = setInterval(async () => {
        try {
          const res = await fetch(\`/status/\${taskId}\`);
          const result = await res.json();

          if (result.status === 'SUCCESS' && result.video_url) {
            clearInterval(pollInterval);
            showVideo(result.video_url);
          } else if (result.status === 'FAILED') {
            clearInterval(pollInterval);
            showStatus('error', 'Video generation failed');
            document.getElementById('generateBtn').disabled = false;
            document.getElementById('generateBtn').innerHTML = 'Generate Video';
          }
        } catch (error) {
          clearInterval(pollInterval);
          showStatus('error', 'Polling failed: ' + error.message);
        }
      }, 3000);
    }

    function showVideo(url) {
      clearInterval(pollInterval);
      currentVideoUrl = url;
      document.getElementById('video').src = url;
      document.getElementById('videoPreview').classList.remove('hidden');
      showStatus('success', 'Video generated successfully!');
      document.getElementById('generateBtn').disabled = false;
      document.getElementById('generateBtn').innerHTML = 'Generate Video';
    }

    function showStatus(type, message) {
      const status = document.getElementById('status');
      status.className = 'block mt-6 p-4 rounded-lg ';
      if (type === 'loading') status.className += 'bg-blue-500/10 border border-blue-500/20 text-blue-400';
      else if (type === 'success') status.className += 'bg-green-500/10 border border-green-500/20 text-green-400';
      else status.className += 'bg-red-500/10 border border-red-500/20 text-red-400';
      status.textContent = message;
    }

    // Download
    document.getElementById('downloadBtn').addEventListener('click', () => {
      if (!currentVideoUrl) return;
      const a = document.createElement('a');
      a.href = currentVideoUrl;
      a.download = \`video_\${Date.now()}.mp4\`;
      a.click();
    });

    // Initial state
    updateEndFrameVisibility();
  </script>
</body>
</html>`;
