#!/usr/bin/env python3
"""
Universal Kie.ai API Client
Handles all VEO 3 operations: generate, poll, download, file upload, frame extraction
"""

import requests
import json
import base64
import time
import subprocess
from pathlib import Path
from typing import Optional, Dict, List
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class KieClient:
    """Universal client for all Kie.ai VEO 3 operations"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or "20108f4bba626227a1bb5e281d1e5a64"
        self.veo_base_url = "https://api.kie.ai/api/v1/veo"
        self.upload_url = "https://kieai.redpandaai.co/api/file-base64-upload"
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def generate_video(
        self,
        prompt: str,
        model: str = "veo3_fast",
        aspect_ratio: str = "16:9",
        image_url: Optional[str] = None,
        enable_fallback: bool = True,
        enable_translation: bool = True,
        watermark: Optional[str] = None
    ) -> Dict:
        """
        Generate a video with VEO 3

        Args:
            prompt: Video description prompt
            model: "veo3" or "veo3_fast"
            aspect_ratio: "16:9" or "9:16"
            image_url: Optional image URL for image-to-video
            enable_fallback: Enable fallback (25% higher success)
            enable_translation: Auto-translate prompts
            watermark: Optional watermark text

        Returns:
            Dict with task_id and generation info
        """
        payload = {
            "prompt": prompt,
            "model": model,
            "aspectRatio": aspect_ratio,
            "enableFallback": enable_fallback,
            "enableTranslation": enable_translation
        }

        if image_url:
            payload["imageUrls"] = [image_url]

        if watermark:
            payload["watermark"] = watermark

        logger.info(f"Generating video with {model}")
        if image_url:
            logger.info(f"Image-to-video: {image_url}")

        response = requests.post(
            f"{self.veo_base_url}/generate",
            headers=self.headers,
            json=payload
        )

        result = response.json()

        if result.get('code') in [0, 200]:
            task_id = result['data']['taskId']
            logger.info(f"✅ Generation started. Task ID: {task_id}")
            return {
                'task_id': task_id,
                'model': model,
                'aspect_ratio': aspect_ratio,
                'has_image': bool(image_url)
            }
        else:
            raise Exception(f"Generation failed: {result}")

    def get_status(self, task_id: str) -> Dict:
        """
        Get generation status

        Args:
            task_id: Generation task ID

        Returns:
            Dict with status info
        """
        response = requests.get(
            f"{self.veo_base_url}/record-info",
            headers=self.headers,
            params={"taskId": task_id}
        )

        result = response.json()

        if result.get('code') in [0, 200]:
            data = result['data']

            # Determine status from successFlag and response
            success_flag = data.get('successFlag')
            if success_flag == 1:
                status = 'SUCCESS'
            elif success_flag == -1:
                status = 'FAILED'
            elif data.get('errorMessage'):
                status = 'ERROR'
            else:
                status = 'PROCESSING'

            video_url = None
            if data.get('response'):
                video_url = data['response'].get('resultUrls', [None])[0]

            return {
                'task_id': task_id,
                'status': status,
                'video_url': video_url,
                'error_message': data.get('errorMessage'),
                'complete_time': data.get('completeTime'),
                'create_time': data.get('createTime')
            }
        else:
            raise Exception(f"Status check failed: {result}")

    def poll_until_complete(
        self,
        task_id: str,
        timeout: int = 1200,
        poll_interval: int = 60,
        verbose: bool = True
    ) -> Dict:
        """
        Poll generation until complete or timeout

        Args:
            task_id: Generation task ID
            timeout: Max wait time in seconds (default 20min)
            poll_interval: Seconds between checks (default 60s)
            verbose: Print status updates

        Returns:
            Complete status dict with video_url
        """
        if verbose:
            logger.info(f"⏳ Polling for completion...")
            logger.info(f"   Timeout: {timeout}s | Interval: {poll_interval}s")

        start_time = time.time()

        while (time.time() - start_time) < timeout:
            status_info = self.get_status(task_id)
            status = status_info['status']

            if verbose:
                elapsed = int(time.time() - start_time)
                logger.info(f"   [{elapsed}s] Status: {status}")

            if status == 'SUCCESS':
                if verbose:
                    logger.info(f"✅ Generation complete!")
                    logger.info(f"🎥 Video URL: {status_info['video_url']}")
                return status_info

            elif status in ['FAILED', 'ERROR']:
                error_msg = status_info.get('error_message', 'Unknown error')
                raise Exception(f"Generation failed: {error_msg}")

            time.sleep(poll_interval)

        raise TimeoutError(f"Generation timeout after {timeout}s")

    def get_1080p_video(self, task_id: str) -> str:
        """
        Get 1080p version of generated video

        Args:
            task_id: Generation task ID

        Returns:
            URL to 1080p video
        """
        logger.info(f"📹 Requesting 1080p version...")

        response = requests.get(
            f"{self.veo_base_url}/get-1080p-video",
            headers=self.headers,
            params={"taskId": task_id}
        )

        result = response.json()

        if result.get('code') == 0:
            video_url = result['data'].get('videoUrl')
            logger.info(f"✅ 1080p URL: {video_url}")
            return video_url
        else:
            raise Exception(f"1080p request failed: {result}")

    def download_video(self, video_url: str, output_path: Path, resolution: str = "720p") -> Path:
        """
        Download video from URL

        Args:
            video_url: URL to video file
            output_path: Path to save video
            resolution: "720p" or "1080p" (for labeling)

        Returns:
            Path to downloaded video
        """
        logger.info(f"⬇️  Downloading video ({resolution})...")

        response = requests.get(video_url, stream=True)
        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        file_size = output_path.stat().st_size / (1024 * 1024)
        logger.info(f"✅ Downloaded: {output_path} ({file_size:.2f} MB)")

        return output_path

    def extract_last_frame(self, video_path: Path, output_path: Optional[Path] = None) -> Path:
        """
        Extract last frame from video using FFmpeg

        Args:
            video_path: Path to video file
            output_path: Optional output path (auto-generated if not provided)

        Returns:
            Path to extracted frame
        """
        if output_path is None:
            output_path = video_path.parent / f"{video_path.stem}_ending.jpg"

        logger.info(f"📸 Extracting last frame...")

        cmd = [
            'ffmpeg',
            '-sseof', '-0.1',  # 0.1s before end
            '-i', str(video_path),
            '-vframes', '1',
            '-q:v', '2',  # High quality
            '-y',
            str(output_path)
        ]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result.returncode != 0:
            raise Exception(f"FFmpeg failed: {result.stderr.decode()}")

        logger.info(f"✅ Extracted: {output_path}")
        return output_path

    def upload_image(self, image_path: Path, upload_path: str = "veo3-scenes") -> str:
        """
        Upload image to Kie.ai for use in image-to-video

        Args:
            image_path: Path to image file
            upload_path: Remote path on Kie.ai

        Returns:
            URL of uploaded image (valid for 3 days)
        """
        logger.info(f"📤 Uploading image: {image_path.name}...")

        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        # Detect MIME type
        suffix = image_path.suffix.lower()
        mime_types = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.webp': 'image/webp'
        }
        mime_type = mime_types.get(suffix, 'image/jpeg')

        payload = {
            'base64Data': f'data:{mime_type};base64,{image_data}',
            'uploadPath': upload_path,
            'fileName': image_path.name
        }

        response = requests.post(
            self.upload_url,
            headers=self.headers,
            json=payload
        )

        result = response.json()

        if result.get('success') or result.get('code') == 200:
            image_url = result['data']['downloadUrl']
            logger.info(f"✅ Uploaded: {image_url}")
            logger.info(f"⏰ Auto-deletes after 3 days")
            return image_url
        else:
            raise Exception(f"Upload failed: {result}")

    def generate_and_wait(
        self,
        prompt: str,
        model: str = "veo3_fast",
        aspect_ratio: str = "16:9",
        image_path: Optional[Path] = None,
        output_dir: Path = Path("output"),
        scene_name: str = "video",
        download: bool = True,
        extract_frame: bool = True,
        analyze_quality: bool = False
    ) -> Dict:
        """
        Complete workflow: Upload image (if provided) → Generate → Poll → Download → Extract frame

        Args:
            prompt: Video prompt
            model: veo3 or veo3_fast
            aspect_ratio: 16:9 or 9:16
            image_path: Optional starting frame for image-to-video
            output_dir: Where to save outputs
            scene_name: Name for output files
            download: Whether to download video
            extract_frame: Whether to extract last frame

        Returns:
            Dict with all info (task_id, video_path, frame_path, frame_url)
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Step 1: Upload image if provided
        image_url = None
        if image_path:
            image_url = self.upload_image(image_path)

        # Step 2: Generate
        gen_info = self.generate_video(
            prompt=prompt,
            model=model,
            aspect_ratio=aspect_ratio,
            image_url=image_url
        )

        # Step 3: Poll until complete
        status_info = self.poll_until_complete(gen_info['task_id'])

        result = {
            'task_id': gen_info['task_id'],
            'video_url': status_info['video_url'],
            'model': model,
            'aspect_ratio': aspect_ratio
        }

        # Step 4: Download video
        if download:
            video_path = output_dir / f"{scene_name}.mp4"
            self.download_video(status_info['video_url'], video_path)
            result['video_path'] = str(video_path)

            # Step 5: Extract last frame
            if extract_frame:
                frame_path = self.extract_last_frame(video_path)
                result['frame_path'] = str(frame_path)

                # Optionally upload frame for next scene
                # frame_url = self.upload_image(frame_path)
                # result['frame_url'] = frame_url

            # Step 6: Auto-analyze quality if requested
            if analyze_quality:
                try:
                    from scripts.video_quality_analyzer import VideoQualityAnalyzer
                    analyzer = VideoQualityAnalyzer()

                    logger.info("🔍 Running quick quality analysis...")
                    frames = analyzer.extract_frames_at_intervals(
                        video_path,
                        interval=2.0  # Every 2 seconds for 8s video
                    )

                    logger.info(f"   Extracted {len(frames)} frames for review")
                    logger.info("   Check frames if quality issues detected")

                    # Auto-cleanup after
                    if frames:
                        analyzer.cleanup_analysis_folder(frames[0].parent)

                except Exception as e:
                    logger.warning(f"Quality analysis skipped: {e}")

        return result


def main():
    """Example usage"""
    client = KieClient()

    # Example 1: Simple text-to-video
    print("Example 1: Text-to-video")
    result = client.generate_and_wait(
        prompt="A cinematic shot of a person walking through a forest",
        model="veo3_fast",
        scene_name="example_scene",
        output_dir=Path("output/examples")
    )
    print(json.dumps(result, indent=2))

    # Example 2: Image-to-video with frame extraction
    # result = client.generate_and_wait(
    #     prompt="Camera pans right revealing the landscape",
    #     image_path=Path("path/to/starting_frame.jpg"),
    #     scene_name="continued_scene",
    #     extract_frame=True
    # )


if __name__ == "__main__":
    main()