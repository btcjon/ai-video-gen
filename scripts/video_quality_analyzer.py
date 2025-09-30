#!/usr/bin/env python3
"""
Video Quality Analyzer
Extracts frames at regular intervals from a video for quality inspection
This allows reviewing what actually happened vs what was prompted
"""

import subprocess
import json
from pathlib import Path
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class VideoQualityAnalyzer:
    """Extract and analyze frames from generated videos"""

    def __init__(self):
        self.analysis_dir = Path("output/quality_analysis")
        self.analysis_dir.mkdir(parents=True, exist_ok=True)

    def extract_frames_at_intervals(
        self,
        video_path: Path,
        interval: float = 1.0,
        output_dir: Path = None
    ) -> List[Path]:
        """
        Extract frames at regular intervals from video

        Args:
            video_path: Path to video file
            interval: Seconds between frame extractions (default 1s)
            output_dir: Where to save frames (auto-created if None)

        Returns:
            List of extracted frame paths
        """
        if not video_path.exists():
            raise FileNotFoundError(f"Video not found: {video_path}")

        # Create output directory
        if output_dir is None:
            output_dir = self.analysis_dir / video_path.stem
        output_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f"📹 Analyzing: {video_path.name}")
        logger.info(f"   Extracting frames every {interval}s")

        # Get video duration
        duration = self.get_video_duration(video_path)
        logger.info(f"   Video duration: {duration:.2f}s")

        # Calculate frame extraction points
        extraction_points = []
        current_time = 0
        while current_time <= duration:
            extraction_points.append(current_time)
            current_time += interval

        # Extract frames
        extracted_frames = []
        for i, timestamp in enumerate(extraction_points):
            output_path = output_dir / f"frame_{i:02d}_at_{timestamp:.1f}s.jpg"

            cmd = [
                'ffmpeg',
                '-ss', str(timestamp),
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

            if result.returncode == 0 and output_path.exists():
                extracted_frames.append(output_path)
                logger.info(f"   ✅ Frame {i:02d} @ {timestamp:.1f}s")
            else:
                logger.warning(f"   ❌ Failed @ {timestamp:.1f}s")

        logger.info(f"📸 Extracted {len(extracted_frames)} frames to {output_dir}")
        return extracted_frames

    def get_video_duration(self, video_path: Path) -> float:
        """Get video duration in seconds"""
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-show_entries', 'format=duration',
            '-of', 'json',
            str(video_path)
        ]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result.returncode == 0:
            data = json.loads(result.stdout)
            return float(data['format']['duration'])
        return 0.0

    def analyze_scene_consistency(
        self,
        video_path: Path,
        expected_elements: Dict[str, List[str]],
        cleanup_after: bool = True
    ) -> Dict:
        """
        Analyze a video for consistency with expected elements

        Args:
            video_path: Path to video
            expected_elements: Dict of what should be in the video
                {
                    "character": ["weathered face", "green jacket", "stubble"],
                    "environment": ["oak tree", "water jug", "wilderness"],
                    "lighting": ["sunset→night", "moonlight", "stars"],
                    "actions": ["meditation", "opens eyes", "looks at jug"]
                }
            cleanup_after: Remove extracted frames after analysis (default True)

        Returns:
            Analysis report dict
        """
        frames = self.extract_frames_at_intervals(video_path)

        report = {
            "video": video_path.name,
            "frames_extracted": len(frames),
            "frame_paths": [str(f) for f in frames],
            "expected_elements": expected_elements,
            "analysis": {
                "beginning": f"Check {frames[0].name} for initial state",
                "middle": f"Check {frames[len(frames)//2].name} for transition",
                "ending": f"Check {frames[-1].name} for final state"
            },
            "quality_checklist": {
                "character_consistency": "Review face/clothing across all frames",
                "environment_stability": "Check if oak tree remains visible",
                "lighting_progression": "Verify sunset→twilight→night transition",
                "action_completion": "Confirm all prompted actions occurred"
            }
        }

        # Save analysis report
        report_path = frames[0].parent / "analysis_report.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)

        logger.info(f"📊 Analysis saved: {report_path}")

        # Cleanup if requested
        if cleanup_after and frames:
            self.cleanup_analysis_folder(frames[0].parent)

        return report

    def cleanup_analysis_folder(self, folder_path: Path):
        """Remove analysis folder after review"""
        import shutil
        try:
            shutil.rmtree(folder_path)
            logger.info(f"🧹 Cleaned up: {folder_path}")
        except Exception as e:
            logger.warning(f"Could not cleanup {folder_path}: {e}")

    def compare_prompts_to_frames(
        self,
        video_path: Path,
        prompt: str,
        interval: float = 2.0
    ) -> Dict:
        """
        Extract frames and compare to original prompt

        Args:
            video_path: Video to analyze
            prompt: Original generation prompt
            interval: Frame extraction interval (default 2s for 8s videos)

        Returns:
            Comparison report
        """
        frames = self.extract_frames_at_intervals(video_path, interval)

        # Parse prompt for time-based expectations
        prompt_segments = []
        if "0-2 seconds" in prompt:
            prompt_segments.append((0, 2, "Initial state"))
        if "2-4 seconds" in prompt:
            prompt_segments.append((2, 4, "First transition"))
        if "4-6 seconds" in prompt:
            prompt_segments.append((4, 6, "Second transition"))
        if "6-8 seconds" in prompt:
            prompt_segments.append((6, 8, "Final state"))

        report = {
            "video": video_path.name,
            "prompt_summary": prompt[:200] + "...",
            "frame_analysis": []
        }

        for i, frame in enumerate(frames):
            timestamp = i * interval
            segment_desc = "Unknown"

            for start, end, desc in prompt_segments:
                if start <= timestamp < end:
                    segment_desc = desc
                    break

            report["frame_analysis"].append({
                "frame": frame.name,
                "timestamp": f"{timestamp}s",
                "expected_segment": segment_desc,
                "check_for": f"Review this frame for {segment_desc}"
            })

        return report


def main():
    """Example usage"""
    analyzer = VideoQualityAnalyzer()

    # Analyze Scene 4
    video_path = Path("output/h2o_pure_test/scene_04_with_edited_image.mp4")

    if video_path.exists():
        # Extract frames every second
        frames = analyzer.extract_frames_at_intervals(video_path, interval=1.0)

        # Analyze for expected elements
        expected = {
            "character": ["weathered face", "green jacket", "stubble", "meditation pose"],
            "environment": ["oak tree visible throughout", "water jug", "wilderness"],
            "lighting": ["sunset start", "twilight middle", "night with stars end"],
            "actions": ["sitting meditation", "opens eyes at end", "looks at jug"]
        }

        report = analyzer.analyze_scene_consistency(video_path, expected)

        print("\n" + "=" * 70)
        print("QUALITY ANALYSIS COMPLETE")
        print("=" * 70)
        print(f"Frames extracted: {len(frames)}")
        print(f"Check these files:")
        for frame in frames:
            print(f"  - {frame}")
        print("=" * 70)
        print("\nNow you can inspect each frame to verify:")
        print("1. Character consistency (face, clothing)")
        print("2. Environmental stability (tree remains visible)")
        print("3. Lighting progression (sunset→night)")
        print("4. Action completion (meditation→eyes open)")
    else:
        print(f"Video not found: {video_path}")


if __name__ == "__main__":
    main()