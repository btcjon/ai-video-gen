# Frame-to-Frame Video Generation Workflow
## Creative Process for Sequential AI Video Production

This workflow enables seamless multi-scene video narratives by using each scene's ending frame to guide the next scene's generation, ensuring perfect visual continuity.

---

## 🚨 CRITICAL RULES (Read This First)

### The 5 Non-Negotiable Rules for Frame-to-Frame Success

#### 1. **FACE MUST BE VISIBLE IN ENDING FRAME**
**Why**: VEO 3 cannot maintain character consistency if the face isn't visible in the reference image.
- ❌ WRONG: Character walking away, back to camera, face obscured
- ✅ RIGHT: Character in 3/4 profile or facing camera at scene end
- **Rule**: Always end scenes with face visible at chest level or closer

#### 2. **ONE ACTION PER 8-SECOND SCENE**
**Why**: Cramming multiple actions results in incomplete execution.
- ❌ WRONG: "Walk to camp + arrive + interact + demonstrate" (4 actions)
- ✅ RIGHT: "Walk to camp and arrive" (1 action) → Next scene: "Interact and demonstrate" (1 action)
- **Rule**: Max 4 distinct 2-second steps per scene, all serving ONE primary action

#### 3. **MAINTAIN CONTINUITY BETWEEN SCENES**
**Why**: Skipping logical steps breaks visual flow.
- ❌ WRONG: Scene N ends sitting → Scene N+1 starts standing at different location
- ✅ RIGHT: Scene N ends sitting → Scene N+1 starts sitting, then stands
- **Rule**: Ending state of Scene N = Starting state of Scene N+1

#### 4. **USE JSON FOR COMPLEX SCENES**
**Why**: Plain text lacks structure and completeness checks (from veo3_prompt_analysis.md).
- **Use JSON for**: Multiple characters, camera movements, precise lighting, interactions
- **Plain text OK for**: Simple single-character continuity scenes
- **Rule**: When in doubt about completeness, use JSON structure

#### 5. **PLAN TRANSITIONS, DON'T SKIP THEM**
**Why**: Major location/time changes need transition scenes.
- ❌ WRONG: Forest → teleport to camp
- ✅ RIGHT: Forest → see lights → walk toward lights → arrive at camp (2-3 scenes)
- **Rule**: If ending and beginning don't match, add a transition scene

#### 6. **ESTABLISH ENVIRONMENTAL AESTHETICS AT TRANSITION POINT**
**Why**: Major style changes (day→night, location shifts) need clear visual direction set in the transition scene's ending frame.
- ❌ WRONG: Scene 3 (sunset) ends vague → Scene 4 (night) generates poor/inconsistent night look
- ✅ RIGHT: Scene 3 ending explicitly describes: "ending with deep blue twilight, first stars visible, silver moonlight beginning to illuminate scene, cool color temperature establishing night aesthetic"
- **Examples of what to specify**:
  - **Night scenes**: "Deep blue-black sky, silver moonlight as key light, cool color temperature, stars visible, atmospheric haze"
  - **Dawn scenes**: "Warm golden orange horizon, soft pink sky, warm color temperature, volumetric morning mist"
  - **Indoor→Outdoor**: "Natural daylight flooding in, warm vs cool contrast, specific weather conditions"
- **Rule**: The scene where transition HAPPENS must end with complete aesthetic description of the new environment

#### 7. **PRODUCT VISIBILITY THROUGHOUT SCENE CHAIN** ⚠️ CRITICAL FOR PRODUCT VIDEOS
**Why**: Once a product disappears from frame, it's extremely difficult to reintroduce it with brand consistency.

**The Product Continuity Problem**:
- VEO 3 cannot accurately recreate branded products (logos, labels, specific designs)
- If product exits frame → Next scene will hallucinate incorrect product or omit it entirely
- Manual product compositing is time-consuming and may not match scene lighting/angle

**Two Strategies**:

**Strategy A: Keep Product Visible (Preferred)**
```
✅ Scene 2: Character discovers product → holds in hands
✅ Scene 3: Still holding product, adds drops to water jug
✅ Scene 4: Product visible beside character during wait
✅ Scene 5: Picks up product again to demonstrate
```
- **Rule**: Product must be visible in EVERY ending frame
- Either held by character OR positioned prominently in scene
- Plan camera angles to keep product in frame

