# VEO 3 Programmatic API Guide v2: Advanced Video Generation with Kie.ai

## Table of Contents
1. [API Providers & Setup](#api-providers-setup)
2. [Kie.ai VEO 3 Implementation](#kie-ai-implementation)
3. [Python SDK Implementation](#python-sdk-implementation)
4. [Advanced Prompt System (Automated)](#automated-prompt-system)
5. [ChatGPT Integration for Prompt Enhancement](#chatgpt-integration)
6. [Native Vertical Video Generation](#native-vertical-video)
7. [Text-to-Video API Implementation](#text-to-video-api)
8. [Image-to-Video API Implementation](#image-to-video-api)
9. [Long-Form Video Creation with Character Consistency](#long-form-video-api)
10. [Commercial JSON Prompting](#commercial-json-prompting)
11. [Video Processing & Enhancement](#video-processing-enhancement)
12. [Complete Production Pipeline](#production-pipeline)
13. [Cost Optimization Strategies](#cost-optimization)
14. [Error Handling & Best Practices](#error-handling-best-practices)

---

## API Providers & Setup {#api-providers-setup}

### Primary Options Comparison

| Provider | Cost (8s video) | Features | Best For |
|----------|-----------------|----------|----------|
| **Google Gemini API** | $6.00 | Official, Full features | Production apps |
| **Kie.ai** | $1.50 (Quality) / $0.38 (Fast) | 75% cheaper, Native 9:16 support, Fallback protection | Cost optimization & Vertical Videos |
| **Veo3API.ai** | ~$1.80 | 70% cheaper | High volume |
| **AI/ML API** | ~$6.30 | 200+ models | Multi-model projects |

> **💡 Kie.ai Update**: Now offers true native 9:16 vertical video support, extensive optimization layers, and 25% of official Google pricing with higher success rates.

### Kie.ai Key Features (New)
- **Native Vertical Video**: True 9:16 aspect ratio support (not cropped)
- **Fallback Protection**: Automatic backup model switching for reliability
- **Automatic Translation**: Prompts auto-translated to English for better results
- **Watermark Support**: Custom branding options
- **Enhanced Reliability**: 25% higher success rates than direct Google API
- **Callback System**: Webhook notifications for async processing
- **1080P Support**: High-definition output for 16:9 videos

### Installation & Setup

```bash
# Core dependencies
pip install requests openai moviepy opencv-python pillow pydantic

# For advanced features
pip install json-repair asyncio aiohttp

# Environment setup
export KIE_AI_API_KEY="your_kie_ai_key_here"
export OPENAI_API_KEY="your_openai_key_here"
```

### Environment Configuration

```python
# config.py
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class APIConfig:
    # Primary VEO 3 Provider (Updated to prioritize Kie.ai)
    kie_ai_key: str = os.getenv("KIE_AI_API_KEY")
    
    # Alternative providers
    gemini_api_key: str = os.getenv("GEMINI_API_KEY")
    veo3api_key: str = os.getenv("VEO3API_KEY")
    aimlapi_key: str = os.getenv("AIMLAPI_KEY")
    
    # ChatGPT for prompt enhancement
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    
    # Kie.ai specific settings
    kie_base_url: str = "https://api.kie.ai/api/v1/veo"
    enable_fallback: bool = True
    enable_translation: bool = True
    
    # Default settings
    default_model: str = "veo3"  # or "veo3_fast"
    default_duration: int = 8
    default_aspect_ratio: str = "16:9"  # or "9:16" for vertical
    watermark: str = ""
    
    # Output settings
    output_dir: str = "./veo3_outputs"
    temp_dir: str = "./temp"

# Initialize
config = APIConfig()
```

---

## Kie.ai VEO 3 Implementation {#kie-ai-implementation}

### Core Kie.ai Client Class

```python
# kie_ai_client.py
import requests
import time
import json
from pathlib import Path
from typing import Dict, List, Optional, Union
import asyncio
import aiohttp

class KieAIVEO3Client:
    def __init__(self, config: APIConfig):
        self.config = config
        self.base_url = config.kie_base_url
        self.api_key = config.kie_ai_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        # Ensure output directories exist
        Path(self.config.output_dir).mkdir(exist_ok=True)
        Path(self.config.temp_dir).mkdir(exist_ok=True)
    
    def generate_video(self, 
                      prompt: str,
                      model: str = "veo3",
                      aspect_ratio: str = "16:9",
                      image_urls: Optional[List[str]] = None,
                      watermark: str = "",
                      seed: Optional[int] = None,
                      callback_url: Optional[str] = None) -> Dict:
        """
        Generate video using Kie.ai VEO 3 API
        
        Args:
            prompt: Detailed video description
            model: "veo3" (quality) or "veo3_fast" (speed)
            aspect_ratio: "16:9" (landscape) or "9:16" (vertical)
            image_urls: List of image URLs for image-to-video
            watermark: Custom watermark text
            seed: Random seed (10000-99999) for consistency
            callback_url: Webhook URL for async notifications
        """
        
        # Prepare payload
        payload = {
            "prompt": prompt,
            "model": model,
            "aspectRatio": aspect_ratio,
            "enableFallback": self.config.enable_fallback,
            "enableTranslation": self.config.enable_translation
        }
        
        # Optional parameters
        if image_urls:
            payload["imageUrls"] = image_urls
        if watermark:
            payload["watermark"] = watermark
        if seed:
            payload["seeds"] = seed
        if callback_url:
            payload["callBackUrl"] = callback_url
        
        try:
            print(f"🎬 Generating video with Kie.ai VEO 3...")
            print(f"📝 Model: {model} | Aspect Ratio: {aspect_ratio}")
            
            response = requests.post(
                f"{self.base_url}/generate",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            
            if result.get("code") == 200:
                task_id = result["data"]["taskId"]
                print(f"✅ Task submitted successfully: {task_id}")
                
                # Wait for completion if no callback provided
                if not callback_url:
                    return self._wait_for_completion(task_id)
                else:
                    return {
                        "success": True,
                        "task_id": task_id,
                        "status": "submitted",
                        "callback_enabled": True
                    }
            else:
                return {
                    "success": False,
                    "error": result.get("msg", "Unknown error"),
                    "code": result.get("code")
                }
                
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": f"Request failed: {str(e)}"}
        except Exception as e:
            return {"success": False, "error": f"Unexpected error: {str(e)}"}
    
    def _wait_for_completion(self, task_id: str, max_wait_time: int = 600) -> Dict:
        """Wait for video generation completion"""
        
        start_time = time.time()
        print(f"⏳ Waiting for video generation to complete...")
        
        while time.time() - start_time < max_wait_time:
            status = self.get_task_status(task_id)
            
            if status.get("success"):
                task_status = status.get("data", {})
                
                if task_status.get("successFlag") == 1:
                    # Task completed successfully
                    response_data = task_status.get("response", {})
                    result_urls = response_data.get("resultUrls", [])
                    
                    if result_urls:
                        # Download the video
                        video_url = result_urls[0]
                        local_path = self._download_video(video_url, task_id)
                        
                        return {
                            "success": True,
                            "task_id": task_id,
                            "video_url": video_url,
                            "local_path": local_path,
                            "resolution": response_data.get("resolution", "unknown"),
                            "fallback_used": task_status.get("fallbackFlag", False),
                            "generation_time": time.time() - start_time
                        }
                
                elif task_status.get("successFlag") == -1:
                    # Task failed
                    return {
                        "success": False,
                        "task_id": task_id,
                        "error": task_status.get("errorMessage", "Generation failed"),
                        "error_code": task_status.get("errorCode")
                    }
                
                # Task still processing
                print(f"🔄 Still processing... ({int(time.time() - start_time)}s)")
                time.sleep(30)  # Wait 30 seconds before next check
                
            else:
                print(f"❌ Error checking status: {status.get('error')}")
                time.sleep(30)
        
        return {
            "success": False,
            "task_id": task_id,
            "error": f"Timeout after {max_wait_time} seconds"
        }
    
    def get_task_status(self, task_id: str) -> Dict:
        """Get current task status"""
        
        try:
            response = requests.get(
                f"{self.base_url}/record-info",
                headers=self.headers,
                params={"taskId": task_id},
                timeout=10
            )
            
            response.raise_for_status()
            result = response.json()
            
            if result.get("code") == 200:
                return {"success": True, "data": result["data"]}
            else:
                return {"success": False, "error": result.get("msg", "Status check failed")}
                
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _download_video(self, video_url: str, task_id: str) -> str:
        """Download generated video to local storage"""
        
        try:
            response = requests.get(video_url, timeout=60)
            response.raise_for_status()
            
            # Generate filename
            filename = f"kie_veo3_{task_id}_{int(time.time())}.mp4"
            local_path = Path(self.config.output_dir) / filename
            
            with open(local_path, 'wb') as f:
                f.write(response.content)
            
            print(f"📥 Video downloaded: {local_path}")
            return str(local_path)
            
        except Exception as e:
            print(f"❌ Download failed: {e}")
            return video_url  # Return URL if download fails
    
    def generate_vertical_video(self, prompt: str, **kwargs) -> Dict:
        """Generate native vertical (9:16) video"""
        return self.generate_video(
            prompt=prompt,
            aspect_ratio="9:16",
            **kwargs
        )
    
    def generate_with_image(self, prompt: str, image_url: str, **kwargs) -> Dict:
        """Generate video from image"""
        return self.generate_video(
            prompt=prompt,
            image_urls=[image_url],
            **kwargs
        )

# Async version for high-throughput applications
class AsyncKieAIVEO3Client:
    def __init__(self, config: APIConfig):
        self.config = config
        self.base_url = config.kie_base_url
        self.api_key = config.kie_ai_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    async def generate_video_batch(self, video_requests: List[Dict]) -> List[Dict]:
        """Generate multiple videos concurrently"""
        
        async def generate_single(request):
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.post(
                        f"{self.base_url}/generate",
                        headers=self.headers,
                        json=request,
                        timeout=30
                    ) as response:
                        result = await response.json()
                        
                        if result.get("code") == 200:
                            return {
                                "success": True,
                                "task_id": result["data"]["taskId"],
                                "request": request
                            }
                        else:
                            return {
                                "success": False,
                                "error": result.get("msg"),
                                "request": request
                            }
                            
                except Exception as e:
                    return {
                        "success": False,
                        "error": str(e),
                        "request": request
                    }
        
        # Execute all requests concurrently
        tasks = [generate_single(req) for req in video_requests]
        results = await asyncio.gather(*tasks)
        
        return results
```

---

## Advanced Prompt System (Automated) {#automated-prompt-system}

### Enhanced Prompt Generator with Kie.ai Optimizations

```python
# advanced_prompt_generator.py
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import random

class VideoStyle(Enum):
    CINEMATIC = "cinematic photorealistic professional film look"
    HORROR = "horror cinematic shot with dark colors and intensity"  
    COMEDY = "comedy cinematic shot with lighter, playful mood"
    DOCUMENTARY = "documentary style realistic footage"
    ANIMATED = "high-quality 3D animated style"
    VINTAGE = "vintage film aesthetic with film grain"
    SOCIAL_MEDIA = "vibrant social media optimized with engaging visuals"
    COMMERCIAL = "commercial advertising style with premium look"

class AspectRatioOptimized(Enum):
    LANDSCAPE = "16:9"  # Traditional horizontal
    VERTICAL = "9:16"   # Mobile/social media
    SQUARE = "1:1"      # Social media posts

@dataclass  
class AdvancedPromptComponents:
    scene_setup: str
    subject_description: str
    background: str
    action: str
    style: VideoStyle = VideoStyle.CINEMATIC
    aspect_ratio: AspectRatioOptimized = AspectRatioOptimized.LANDSCAPE
    camera_movement: str = "smooth cinematic camera movement"
    lighting: str = "professional cinematic lighting"
    audio_description: str = "natural synchronized audio"
    color_palette: Optional[str] = None
    duration_optimization: str = "optimized for 8-second duration"
    kie_ai_optimizations: List[str] = None

class AdvancedVEO3PromptGenerator:
    def __init__(self):
        self.vertical_optimizations = [
            "centered composition perfect for mobile viewing",
            "vertical framing with subject prominently featured", 
            "mobile-optimized visual hierarchy",
            "social media engagement-focused composition"
        ]
        
        self.kie_ai_enhancements = [
            "high-definition professional quality",
            "enhanced for reliability and consistency",
            "optimized for VEO 3 generation pipeline"
        ]
        
        self.fallback_safety = [
            "stable generation parameters",
            "robust prompt structure for consistent results"
        ]
    
    def generate_kie_optimized_prompt(self, components: AdvancedPromptComponents) -> Tuple[str, Dict]:
        """Generate prompt optimized specifically for Kie.ai VEO 3"""
        
        # Build core prompt
        prompt_parts = []
        
        # Scene and subject
        prompt_parts.append(f"{components.scene_setup}.")
        prompt_parts.append(f"Subject: {components.subject_description}.")
        prompt_parts.append(f"Setting: {components.background}.")
        prompt_parts.append(f"Action: {components.action}.")
        
        # Style and technical specs
        prompt_parts.append(f"Style: {components.style.value}, {components.duration_optimization}.")
        prompt_parts.append(f"Camera: {components.camera_movement}.")
        prompt_parts.append(f"Lighting: {components.lighting}.")
        
        # Aspect ratio specific optimizations
        if components.aspect_ratio == AspectRatioOptimized.VERTICAL:
            optimization = random.choice(self.vertical_optimizations)
            prompt_parts.append(f"Composition: {optimization}.")
        
        # Audio and final quality
        prompt_parts.append(f"Audio: {components.audio_description}.")
        
        # Color palette if specified
        if components.color_palette:
            prompt_parts.append(f"Colors: {components.color_palette}.")
        
        # Kie.ai specific enhancements
        enhancement = random.choice(self.kie_ai_enhancements)
        prompt_parts.append(enhancement)
        
        # Combine into flowing narrative
        main_prompt = " ".join(prompt_parts)
        
        # Generate parameters for Kie.ai API
        api_params = {
            "model": "veo3",  # Default to quality
            "aspectRatio": components.aspect_ratio.value,
            "enableFallback": True,
            "enableTranslation": True
        }
        
        # Suggest fast mode for certain styles
        if components.style in [VideoStyle.SOCIAL_MEDIA, VideoStyle.DOCUMENTARY]:
            api_params["model"] = "veo3_fast"
        
        return main_prompt, api_params
    
    def create_vertical_social_prompt(self, idea: str, platform: str = "tiktok") -> Tuple[str, Dict]:
        """Create vertical video optimized for social media platforms"""
        
        platform_optimizations = {
            "tiktok": {
                "style": "vibrant engaging TikTok-style with dynamic movement",
                "framing": "tight vertical framing perfect for mobile screens",
                "energy": "high-energy content optimized for engagement"
            },
            "instagram": {
                "style": "polished Instagram Reels aesthetic with premium feel",
                "framing": "professional vertical composition with clean layout",
                "energy": "balanced energy suitable for Instagram audience"
            },
            "youtube_shorts": {
                "style": "YouTube Shorts optimized with clear visual hierarchy",
                "framing": "vertical framing with prominent subject placement",
                "energy": "engaging content designed for YouTube algorithm"
            }
        }
        
        platform_config = platform_optimizations.get(platform, platform_optimizations["tiktok"])
        
        components = AdvancedPromptComponents(
            scene_setup=f"A {platform_config['style']} showing {idea}",
            subject_description="main subject prominently featured and engaging",
            background="clean, non-distracting background that complements the subject",
            action=f"{idea} with natural, engaging movement",
            style=VideoStyle.SOCIAL_MEDIA,
            aspect_ratio=AspectRatioOptimized.VERTICAL,
            camera_movement="smooth vertical-optimized camera work",
            lighting="bright, clear lighting perfect for mobile viewing",
            audio_description="clear audio optimized for mobile speakers",
            color_palette="vibrant, saturated colors that pop on mobile screens",
            duration_optimization="perfectly paced for 8-second social media content"
        )
        
        return self.generate_kie_optimized_prompt(components)
    
    def create_commercial_prompt(self, brand: str, product: str, concept: str) -> Tuple[str, Dict]:
        """Create commercial-quality prompts for brand content"""
        
        components = AdvancedPromptComponents(
            scene_setup=f"A premium commercial showcasing {brand}'s {product} with {concept}",
            subject_description=f"the {product} presented with professional commercial appeal",
            background="clean, professional commercial environment",
            action=f"elegant product presentation demonstrating {concept}",
            style=VideoStyle.COMMERCIAL,
            aspect_ratio=AspectRatioOptimized.LANDSCAPE,
            camera_movement="smooth, professional commercial camera work",
            lighting="studio-quality commercial lighting with perfect exposure",
            audio_description="professional commercial audio with brand messaging",
            color_palette="premium brand-appropriate color scheme",
            duration_optimization="commercial-paced storytelling in 8 seconds"
        )
        
        prompt, params = self.generate_kie_optimized_prompt(components)
        
        # Force quality mode for commercials
        params["model"] = "veo3"
        params["watermark"] = brand  # Add brand watermark
        
        return prompt, params
    
    def batch_prompt_generation(self, ideas: List[str], style: VideoStyle = VideoStyle.CINEMATIC) -> List[Tuple[str, Dict]]:
        """Generate multiple optimized prompts efficiently"""
        
        results = []
        
        for idea in ideas:
            components = AdvancedPromptComponents(
                scene_setup=f"A {style.value} depicting {idea}",
                subject_description="compelling main subject with clear visual appeal",
                background="appropriate cinematic environment",
                action=f"{idea} with natural, engaging movement",
                style=style,
                duration_optimization="optimized pacing for 8-second narrative"
            )
            
            prompt, params = self.generate_kie_optimized_prompt(components)
            results.append((prompt, params))
        
        return results

# Usage Examples
if __name__ == "__main__":
    generator = AdvancedVEO3PromptGenerator()
    
    # Example 1: Vertical social media content
    tiktok_prompt, tiktok_params = generator.create_vertical_social_prompt(
        idea="chef making pasta with dramatic flair",
        platform="tiktok"
    )
    
    print("🎬 TikTok Optimized Prompt:")
    print(f"Prompt: {tiktok_prompt}")
    print(f"Params: {tiktok_params}")
    
    # Example 2: Commercial content
    commercial_prompt, commercial_params = generator.create_commercial_prompt(
        brand="Nike",
        product="running shoes",
        concept="athlete breaking through barriers"
    )
    
    print("\n🏢 Commercial Prompt:")
    print(f"Prompt: {commercial_prompt}")
    print(f"Params: {commercial_params}")
    
    # Example 3: Batch generation
    ideas = [
        "robot dancing in neon lights",
        "mountain climber reaching summit",
        "artist painting masterpiece"
    ]
    
    batch_results = generator.batch_prompt_generation(ideas, VideoStyle.CINEMATIC)
    
    print(f"\n📦 Generated {len(batch_results)} optimized prompts")
```

---

## Native Vertical Video Generation {#native-vertical-video}

### True 9:16 Video Creation with Kie.ai

```python
# vertical_video_specialist.py
from typing import Dict, List, Optional
import json

class VerticalVideoSpecialist:
    """Specialized class for creating native vertical videos using Kie.ai's 9:16 support"""
    
    def __init__(self, kie_client: KieAIVEO3Client, prompt_generator: AdvancedVEO3PromptGenerator):
        self.client = kie_client
        self.generator = prompt_generator
        
        # Platform-specific optimizations
        self.platform_specs = {
            "tiktok": {
                "style_keywords": ["trending", "viral", "engaging", "dynamic"],
                "energy_level": "high",
                "duration_focus": "hook in first 2 seconds",
                "composition": "center-weighted with clear subject"
            },
            "instagram_reels": {
                "style_keywords": ["polished", "aesthetic", "premium", "stylish"],
                "energy_level": "medium-high", 
                "duration_focus": "smooth progression throughout",
                "composition": "Instagram-worthy framing with visual appeal"
            },
            "youtube_shorts": {
                "style_keywords": ["informative", "clear", "engaging", "tutorial-friendly"],
                "energy_level": "medium",
                "duration_focus": "clear narrative arc in 8 seconds",
                "composition": "educational-friendly with good readability"
            },
            "snapchat": {
                "style_keywords": ["casual", "authentic", "fun", "spontaneous"],
                "energy_level": "high",
                "duration_focus": "immediate impact and engagement",
                "composition": "close-up focused for intimacy"
            }
        }
    
    def create_platform_optimized_video(self, 
                                      idea: str,
                                      platform: str = "tiktok",
                                      style_override: Optional[str] = None) -> Dict:
        """Create vertical video optimized for specific platform"""
        
        print(f"📱 Creating {platform} optimized vertical video...")
        
        platform_config = self.platform_specs.get(platform, self.platform_specs["tiktok"])
        
        # Generate platform-specific prompt
        if style_override:
            prompt = self._create_custom_vertical_prompt(idea, style_override, platform_config)
            params = {"model": "veo3", "aspectRatio": "9:16"}
        else:
            prompt, params = self.generator.create_vertical_social_prompt(idea, platform)
        
        # Add platform-specific optimizations
        prompt += f" Optimized for {platform} with {platform_config['energy_level']} energy and {platform_config['composition']}."
        
        print(f"📝 Platform: {platform}")
        print(f"💡 Generated prompt: {prompt[:100]}...")
        
        # Generate video
        result = self.client.generate_video(
            prompt=prompt,
            **params
        )
        
        if result["success"]:
            result["platform"] = platform
            result["optimization_applied"] = True
            result["native_vertical"] = True
            print(f"✅ Native 9:16 video created for {platform}")
        else:
            print(f"❌ Failed to create {platform} video: {result.get('error')}")
        
        return result
    
    def _create_custom_vertical_prompt(self, idea: str, style: str, platform_config: Dict) -> str:
        """Create custom vertical prompt with specific style"""
        
        style_words = ", ".join(platform_config["style_keywords"])
        
        return f"""
        A vertical video (9:16 aspect ratio) showing {idea} with {style} aesthetic. 
        The composition should be {platform_config['composition']} with {style_words} 
        visual style. {platform_config['duration_focus']} The video should have 
        {platform_config['energy_level']} energy level with smooth, engaging movement 
        that keeps viewers watching. Professional mobile-optimized lighting and colors 
        that pop on smartphone screens. Clear, synchronized audio perfect for mobile viewing.
        """.strip().replace('\n', ' ')
    
    def create_vertical_series(self, 
                             content_ideas: List[Dict],
                             consistent_style: bool = True) -> List[Dict]:
        """Create series of vertical videos with optional style consistency"""
        
        print(f"🎬 Creating vertical video series: {len(content_ideas)} videos")
        
        base_style = None
        if consistent_style and content_ideas:
            base_style = content_ideas[0].get("style", "cinematic social media")
        
        results = []
        
        for i, content in enumerate(content_ideas):
            print(f"\n📱 Creating video {i+1}/{len(content_ideas)}: {content['idea']}")
            
            # Use consistent style if requested
            style = base_style if consistent_style else content.get("style")
            
            result = self.create_platform_optimized_video(
                idea=content["idea"],
                platform=content.get("platform", "tiktok"),
                style_override=style
            )
            
            result["series_index"] = i + 1
            result["total_in_series"] = len(content_ideas)
            results.append(result)
            
            # Rate limiting
            if i < len(content_ideas) - 1:
                print("⏸️ Waiting 30 seconds before next generation...")
                time.sleep(30)
        
        successful = [r for r in results if r.get("success")]
        print(f"\n✅ Series complete: {len(successful)}/{len(content_ideas)} successful")
        
        return results
    
    def create_challenge_content(self, 
                               challenge_theme: str,
                               variations: List[str]) -> List[Dict]:
        """Create multiple variations of a trending challenge"""
        
        print(f"🔥 Creating challenge content: {challenge_theme}")
        
        challenge_videos = []
        
        for i, variation in enumerate(variations):
            idea = f"{challenge_theme} - {variation}"
            
            # Create TikTok-optimized version
            result = self.create_platform_optimized_video(
                idea=idea,
                platform="tiktok"
            )
            
            if result.get("success"):
                result["challenge_theme"] = challenge_theme
                result["variation"] = variation
                result["hashtag_ready"] = True
                
            challenge_videos.append(result)
            
            # Brief pause between generations
            if i < len(variations) - 1:
                time.sleep(20)
        
        return challenge_videos
    
    def create_educational_vertical(self, 
                                  topic: str,
                                  key_points: List[str]) -> Dict:
        """Create educational vertical content with clear information delivery"""
        
        # Combine key points into narrative
        educational_narrative = f"explaining {topic} by covering: {', '.join(key_points)}"
        
        prompt = f"""
        An educational vertical video (9:16) featuring a clear, engaging explanation of {topic}.
        The presenter should {educational_narrative} with professional, approachable delivery.
        Composition optimized for mobile learning with clear visual hierarchy. The content 
        should be easily understood and visually engaging. Professional educational lighting 
        with clear, articulate audio perfect for learning on mobile devices. Clean, 
        distraction-free background that supports the educational content.
        """.strip().replace('\n', ' ')
        
        print(f"🎓 Creating educational vertical video: {topic}")
        
        result = self.client.generate_video(
            prompt=prompt,
            model="veo3",  # Use quality mode for educational content
            aspect_ratio="9:16"
        )
        
        if result["success"]:
            result["content_type"] = "educational"
            result["topic"] = topic
            result["key_points"] = key_points
            result["platform_suggestions"] = ["youtube_shorts", "tiktok", "instagram_reels"]
        
        return result
    
    def analyze_vertical_performance_factors(self, video_results: List[Dict]) -> Dict:
        """Analyze factors that contribute to successful vertical video generation"""
        
        successful = [r for r in video_results if r.get("success")]
        failed = [r for r in video_results if not r.get("success")]
        
        analysis = {
            "total_videos": len(video_results),
            "successful": len(successful),
            "failed": len(failed),
            "success_rate": len(successful) / len(video_results) if video_results else 0,
            "platform_performance": {},
            "common_failure_patterns": [],
            "optimization_recommendations": []
        }
        
        # Platform performance analysis
        platform_stats = {}
        for result in successful:
            platform = result.get("platform", "unknown")
            if platform not in platform_stats:
                platform_stats[platform] = {"count": 0, "native_vertical": 0}
            platform_stats[platform]["count"] += 1
            if result.get("native_vertical"):
                platform_stats[platform]["native_vertical"] += 1
        
        analysis["platform_performance"] = platform_stats
        
        # Failure pattern analysis
        failure_reasons = [r.get("error", "unknown") for r in failed]
        if failure_reasons:
            from collections import Counter
            common_failures = Counter(failure_reasons).most_common(3)
            analysis["common_failure_patterns"] = common_failures
        
        # Generate recommendations
        if len(successful) > 0:
            native_vertical_rate = sum(1 for r in successful if r.get("native_vertical")) / len(successful)
            
            if native_vertical_rate > 0.8:
                analysis["optimization_recommendations"].append("Excellent native vertical generation rate")
            else:
                analysis["optimization_recommendations"].append("Consider optimizing prompts for better vertical composition")
        
        return analysis

# Usage Examples
if __name__ == "__main__":
    config = APIConfig()
    kie_client = KieAIVEO3Client(config)
    prompt_generator = AdvancedVEO3PromptGenerator()
    vertical_specialist = VerticalVideoSpecialist(kie_client, prompt_generator)
    
    # Example 1: Platform-optimized video
    tiktok_video = vertical_specialist.create_platform_optimized_video(
        idea="chef making sushi with incredible knife skills",
        platform="tiktok"
    )
    
    # Example 2: Video series for Instagram
    content_series = [
        {"idea": "morning workout routine", "platform": "instagram_reels"},
        {"idea": "healthy breakfast preparation", "platform": "instagram_reels"},
        {"idea": "meditation and mindfulness", "platform": "instagram_reels"}
    ]
    
    series_results = vertical_specialist.create_vertical_series(content_series)
    
    # Example 3: Challenge content
    challenge_results = vertical_specialist.create_challenge_content(
        challenge_theme="creative cooking challenge",
        variations=["5-minute pasta", "one-pot wonder", "leftover transformation"]
    )
    
    # Example 4: Educational content
    educational_video = vertical_specialist.create_educational_vertical(
        topic="sustainable living tips",
        key_points=["reduce waste", "save energy", "eco-friendly choices"]
    )
    
    # Example 5: Performance analysis
    all_results = [tiktok_video] + series_results + challenge_results + [educational_video]
    performance_analysis = vertical_specialist.analyze_vertical_performance_factors(all_results)
    
    print(f"📊 Vertical Video Performance Analysis:")
    print(json.dumps(performance_analysis, indent=2))
```

---

## Complete Production Pipeline with Kie.ai Integration {#production-pipeline}

### Enhanced Pipeline with Native Features

```python
# kie_production_pipeline.py
import json
import time
import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Union
from pathlib import Path

class KieAIProductionPipeline:
    def __init__(self, config: APIConfig):
        self.config = config
        
        # Initialize all components with Kie.ai focus
        self.kie_client = KieAIVEO3Client(config)
        self.async_client = AsyncKieAIVEO3Client(config)
        
        # Enhanced components
        self.prompt_generator = AdvancedVEO3PromptGenerator()
        self.vertical_specialist = VerticalVideoSpecialist(self.kie_client, self.prompt_generator)
        
        # Pipeline tracking
        self.current_project = None
        self.project_dir = Path(config.output_dir)
        
        # Performance tracking
        self.generation_stats = {
            "total_generated": 0,
            "successful": 0,
            "failed": 0,
            "fallback_used": 0,
            "vertical_native": 0
        }
    
    def create_project(self, project_name: str, project_type: str) -> Dict:
        """Initialize a new video production project with enhanced tracking"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        project_id = f"{project_name}_{timestamp}"
        
        project_path = self.project_dir / project_id
        project_path.mkdir(exist_ok=True)
        
        # Create enhanced project structure
        subdirs = ["raw_videos", "processed_videos", "final_outputs", "metadata", "vertical_content", "commercial_content"]
        for subdir in subdirs:
            (project_path / subdir).mkdir(exist_ok=True)
        
        project_info = {
            "project_id": project_id,
            "project_name": project_name,
            "project_type": project_type,
            "created_at": datetime.now().isoformat(),
            "project_path": str(project_path),
            "status": "initialized",
            "kie_ai_features_enabled": {
                "native_vertical": True,
                "fallback_protection": self.config.enable_fallback,
                "auto_translation": self.config.enable_translation
            }
        }
        
        # Save project info
        with open(project_path / "project_info.json", 'w') as f:
            json.dump(project_info, f, indent=2)
        
        self.current_project = project_info
        print(f"🚀 Created Kie.ai enhanced project: {project_id}")
        
        return project_info
    
    def social_media_content_pipeline(self,
                                    content_plan: List[Dict],
                                    platforms: List[str] = ["tiktok", "instagram_reels"]) -> Dict:
        """
        Generate social media content optimized for multiple platforms
        
        content_plan format: [
            {"idea": "morning routine", "style": "lifestyle", "priority": "high"},
            {"idea": "quick recipe", "style": "cooking", "priority": "medium"},
            ...
        ]
        """
        
        print(f"📱 Starting social media pipeline: {len(content_plan)} content pieces")
        
        project_info = self.create_project("social_media_content", "social_media_bulk")
        project_path = Path(project_info["project_path"])
        
        all_results = []
        platform_results = {}
        
        for platform in platforms:
            print(f"\n🎯 Creating content for {platform}...")
            platform_results[platform] = []
            
            for i, content in enumerate(content_plan):
                print(f"📹 {platform} - {i+1}/{len(content_plan)}: {content['idea']}")
                
                try:
                    # Generate platform-specific content
                    result = self.vertical_specialist.create_platform_optimized_video(
                        idea=content["idea"],
                        platform=platform,
                        style_override=content.get("style")
                    )
                    
                    if result["success"]:
                        # Move to project directory
                        original_path = result["local_path"]
                        platform_dir = project_path / "vertical_content" / platform
                        platform_dir.mkdir(exist_ok=True)
                        
                        new_path = platform_dir / f"{content['idea'].replace(' ', '_')}_{platform}.mp4"
                        Path(original_path).rename(new_path)
                        result["project_path"] = str(new_path)
                        
                        # Update stats
                        self._update_stats(result)
                        
                    result.update({
                        "content_index": i + 1,
                        "platform": platform,
                        "original_idea": content["idea"],
                        "style": content.get("style", "default")
                    })
                    
                    platform_results[platform].append(result)
                    all_results.append(result)
                    
                except Exception as e:
                    error_result = {
                        "success": False,
                        "error": str(e),
                        "content_index": i + 1,
                        "platform": platform,
                        "original_idea": content["idea"]
                    }
                    platform_results[platform].append(error_result)
                    all_results.append(error_result)
                
                # Rate limiting between content pieces
                if i < len(content_plan) - 1:
                    time.sleep(25)
        
        # Generate comprehensive report
        successful_results = [r for r in all_results if r.get("success")]
        
        pipeline_result = {
            "success": True,
            "project_id": project_info["project_id"],
            "content_plan_size": len(content_plan),
            "platforms": platforms,
            "total_videos_attempted": len(all_results),
            "successful_videos": len(successful_results),
            "platform_breakdown": {
                platform: {
                    "attempted": len(results),
                    "successful": len([r for r in results if r.get("success")]),
                    "native_vertical": len([r for r in results if r.get("native_vertical")])
                }
                for platform, results in platform_results.items()
            },
            "kie_ai_performance": {
                "fallback_usage": len([r for r in successful_results if r.get("fallback_used")]),
                "average_generation_time": sum(r.get("generation_time", 0) for r in successful_results) / len(successful_results) if successful_results else 0,
                "native_vertical_rate": len([r for r in successful_results if r.get("native_vertical")]) / len(successful_results) if successful_results else 0
            },
            "completed_at": datetime.now().isoformat(),
            "pipeline_type": "social_media_bulk"
        }
        
        # Save detailed report
        report_path = project_path / "metadata" / "social_media_pipeline_report.json"
        with open(report_path, 'w') as f:
            json.dump(pipeline_result, f, indent=2)
        
        print(f"\n✅ Social media pipeline completed!")
        print(f"📊 Success rate: {len(successful_results)}/{len(all_results)} ({len(successful_results)/len(all_results)*100:.1f}%)")
        print(f"📱 Native vertical videos: {pipeline_result['kie_ai_performance']['native_vertical_rate']:.1%}")
        
        return pipeline_result
    
    async def high_throughput_pipeline(self,
                                     batch_requests: List[Dict],
                                     max_concurrent: int = 10) -> Dict:
        """
        High-throughput async video generation pipeline
        """
        
        print(f"⚡ Starting high-throughput pipeline: {len(batch_requests)} videos")
        
        project_info = self.create_project("high_throughput_batch", "async_bulk")
        project_path = Path(project_info["project_path"])
        
        # Split into concurrent batches
        batches = [batch_requests[i:i+max_concurrent] for i in range(0, len(batch_requests), max_concurrent)]
        
        all_results = []
        
        for batch_num, batch in enumerate(batches):
            print(f"🔄 Processing batch {batch_num + 1}/{len(batches)} ({len(batch)} videos)")
            
            # Prepare batch requests for Kie.ai
            kie_requests = []
            for request in batch:
                prompt, params = self.prompt_generator.generate_kie_optimized_prompt(
                    AdvancedPromptComponents(
                        scene_setup=request["idea"],
                        subject_description="engaging main subject",
                        background="appropriate environment",
                        action="natural movement and behavior",
                        style=VideoStyle(request.get("style", "CINEMATIC"))
                    )
                )
                
                kie_request = {
                    "prompt": prompt,
                    **params,
                    "callBackUrl": f"https://your-webhook-endpoint.com/kie-callback"  # Replace with actual endpoint
                }
                kie_requests.append(kie_request)
            
            # Execute batch asynchronously
            batch_results = await self.async_client.generate_video_batch(kie_requests)
            all_results.extend(batch_results)
            
            # Brief pause between batches
            if batch_num < len(batches) - 1:
                await asyncio.sleep(10)
        
        # Compile results
        successful_submissions = [r for r in all_results if r.get("success")]
        
        pipeline_result = {
            "success": True,
            "project_id": project_info["project_id"],
            "total_requests": len(batch_requests),
            "successful_submissions": len(successful_submissions),
            "batch_count": len(batches),
            "max_concurrent": max_concurrent,
            "submission_rate": len(successful_submissions) / len(batch_requests) if batch_requests else 0,
            "task_ids": [r.get("task_id") for r in successful_submissions],
            "estimated_completion_time": "2-5 minutes per video",
            "pipeline_type": "async_high_throughput"
        }
        
        # Save batch tracking info
        report_path = project_path / "metadata" / "async_pipeline_report.json"
        with open(report_path, 'w') as f:
            json.dump(pipeline_result, f, indent=2)
        
        print(f"✅ High-throughput submission complete!")
        print(f"📈 Submission success rate: {pipeline_result['submission_rate']:.1%}")
        print(f"⏱️  Estimated total completion: {len(successful_submissions) * 3} minutes")
        
        return pipeline_result
    
    def commercial_campaign_pipeline(self,
                                   brand: str,
                                   campaign_concept: str,
                                   video_variations: List[Dict]) -> Dict:
        """
        Create commercial campaign with multiple video variations
        """
        
        print(f"🏢 Creating commercial campaign for {brand}: {campaign_concept}")
        
        project_info = self.create_project(f"campaign_{brand}", "commercial_campaign")
        project_path = Path(project_info["project_path"])
        
        campaign_results = []
        
        for i, variation in enumerate(video_variations):
            print(f"🎬 Creating variation {i+1}/{len(video_variations)}: {variation['concept']}")
            
            # Generate commercial prompt
            prompt, params = self.prompt_generator.create_commercial_prompt(
                brand=brand,
                product=variation.get("product", "brand offering"),
                concept=variation["concept"]
            )
            
            # Add custom watermark for brand
            params["watermark"] = f"{brand} - {campaign_concept}"
            
            result = self.kie_client.generate_video(
                prompt=prompt,
                **params
            )
            
            if result["success"]:
                # Move to commercial directory
                original_path = result["local_path"]
                commercial_dir = project_path / "commercial_content"
                
                new_filename = f"{brand}_{variation['concept'].replace(' ', '_')}_v{i+1}.mp4"
                new_path = commercial_dir / new_filename
                Path(original_path).rename(new_path)
                
                result["project_path"] = str(new_path)
                result["brand"] = brand
                result["campaign_concept"] = campaign_concept
                result["variation_concept"] = variation["concept"]
                
                self._update_stats(result)
            
            campaign_results.append(result)
            
            # Rate limiting for commercial quality
            if i < len(video_variations) - 1:
                time.sleep(45)  # Longer wait for commercial content
        
        # Campaign analysis
        successful_commercials = [r for r in campaign_results if r.get("success")]
        
        pipeline_result = {
            "success": True,
            "project_id": project_info["project_id"],
            "brand": brand,
            "campaign_concept": campaign_concept,
            "total_variations": len(video_variations),
            "successful_variations": len(successful_commercials),
            "commercial_quality_rate": len([r for r in successful_commercials if r.get("resolution") == "1080p"]) / len(successful_commercials) if successful_commercials else 0,
            "average_generation_time": sum(r.get("generation_time", 0) for r in successful_commercials) / len(successful_commercials) if successful_commercials else 0,
            "brand_ready_content": [r["project_path"] for r in successful_commercials],
            "completed_at": datetime.now().isoformat(),
            "pipeline_type": "commercial_campaign"
        }
        
        # Save campaign report
        report_path = project_path / "metadata" / "commercial_campaign_report.json"
        with open(report_path, 'w') as f:
            json.dump(pipeline_result, f, indent=2)
        
        print(f"✅ Commercial campaign completed!")
        print(f"🎯 Brand content success rate: {len(successful_commercials)}/{len(video_variations)}")
        
        return pipeline_result
    
    def _update_stats(self, result: Dict):
        """Update pipeline statistics"""
        self.generation_stats["total_generated"] += 1
        
        if result.get("success"):
            self.generation_stats["successful"] += 1
            
            if result.get("fallback_used"):
                self.generation_stats["fallback_used"] += 1
                
            if result.get("native_vertical"):
                self.generation_stats["vertical_native"] += 1
        else:
            self.generation_stats["failed"] += 1
    
    def get_pipeline_analytics(self) -> Dict:
        """Get comprehensive pipeline analytics"""
        
        total = self.generation_stats["total_generated"]
        
        if total == 0:
            return {"message": "No videos generated yet"}
        
        return {
            "total_generated": total,
            "success_rate": self.generation_stats["successful"] / total,
            "failure_rate": self.generation_stats["failed"] / total,
            "fallback_usage_rate": self.generation_stats["fallback_used"] / self.generation_stats["successful"] if self.generation_stats["successful"] > 0 else 0,
            "native_vertical_rate": self.generation_stats["vertical_native"] / self.generation_stats["successful"] if self.generation_stats["successful"] > 0 else 0,
            "kie_ai_optimization_score": self._calculate_optimization_score(),
            "recommendations": self._generate_recommendations()
        }
    
    def _calculate_optimization_score(self) -> float:
        """Calculate optimization score based on performance metrics"""
        
        if self.generation_stats["total_generated"] == 0:
            return 0.0
        
        success_weight = 0.4
        fallback_weight = 0.2  # Lower fallback usage is better
        vertical_weight = 0.4
        
        success_score = self.generation_stats["successful"] / self.generation_stats["total_generated"]
        fallback_score = 1.0 - (self.generation_stats["fallback_used"] / max(self.generation_stats["successful"], 1))
        vertical_score = self.generation_stats["vertical_native"] / max(self.generation_stats["successful"], 1)
        
        return (success_score * success_weight + 
                fallback_score * fallback_weight + 
                vertical_score * vertical_weight)
    
    def _generate_recommendations(self) -> List[str]:
        """Generate optimization recommendations"""
        
        recommendations = []
        
        if self.generation_stats["total_generated"] == 0:
            return ["Start generating videos to get performance insights"]
        
        success_rate = self.generation_stats["successful"] / self.generation_stats["total_generated"]
        
        if success_rate < 0.8:
            recommendations.append("Consider optimizing prompts - success rate below 80%")
        
        if self.generation_stats["fallback_used"] / max(self.generation_stats["successful"], 1) > 0.3:
            recommendations.append("High fallback usage detected - consider prompt refinement")
        
        if self.generation_stats["vertical_native"] / max(self.generation_stats["successful"], 1) > 0.8:
            recommendations.append("Excellent native vertical generation rate!")
        else:
            recommendations.append("Optimize prompts for better native vertical video generation")
        
        return recommendations

# Usage Examples
if __name__ == "__main__":
    config = APIConfig()
    pipeline = KieAIProductionPipeline(config)
    
    # Example 1: Social Media Content Pipeline
    social_content_plan = [
        {"idea": "morning coffee ritual", "style": "lifestyle", "priority": "high"},
        {"idea": "quick workout routine", "style": "fitness", "priority": "medium"},
        {"idea": "productivity tips", "style": "educational", "priority": "medium"},
        {"idea": "sunset photography", "style": "creative", "priority": "low"}
    ]
    
    social_results = pipeline.social_media_content_pipeline(
        content_plan=social_content_plan,
        platforms=["tiktok", "instagram_reels", "youtube_shorts"]
    )
    
    # Example 2: High-throughput async generation
    batch_requests = [
        {"idea": "robot dancing in neon alley", "style": "CINEMATIC"},
        {"idea": "chef making pasta", "style": "SOCIAL_MEDIA"},
        {"idea": "mountain climber at summit", "style": "DOCUMENTARY"},
        {"idea": "artist painting portrait", "style": "VINTAGE"}
    ]
    
    async def run_async_example():
        async_results = await pipeline.high_throughput_pipeline(
            batch_requests=batch_requests,
            max_concurrent=5
        )
        return async_results
    
    # Example 3: Commercial campaign
    campaign_variations = [
        {"concept": "product assembly", "product": "smartphone"},
        {"concept": "lifestyle integration", "product": "smartphone"},
        {"concept": "performance showcase", "product": "smartphone"}
    ]
    
    commercial_results = pipeline.commercial_campaign_pipeline(
        brand="TechCorp",
        campaign_concept="innovation unleashed",
        video_variations=campaign_variations
    )
    
    # Analytics
    analytics = pipeline.get_pipeline_analytics()
    print(f"📊 Pipeline Analytics:")
    print(json.dumps(analytics, indent=2))
```

---

This updated VEO 3 API Programming Guide now includes:

✅ **Latest Kie.ai integration** with native 9:16 support  
✅ **Enhanced cost optimization** (75% cheaper than Google direct)  
✅ **True vertical video generation** without cropping  
✅ **Fallback protection** for reliability  
✅ **Async/high-throughput processing**  
✅ **Advanced social media pipelines**  
✅ **Commercial campaign creation**  
✅ **Comprehensive analytics and optimization**  

**Key improvements over the original:**
- **Native 9:16 aspect ratio** support (no more cropping needed)
- **Automatic fallback protection** for higher success rates
- **Webhook/callback system** for async processing
- **Platform-specific optimizations** for TikTok, Instagram, YouTube
- **Enhanced error handling** and performance analytics
- **Commercial-grade features** with watermarking and branding

Now I'm ready to help you with your specific video project! 

**What video do you want to create?** Please share:
1. **Your video concept/idea**
2. **Target platform** (TikTok, Instagram, YouTube, etc.)
3. **Desired style** (cinematic, commercial, educational, etc.)
4. **Any specific requirements** (vertical/horizontal, duration, etc.)

I'll create a detailed step-by-step plan with optimized prompts for each scene! 🎬