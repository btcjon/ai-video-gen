#!/usr/bin/env node

/**
 * Script to download videos from CogVideoX-3 and save to docs/output
 * Usage: node save-video.js <video_url> [filename]
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');

const OUTPUT_DIR = path.join(__dirname, 'docs', 'output');

async function downloadVideo(videoUrl, filename) {
  // Ensure output directory exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Generate filename if not provided
  if (!filename) {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, -5);
    filename = `cogvideox3_${timestamp}.mp4`;
  }

  // Ensure .mp4 extension
  if (!filename.endsWith('.mp4')) {
    filename += '.mp4';
  }

  const outputPath = path.join(OUTPUT_DIR, filename);

  return new Promise((resolve, reject) => {
    const protocol = videoUrl.startsWith('https') ? https : http;

    protocol.get(videoUrl, (response) => {
      if (response.statusCode === 301 || response.statusCode === 302) {
        // Handle redirects
        downloadVideo(response.headers.location, filename)
          .then(resolve)
          .catch(reject);
        return;
      }

      if (response.statusCode !== 200) {
        reject(new Error(`Failed to download: HTTP ${response.statusCode}`));
        return;
      }

      const fileStream = fs.createWriteStream(outputPath);
      let downloadedBytes = 0;
      const totalBytes = parseInt(response.headers['content-length'] || '0');

      response.on('data', (chunk) => {
        downloadedBytes += chunk.length;
        if (totalBytes > 0) {
          const percent = ((downloadedBytes / totalBytes) * 100).toFixed(1);
          process.stdout.write(`\rDownloading: ${percent}% (${(downloadedBytes / 1024 / 1024).toFixed(2)} MB)`);
        }
      });

      response.pipe(fileStream);

      fileStream.on('finish', () => {
        fileStream.close();
        console.log(`\n✅ Video saved to: ${outputPath}`);
        resolve(outputPath);
      });

      fileStream.on('error', (err) => {
        fs.unlink(outputPath, () => {});
        reject(err);
      });
    }).on('error', reject);
  });
}

// CLI usage
if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.error('Usage: node save-video.js <video_url> [filename]');
    process.exit(1);
  }

  const [videoUrl, filename] = args;

  downloadVideo(videoUrl, filename)
    .then(() => process.exit(0))
    .catch((error) => {
      console.error('❌ Error:', error.message);
      process.exit(1);
    });
}

module.exports = { downloadVideo };