**Strategy B: Plan for Manual Compositing**
```
✅ Scene 2: Character examines generic bottle
   Ending frame: Bottle held at chest level, clear view, good lighting
   → Manually composite real product in post
✅ Scene 3: Use composited ending frame from Scene 2 as starting point
   Generate with product visible throughout
```
- **Rule**: If product will be composited, ending frame MUST show:
  - Product in clear, unobstructed view
  - Good lighting on product area
  - Angle suitable for product placement (not extreme perspective)
  - Character's hand position/grip visible for natural compositing

**Common Mistakes**:
- ❌ Scene 2 ends with product → Scene 3 starts without product (broken continuity)
- ❌ Product too small/obscured in ending frame → Can't composite cleanly
- ❌ Product at extreme angle in ending → Looks unnatural when composited
- ❌ Assuming VEO 3 can recreate branded product from text description (it cannot)

**Best Practice for Product Videos**:
1. Start product introduction scene with actual product image (pre-composited if needed)
2. Never let product leave frame throughout remaining scenes
3. If product must exit, plan dedicated "product return" scene showing character retrieving it
4. For ending frames, always position product prominently for next scene continuity

---

## Workflow Overview

**Philosophy**: "Generate → Extract → Guide → Repeat"

```
Creative Brief → Scene 1 Prompt → Generate → Extract End Frame
                                                    ↓
Scene 7 Complete ← Scene 6 ← Scene 5 ← Scene 4 ← Scene 3 ← Scene 2 Prompt
```

**Key Advantage**: Real frames (not imagined images) ensure perfect continuity in lighting, character appearance, positioning, and environment.

---

## Phase 1: Creative Storyboarding

### 1.1 Define the Narrative Arc

**Required Elements**:
- **Problem**: What challenge does the protagonist face?
- **Journey**: How do they discover/implement the solution?
- **Resolution**: What's the emotional/practical outcome?

**Example - H2O Pure Campaign**:
```
Scene 1: Contaminated water desperation
Scene 2: Discovery of solution in backpack
Scene 3: Application/purification process
Scene 4: Waiting/time passage
Scene 5: Validation/testing success
Scene 6: Sharing with community
```

### 1.2 Scene Duration Planning

**6-Second Scenes** (Hailuo):
- 6 scenes = 36 seconds total
- Perfect for social media formats

**8-Second Scenes** (VEO 3):
- 7 scenes = 56 seconds (under 60s limit)
- More breathing room for action

### 1.3 Emotional Journey Mapping

Each scene must have clear emotional purpose:
```
Scene 1: Desperation/Frustration
Scene 2: Hope/Discovery
Scene 3: Action/Determination
Scene 4: Patience/Trust
Scene 5: Relief/Validation
Scene 6: Connection/Generosity
```

---

## Phase 2: Master Prompt Engineering

### 2.1 Scene 1 Foundation Prompt

**This is the MOST CRITICAL prompt** - it establishes:
- Character appearance (lock in details!)
- Environment/setting
- Lighting conditions
- Visual style/mood
- Camera angle

**Scene 1 Prompt Structure**:

```
[Camera Shot] Specific angle, movement, framing

[Subject] DETAILED character description with:
- Age, build, specific features
- Exact clothing (colors, style, details)
- Hair (length, color, texture)
- Facial features (beard, expressions)
- Props/gear visible

[Action] Second-by-second breakdown:
"At 1 second... At 2 seconds... At 3 seconds..."
- Opening state
- Mid-action development
- Ending position/expression

[Scene] Environment details:
- Location specifics
- Background elements
- Environmental conditions
- Atmospheric details

[Lighting] Precise lighting description:
- Source (sun, moon, artificial)
- Direction (rim, side, key)
- Quality (soft, harsh, golden)
- Time of day effects

[Style/Mood] Overall aesthetic:
- Visual style (cinematic, documentary)
- Emotional tone
- Technical specs (photorealistic, shallow DOF)
- Color grading direction
```

**Critical Success Factors**:
- ✅ Hyper-specific character details (copy these EXACTLY in all scenes)
- ✅ Realistic, achievable actions (not fantasy/impossible)
- ✅ Clear ending pose/position for next scene
- ✅ Consistent lighting that can evolve naturally

### 2.2 Character Consistency Template

**Create a character reference block** to copy into every scene:

```
MALE PROTAGONIST TEMPLATE:
- Male, mid-30s
- Shoulder-length brown hair with natural highlights
- Full beard (not just stubble)
- Lean athletic build
- Weathered/rugged appearance
- Olive green tactical jacket with chest pockets
- Dark tactical pants
- Black boots
- Survival gear (backpack, tools)
```

**Never deviate from these core details across scenes!**

---

## Phase 3: Generate → Extract → Human Review → Guide Cycle

**🚨 CRITICAL: This is NOT Fully Automated**

The workflow requires **human creative decision-making** at each step:
1. ✅ Generate Scene N (automated)
2. ✅ Download & extract ending frame (automated)
3. ⏸️ **HUMAN REVIEWS frame** and decides story direction
4. ⏸️ **HUMAN CRAFTS next prompt** based on what they see
5. ✅ Generate Scene N+1 (automated)

**The creative decisions are YOURS, not the AI's!**

### 📊 Auto-Quality Analysis (NEW)

**Enable automatic quality checking after each generation**:

```python
from scripts.kie_client import KieClient
client = KieClient()

result = client.generate_and_wait(
    prompt="YOUR_SCENE_PROMPT",
    model='veo3_fast',
    scene_name='scene_01',
    output_dir=Path('output/campaign_name'),
    extract_frame=True,
    analyze_quality=True  # NEW: Auto-analyze after generation
)
```

**What Auto-Analysis Does**:
1. Extracts frames at 2-second intervals
2. Logs frame extraction for quick review
3. Auto-cleans up extracted frames after analysis
4. Helps catch issues immediately:
   - Character consistency breaks
   - Environmental elements disappearing
   - Lighting issues
   - Missing actions

**Manual Quality Check** (for deeper analysis):
```python
from scripts.video_quality_analyzer import VideoQualityAnalyzer

analyzer = VideoQualityAnalyzer()
video_path = Path("output/scene_01.mp4")

# Extract frames for inspection
frames = analyzer.extract_frames_at_intervals(
    video_path,
    interval=1.0  # Every second
)

# Review frames, then cleanup
analyzer.cleanup_analysis_folder(frames[0].parent)
```

### ⚠️ CRITICAL LESSONS LEARNED

#### Character Continuity Requirements
**Problem**: If Scene N's ending frame doesn't show the character's face, Scene N+1 cannot maintain character consistency.

**Solution**:
- Always ensure ending frames show character's face in 3/4 or profile view
- Include in prompt: "ending with character's face visible looking toward [next action]"
- Plan ahead: If character turns away, ensure they turn back before scene ends
- Example: "At 6-8 seconds, sits back and turns face 3/4 toward camera"

#### Environmental Consistency in Time-lapses
**Problem**: Elements like trees may disappear during lighting transitions (sunset to night).

**Solution**:
- Explicitly state what must remain constant: "oak tree remains visible and consistent throughout entire sequence"
- Specify lighting changes affect appearance, not existence: "tree silhouette becomes more prominent" not "tree fades"
- Use fixed camera positions for time-lapses to maintain spatial relationships
- Repeat key element descriptions at each time point: "oak tree trunk warm and detailed" → "oak tree now backlit"

#### Ending Frame Planning
**Problem**: You can't fix a bad ending frame after generation - it determines your next scene's starting point.

**Solution**:
- Always specify the exact ending position in your prompt
- Think ahead: What do I need visible for Scene N+1?
- Include: Character face, key objects, environmental context
- Avoid: Character walking out of frame, back to camera, extreme close-ups that lose context

#### Action Density (8-Second Rule)
**Problem**: Trying to pack too many actions into 8 seconds results in incomplete or rushed execution.

**Failed Example**: "Man walks to camp → arrives → holds up jug → others turn → demonstrates solution"
- Result: Only walking/arrival rendered, no actual interaction

**Solution - Apply VEO 3 Mastery Principles**:
1. **Step-by-Step Sequence**: Break complex actions into 2-second chunks (4 clear steps max)
2. **One Primary Action**: Focus on ONE main transformation or moment
3. **Physics Awareness**: Describe how things behave, not just what happens
4. **Specific Timing**: Use exact timestamps: "At 0-2 seconds", "At 2-4 seconds", etc.

**Corrected Approach**:
```
WRONG:
"Man walks to camp, arrives, and interacts with survivors"
(3 major actions = too much)

RIGHT:
"Man already at camp edge, holds up jug to gathered survivors"
(Start at the key moment, use full 8s for interaction)

OR split into 2 scenes:
Scene 6A: Journey to camp (walking, arrival)
Scene 6B: Interaction at camp (demonstration, sharing)
```

**Key Insight from veo3_prompt_analysis.md**:
- Top prompts succeed by giving VEO 3 clear, sequential instructions
- "At X seconds" timing prevents action cramming
- Physics descriptions (how objects move) render better than action lists

#### Continuity Breaks from Poor Planning
**Problem**: Scene N ends in one state, but Scene N+1 starts in completely different state, breaking visual flow.

**Failed Example**:
- Scene 5 ends: Man sitting at night with water jug
- Scene 6 starts: Man standing at camp with other people
- **Break**: How did he get there? Where did others come from?

**Solution - Plan Scene Transitions**:
```
Scene 5: Man sitting, testing water, looks toward distant lights
         (Ending shows him sitting, facing distant direction)

Scene 6: Man stands from sitting position, walks toward lights
         (Uses Scene 5 ending frame as starting point)
         (Ends with him arriving at camp edge)

Scene 7: Man already at camp, interacts with survivors
         (Uses Scene 6 ending frame showing camp arrival)
```

**Critical Rule**: Never skip logical steps between scenes. If ending and beginning don't match, you've broken continuity.

#### JSON Prompting for Complex Scenes
**Problem**: Plain text prompts lack hierarchical structure and completeness checks.

**From veo3_prompt_analysis.md - Why JSON Dominates**:
1. **Hierarchical Thinking**: Forces separation of camera, lighting, audio, motion
2. **Completeness Check**: Hard to forget elements when structured
3. **Reusability**: Swap one field, keep structure
4. **AI Comprehension**: Matches VEO 3's computational structure

**When to Use JSON**:
- Multiple characters interacting
- Complex camera movements
- Precise lighting requirements
- Detailed audio specifications
- Any scene requiring professional production quality

**Plain Text is OK for**:
- Simple single-character actions
- Straightforward continuity scenes
- Quick iteration/testing

**Best Practice**: Use JSON for final production scenes, especially those with multiple elements or interactions.

### 3.1 Scene 1 Generation

**Input**:
- Master Scene 1 prompt (text-to-video)
- No image reference needed

**Using Universal Kie Client** (Recommended):
```python
from scripts.kie_client import KieClient
from pathlib import Path

client = KieClient()

# Complete workflow: Generate → Poll → Download → Extract
result = client.generate_and_wait(
    prompt="YOUR_SCENE_1_PROMPT",
    model='veo3_fast',
    scene_name='scene_01',
    output_dir=Path('output/campaign_name'),
    extract_frame=True  # Auto-extract ending frame
)

print(f"Video: {result['video_path']}")
print(f"Ending frame: {result['frame_path']}")
# Ending frame ready for Scene 2!
```

**Manual API Call** (if needed):
```python
import requests
import json

api_key = "YOUR_API_KEY"
url = "https://api.kie.ai/api/v1/veo/generate"

payload = {
    "prompt": "YOUR_SCENE_1_PROMPT",
    "model": "veo3_fast",
    "aspectRatio": "16:9",
    "enableFallback": True,
    "enableTranslation": True
}

response = requests.post(url,
    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    },
    json=payload
)

result = response.json()
task_id = result['data']['taskId']
print(f"Task ID: {task_id}")
# Check https://kie.ai/dashboard for completion
```

**Wait Time**: 10-15 minutes
**Polling**: Default 60s intervals, 20min timeout

### 3.2 Extract Ending Frame

**Once Scene 1 completes**:

1. Download video from Kie.ai dashboard
2. Extract final frame (multiple methods):

**Option A - FFmpeg**:
```bash
# Extract last frame
ffmpeg -sseof -1 -i scene1.mp4 -vframes 1 scene1_ending.jpg

# Or extract frame at specific timestamp (e.g., 7.9s for 8s video)
ffmpeg -i scene1.mp4 -ss 00:00:07.900 -vframes 1 scene1_ending.jpg
```

**Option B - Screenshot**:
- Play video in media player
- Pause at final frame
- Screenshot (ensure high quality, no UI elements)

**Option C - Video Editing Software**:
- Import to editor (DaVinci Resolve, Premiere)
- Navigate to last frame
- Export frame as image

**Quality Requirements**:
- ✅ Full resolution (1920×1080 for 16:9)
- ✅ No compression artifacts
- ✅ No player UI/watermarks
- ✅ Exact final frame (not 1-2 frames before)

### 3.3 Upload Frame for Next Scene

**Upload to Kie.ai File API**:

```python
import requests
import json
import base64

api_key = "YOUR_API_KEY"
upload_url = "https://kieai.redpandaai.co/api/file-base64-upload"

# Read and encode image
with open('scene1_ending.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

upload_payload = {
    'base64Data': f'data:image/jpeg;base64,{image_data}',
    'uploadPath': 'veo3-scenes',
    'fileName': 'scene1_ending.jpg'
}

response = requests.post(upload_url,
    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    },
    json=upload_payload
)

result = response.json()
image_url = result['data']['downloadUrl']
print(f"Image URL: {image_url}")
# Save this URL for Scene 2 generation!
```

**Note**: Uploaded images auto-delete after 3 days (sufficient for production workflow)

### 3.4 Create Scene 2 Prompt (Guided by Frame)

**Look at the ending frame and observe**:
- Character's exact position/pose
- Lighting conditions at scene end
- Background elements visible
- Props/objects in frame
- Emotional expression

**Build Scene 2 prompt that logically continues**:

```
[Camera Shot] Continue from previous angle OR justify camera movement

[Subject] EXACT SAME character description + current pose/position

[Action] Opens with the ENDING STATE from Scene 1, then:
"Opens with [describe ending frame state].
At 1 second, [next logical action]...
At 2 seconds, [progression]...
..."

[Scene] Same environment OR justify location change

[Lighting] Continue lighting progression (sunset → dusk → night)

[Style/Mood] Emotional evolution from previous scene
```

**Example Transition**:

Scene 1 ends: Man pouring out contaminated water, frustrated
Scene 2 opens: "Opens with man finishing pouring out contaminated water onto ground, water splashing onto dirt creating small puddle..."

**Continuity Checklist**:
- [ ] Character description identical
- [ ] Opening action matches ending frame
- [ ] Lighting evolves naturally
- [ ] Camera movement justified
- [ ] Props/environment consistent

### 3.5 Generate Scene 2 (Image-to-Video)

**Critical**: Include `imageUrls` parameter with uploaded frame!

```python
import requests
import json

api_key = "YOUR_API_KEY"
generate_url = "https://api.kie.ai/api/v1/veo/generate"

payload = {
    "prompt": "YOUR_SCENE_2_PROMPT",
    "model": "veo3_fast",
    "aspectRatio": "16:9",
    "enableFallback": True,
    "enableTranslation": True,
    "imageUrls": ["https://tempfile.redpandaai.co/.../scene1_ending.jpg"]
}

response = requests.post(generate_url,
    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    },
    json=payload
)

result = response.json()
task_id = result['data']['taskId']
print(f"Scene 2 Task ID: {task_id}")
```

### 3.6 Repeat Cycle for Remaining Scenes

**For each subsequent scene**:

```
Scene N Complete
    ↓
Extract ending frame
    ↓
Upload frame to Kie.ai
    ↓
Analyze frame for continuity details
    ↓
Write Scene N+1 prompt (starting from frame state)
    ↓
Generate Scene N+1 with imageUrls parameter
    ↓
Repeat until campaign complete
```

**Track Progress**:
```
Scene 1: ✅ Generated, ending frame extracted
Scene 2: ✅ Generated (using S1 frame), ending frame extracted
Scene 3: ⏳ Generating (using S2 frame)
Scene 4: ⏸️ Awaiting S3 completion
Scene 5: ⏸️ Awaiting S4 completion
Scene 6: ⏸️ Awaiting S5 completion
```

---

## Phase 4: Product Integration Strategy

### 4.1 When to Insert Real Products

**Challenge**: AI can't generate your exact product with branding

**Solution**: Generate generic placeholder, composite real product in post

**Workflow**:

1. **Scene with product**: Generate with generic description
   ```
   "small plastic dropper bottle approximately 1 inch tall with white cap"
   ```

2. **Extract frame** where product is visible

3. **Post-production compositing**:
   - Mask out generic AI product
   - Insert real product image (photographed on transparent background)
   - Match lighting, scale, perspective
   - Color grade to blend seamlessly

**Tools**:
- Photoshop (masking, compositing)
- After Effects (video tracking if product moves)
- DaVinci Resolve Fusion (compositing)

### 4.2 Minimizing Product Visibility Until Ready

**Strategy**: Hide product until moment of reveal, then composite

**Prompt Techniques**:
```
"small bottle barely visible being extracted from pack interior in final moment"
"bottle held in palm with fingers partially obscuring label"
"bottle kept low and out of clear view"
"dropper positioned above jug but bottle mostly hidden by hand angle"
"at 7 seconds, hand moves bottle away out of frame"
"both hands now empty grip jug sides, bottle completely out of view"
```

**Why This Matters**:
- AI can only recreate products it has seen in the starting frame
- If you show AI a partial/obscured product view, it will hallucinate the details incorrectly
- Better to hide the product after initial reveal and composite only where clearly visible

**Post-Production is Your Friend**: Better to have clean plates and composite than rely on AI for branded products

### 4.3 AI-Powered Product Compositing (Nano-Banana)

**Using Google Gemini 2.5 Flash Image for product replacement**:

```python
import sys
sys.path.append('/home/dev/.claude/scripts')
from nano_banana_client import NanoBananaClient
from pathlib import Path

client = NanoBananaClient()

# Composite real product into scene
result = client.fuse_images(
    prompt="Replace the generic bottle with the H2O Pure branded bottle, matching golden hour lighting, preserving hand grip and shadows, natural integration",
    images=[
        Path('output/scene_02_ending.jpg'),  # Scene with generic bottle
        Path('images/h2o_pure_product.png')  # Real branded product
    ],
    output_path=Path('output/scene_02_with_product.jpg')
)

print(f"Composited: {result['output_path']}")
# Use this composited frame for next scene generation!
```

**When AI Compositing Works Well**:
- ✅ Product clearly visible in one frame only
- ✅ Simple backgrounds
- ✅ Good lighting match
- ✅ Static product (not moving)

**When to Use Traditional Tools**:
- ❌ Product visible across multiple seconds of video
- ❌ Product moving/rotating
- ❌ Complex lighting changes
- ❌ Need pixel-perfect brand accuracy

---

## Phase 5: Assembly & Post-Production

### 5.1 Scene Assembly

**Timeline Assembly**:
1. Import all scenes in order
2. Minimal crossfades (0.1-0.2s) since frames already match
3. Trim any duplicate frames at transitions
4. Ensure total duration hits target (30s, 60s, etc.)

**Continuity QC**:
- [ ] Character appearance consistent
- [ ] No jarring lighting jumps
- [ ] Props maintain consistency
- [ ] Background elements coherent
- [ ] Camera movement flows naturally

### 5.2 Color Grading

**Unify Look Across Scenes**:
- Apply consistent LUT/grade
- Match contrast levels
- Ensure lighting evolution is smooth (golden hour → dusk → night)
- Post-apocalyptic grade example:
  - 70% desaturation
  - Orange/teal split toning
  - Lifted blacks (slightly faded look)
  - Film grain overlay (2-5% opacity)

### 5.3 Audio Layer

**Since videos generate WITHOUT dialogue**:

1. **Voiceover** (if needed):
   - Professional narration (11Labs, ElevenLabs)
   - Timed to visual beats
   - Matches emotional tone

2. **Ambient Sound**:
   - Water sounds (splashing, pouring)
   - Foley (backpack unzipping, footsteps)
   - Environmental ambience (wind, birds)

3. **Music**:
   - Emotional score matching narrative arc
   - Build tension → resolution
   - Subtle, not overpowering

4. **Sound Design**:
   - Impact moments (product reveal)
   - Transition whooshes
   - Atmospheric layers

### 5.4 Final Export

**Recommended Settings**:
```
Format: MP4 (H.264)
Resolution: 1920×1080 (16:9) or 1080×1920 (9:16)
Frame Rate: 24fps or 30fps (match source)
Bitrate: 10-15 Mbps (high quality)
Audio: AAC 192kbps
```

---

## Production Timeline Example

### 6-Scene Campaign (8s per scene = 48s total)

| Phase | Duration | Tasks |
|-------|----------|-------|
| **Creative Planning** | 1-2 hours | Storyboard, character design, scene breakdown |
| **Scene 1 Prompt** | 30 min | Write master prompt with all details |
| **Scene 1 Generate** | 10-15 min | API call, wait for completion |
| **Extract Frame 1** | 5 min | Download, extract, upload frame |
| **Scene 2 Prompt** | 20 min | Analyze frame, write continuation |
| **Scene 2 Generate** | 10-15 min | Image-to-video generation |
| **Extract Frame 2** | 5 min | Repeat extraction process |
| **Scenes 3-6** | 3-4 hours | Repeat cycle (4 scenes × ~45min each) |
| **Product Compositing** | 1-2 hours | Replace AI products with real branding |
| **Assembly & Edit** | 1 hour | Timeline assembly, transitions |
| **Color Grade** | 30 min | Unify look, apply LUT |
| **Audio Mixing** | 1 hour | Voiceover, music, sound design |
| **Final Export** | 15 min | Render and QC |
| **TOTAL** | **8-11 hours** | Complete 48-second narrative video |

---

## Best Practices & Pro Tips

### Character Consistency
✅ **DO**: Copy exact character description into every prompt
✅ **DO**: Use distinctive features as anchors (scars, jewelry, gear)
✅ **DO**: Keep clothing/styling identical across all scenes
❌ **DON'T**: Paraphrase or "improve" character details between scenes
❌ **DON'T**: Introduce new clothing/accessories mid-campaign

### Lighting Progression
✅ **DO**: Plan natural time progression (sunset → dusk → night)
✅ **DO**: Keep lighting direction consistent (sun from right throughout)
✅ **DO**: Use time-lapse effects to justify lighting changes
❌ **DON'T**: Jump from night to day without transition
❌ **DON'T**: Change lighting direction randomly between scenes

### Action Continuity
✅ **DO**: End scenes in positions that logically lead to next action
✅ **DO**: Use "At X seconds" timestamps for precise action control
✅ **DO**: Build emotional progression across scenes
❌ **DON'T**: End scenes with impossible-to-continue poses
❌ **DON'T**: Rush actions - let moments breathe

### Technical Quality
✅ **DO**: Use "photorealistic, shot on professional camera" in prompts
✅ **DO**: Specify camera specs (lens, aperture) for consistency
✅ **DO**: Add natural imperfections (dust, wear, texture)
❌ **DON'T**: Use cartoon/anime/illustrated style terms
❌ **DON'T**: Overload prompts - focus on one clear action per scene

### Cost Optimization
✅ **DO**: Use `veo3_fast` ($0.38) for testing/iteration
✅ **DO**: Switch to `veo3` ($1.50) for final hero shots only
✅ **DO**: Generate 3 videos at once (Hailuo credit efficiency)
✅ **DO**: Enable `enableFallback: true` (25% higher success rate)
❌ **DON'T**: Use premium model for every test iteration
❌ **DON'T**: Regenerate entire campaigns - fix problem scenes only

---

## Troubleshooting Common Issues

### Issue: Scene 2 doesn't match Scene 1 ending
**Cause**: Prompt doesn't accurately describe ending frame state
**Solution**:
- Review ending frame carefully
- Copy exact pose/position description
- Ensure lighting description matches
- Use image-to-video with uploaded frame

### Issue: Character appearance changes between scenes
**Cause**: Inconsistent character description across prompts
**Solution**:
- Create master character template
- Copy EXACT description into every scene
- Never paraphrase or "improve" character details
- Use distinctive features as consistency anchors

### Issue: Lighting jumps dramatically between scenes
**Cause**: Unrealistic lighting progression in prompts
**Solution**:
- Plan natural time progression upfront
- Use transition scenes (time-lapse) for major changes
- Keep lighting direction consistent throughout
- Describe lighting evolution explicitly in prompts

### Issue: Props/products don't match real branding
**Cause**: AI invents generic versions of products
**Solution**:
- Use generic descriptions in prompts
- Plan for post-production compositing
- Generate with product barely visible/obscured
- Replace AI products with real photography

### Issue: Actions feel rushed or incomplete
**Cause**: Too much action crammed into 6-8 seconds
**Solution**:
- Focus on ONE clear action per scene
- Use "At X seconds" timestamps
- Let emotional moments breathe
- Add additional scenes if needed for pacing

---

## Conclusion

This frame-to-frame workflow transforms AI video generation from isolated clips into cohesive narratives with cinema-quality continuity. By using real ending frames to guide each subsequent prompt, you eliminate guesswork and ensure seamless visual flow.

**Key Takeaways**:
1. **Strong Scene 1 foundation** locks in character, style, environment
2. **Extract real frames** (not imagined images) for perfect continuity
3. **Image-to-video generation** with uploaded frames ensures consistency
4. **Copy character descriptions exactly** across all scenes
5. **Plan lighting progression** naturally (time of day evolution)
6. **Composite real products** in post-production for brand accuracy
7. **Focus on emotion** - technology serves story, not vice versa

**Cost**: ~$2-5 for 6-scene campaign (veo3_fast)
**Time**: 8-11 hours start to finish
**Result**: Professional 30-60 second narrative video with seamless continuity

---

## Universal Client Scripts

This project includes universal API clients for streamlined workflow:

### VEO 3 Client (`scripts/kie_client.py`)
```python
from scripts.kie_client import KieClient

client = KieClient()

# All-in-one generation workflow
result = client.generate_and_wait(
    prompt="scene prompt",
    image_path=Path("previous_frame.jpg"),  # Optional
    scene_name="scene_02",
    output_dir=Path("output/campaign"),
    extract_frame=True
)
```

**Available Methods**:
- `generate_video()` - Generate video
- `get_status()` - Check status
- `poll_until_complete()` - Auto-poll (60s intervals, 20min timeout)
- `download_video()` - Download from URL
- `extract_last_frame()` - FFmpeg frame extraction
- `upload_image()` - Upload to Kie.ai
- `get_1080p_video()` - Request 1080p version
- `generate_and_wait()` - Complete workflow

### Nano-Banana Client (`/home/dev/.claude/scripts/nano_banana_client.py`)
```python
import sys
sys.path.append('/home/dev/.claude/scripts')
from nano_banana_client import NanoBananaClient

client = NanoBananaClient()

# Image generation
result = client.text_to_image(
    prompt="product photography",
    output_path=Path("output/image.png")
)

# Image editing/compositing
result = client.fuse_images(
    prompt="composite instructions",
    images=[Path("scene.jpg"), Path("product.png")],
    output_path=Path("output/composited.jpg")
)

# With aspect ratio control
result = client.generate_with_aspect_ratio(
    prompt="description",
    aspect_ratio="16:9",
    output_path=Path("output/wide.png")
)
```

**Available Methods**:
- `text_to_image()` - Text-to-image generation
- `edit_image()` - Edit existing image
- `fuse_images()` - Multi-image compositing
- `generate_with_aspect_ratio()` - Aspect ratio control (16:9, 9:16, 4:3, etc.)

---

## Additional Resources

- **VEO 3 API Docs**: https://docs.kie.ai/veo3-api
- **File Upload API**: https://docs.kie.ai/file-upload-api/upload-file-base-64
- **Hailuo Tutorial**: `/docs/hailuo.md` (techniques work for VEO 3 as well)
- **VEO 3 Mastery Guide**: `/docs/veo3-essential-mastery-guide.md`
- **Universal Clients**:
  - `/scripts/kie_client.py` (VEO 3)
  - `/home/dev/.claude/scripts/nano_banana_client.py` (Gemini image generation)

---

*Last Updated: 2025-09-30*
