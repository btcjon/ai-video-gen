# VEO 3 Complete Mastery Guide: Professional AI Video Creation

## Table of Contents
1. [Quick Start Foundation](#quick-start-foundation)
2. [The Ultimate Prompt Formula](#ultimate-prompt-formula)
3. [Frame-to-Frame Workflow for Long Videos](#frame-to-frame-workflow)
4. [Critical Success Principles](#critical-success-principles)
5. [Vertical Video Mastery](#vertical-video-mastery)
6. [Character Consistency](#character-consistency)
7. [Photorealistic Character Creation](#photorealistic-characters)
8. [Commercial-Quality JSON Prompting](#json-prompting)
9. [23 Proven Examples](#proven-examples)
10. [Camera Angles & Storytelling](#camera-storytelling)
11. [Workflow Optimization](#workflow-optimization)
12. [Cost Optimization](#cost-optimization)
13. [Troubleshooting Guide](#troubleshooting)

---

## Quick Start Foundation {#quick-start-foundation}

### Platform Access
- **Primary**: OpenArt platform → Video → Text → Select "Google VEO 3"
- **Alternative**: Search "VEO 3" on Google → First result → "Try in Gemini"
- **API Access**: Kie.ai (75% cheaper for programmatic generation)

### Critical Settings
- ✅ **Resolution**: Highest available (1080p) → Always upscale to 4K
- ✅ **Mode**: Normal/Quality (never Fast mode for finals)
- ✅ **Audio**: Enable for dialogue/sound, disable for silent content
- ✅ **Duration**: 8 seconds maximum (cannot generate longer clips)

### Platform Comparison

| Provider | Cost (8s video) | Features | Best For |
|----------|-----------------|----------|----------|
| **Google Gemini API** | $6.00 | Official, Full features | Production apps |
| **Kie.ai** | $1.50 (Quality) / $0.38 (Fast) | 75% cheaper, Native 9:16, Fallback | Cost optimization |
| **Veo3API.ai** | ~$1.80 | 70% cheaper | High volume |
| **AI/ML API** | ~$6.30 | 200+ models | Multi-model projects |

---

## The Ultimate Prompt Formula {#ultimate-prompt-formula}

### 10 Essential Components (Use ALL)

```
[1. SCENE SETUP] + [2. SUBJECT DESCRIPTION] + [3. BACKGROUND] + 
[4. ACTION] + [5. VIDEO STYLE] + [6. CAMERA SETTINGS] + 
[7. COMPOSITION] + [8. LIGHTING & MOOD] + [9. AUDIO] + 
[10. NEGATIVE INSTRUCTIONS]
```

### Claude Auto-Prompt Template (Copy & Use)

```
Expand this into a full VEO 3 prompt using this structure:

1. Scene Summary – Rewrite my brief as a cinematic moment in one clear sentence.
2. Subject – Describe the main subject(s) in rich detail (appearance, clothing, physical features).
3. Background & Context – Expand the setting/environment for my idea.
4. Action – Describe what's happening, based on my brief, with realistic movement.
5. Style & Aesthetic – Always cinematic, photorealistic, professional film look, high detail.
6. Camera Instructions – Add shot type (close-up, wide shot, POV, aerial, etc.), movement (dolly, pan, tracking), and angle (eye-level, low/high).
7. Composition & Framing – Professional framing that emphasizes the subject clearly.
8. Lighting & Mood – Realistic cinematic lighting to match the mood (golden hour, moody, neon, etc.).
9. Audio – Add dialogue/ambient sounds/effects that fit the scene. Always add (no subtitles).
10. Color Palette – Cohesive cinematic tones that enhance mood.
11. Negative Instructions – Avoid subtitles, distortions, unrealistic proportions, flickering, or extra characters not in the brief.

Expand it into a full VEO 3 prompt, but write it as one continuous cinematic paragraph (not bullet points, no section labels).

[YOUR SIMPLE IDEA HERE]
```

**Key**: Replace `[YOUR SIMPLE IDEA HERE]` with your concept and get a perfect VEO 3 prompt every time.

---

## Frame-to-Frame Workflow for Long Videos {#frame-to-frame-workflow}

### The 8-Second Reality

**VEO 3 Limitation**: Maximum 8-second clips (cannot be extended)
**Solution**: Frame-to-video continuation for seamless longer content

### 🚨 The 7 Critical Rules for Multi-Scene Success

#### 1. **FACE MUST BE VISIBLE IN ENDING FRAME**
**Why**: VEO 3 cannot maintain character consistency without facial reference.

- ❌ WRONG: Character walking away, back to camera, face obscured
- ✅ RIGHT: Character in 3/4 profile or facing camera at scene end
- **Rule**: Always end scenes with face visible at chest level or closer

**Scene Ending Checklist**:
- [ ] Character's face clearly visible (not turned away)
- [ ] Face showing at chest level or closer (not distant)
- [ ] 3/4 profile minimum (full face preferred)
- [ ] Good lighting on face
- [ ] Expression visible

#### 2. **ONE ACTION PER 8-SECOND SCENE**
**Why**: Cramming multiple actions results incomplete execution.

- ❌ WRONG: "Walk to camp + arrive + interact + demonstrate" (4 actions)
- ✅ RIGHT: "Walk to camp and arrive" (1 action) → Next scene: "Interact and demonstrate" (1 action)
- **Rule**: Max 4 distinct 2-second steps per scene, all serving ONE primary action

**Action Density Formula**:
```
Scene 1: ONE action (8 seconds)
  0-2s: Setup
  2-6s: Main action
  6-8s: Completion/transition

NOT this:
Scene 1: FOUR actions (8 seconds)
  0-2s: Action A
  2-4s: Action B
  4-6s: Action C
  6-8s: Action D
  Result: None fully executed
```

#### 3. **MAINTAIN CONTINUITY BETWEEN SCENES**
**Why**: Skipping logical steps breaks visual flow.

- ❌ WRONG: Scene N ends sitting → Scene N+1 starts standing at different location
- ✅ RIGHT: Scene N ends sitting → Scene N+1 starts sitting, then stands
- **Rule**: Ending state of Scene N = Starting state of Scene N+1

**Continuity Planning**:
```
Scene 3 ends: Man sitting by fire at night
Scene 4 must start: Man sitting by fire at night, then [new action]

NOT: Man already standing at camp (broken continuity)
```

#### 4. **USE JSON FOR COMPLEX SCENES**
**Why**: Plain text lacks structure and completeness checks.

- **Use JSON for**: Multiple characters, camera movements, precise lighting, interactions
- **Plain text OK for**: Simple single-character continuity scenes
- **Rule**: When in doubt about completeness, use JSON structure

#### 5. **PLAN TRANSITIONS, DON'T SKIP THEM**
**Why**: Major location/time changes need transition scenes.

- ❌ WRONG: Forest → teleport to camp
- ✅ RIGHT: Forest → see lights → walk toward lights → arrive at camp (2-3 scenes)
- **Rule**: If ending and beginning don't match, add a transition scene

#### 6. **ESTABLISH ENVIRONMENTAL AESTHETICS AT TRANSITION**
**Why**: Major style changes (day→night, location shifts) need clear visual direction.

- ❌ WRONG: Scene 3 (sunset) ends vague → Scene 4 (night) generates poor night look
- ✅ RIGHT: Scene 3 ending explicitly describes complete night aesthetic

**Examples of Environmental Transition Descriptions**:

**Night Transition**:
```
"ending with deep blue twilight, first stars visible, silver moonlight 
beginning to illuminate scene, cool color temperature establishing night 
aesthetic"
```

**Dawn Transition**:
```
"ending with warm golden orange horizon, soft pink sky, warm color 
temperature, volumetric morning mist"
```

**Indoor→Outdoor**:
```
"ending with natural daylight flooding in, warm vs cool contrast, 
clear weather conditions visible through opening"
```

**Rule**: The scene where transition HAPPENS must end with complete aesthetic description.

#### 7. **PRODUCT VISIBILITY THROUGHOUT CHAIN** ⚠️ CRITICAL
**Why**: Once product disappears, VEO 3 cannot accurately recreate it.

**The Product Continuity Problem**:
- VEO 3 cannot recreate branded products (logos, labels, specific designs)
- If product exits frame → Next scene hallucines incorrect product or omits it
- Manual compositing is time-consuming and may not match lighting/angle

**Strategy A: Keep Product Visible (Preferred)**
```
✅ Scene 2: Character discovers product → holds in hands
✅ Scene 3: Still holding product, adds drops to water jug
✅ Scene 4: Product visible beside character during wait
✅ Scene 5: Picks up product again to demonstrate
```
- **Rule**: Product must be visible in EVERY ending frame
- Either held by character OR positioned prominently in scene

**Strategy B: Plan for Manual Compositing**
```
✅ Scene 2: Character examines generic bottle
   Ending frame: Bottle at chest level, clear view, good lighting
   → Manually composite real product in post
✅ Scene 3: Use composited ending frame as starting point
```

**Ending Frame Requirements for Compositing**:
- [ ] Product in clear, unobstructed view
- [ ] Good lighting on product area
- [ ] Angle suitable for placement (not extreme perspective)
- [ ] Character's hand position/grip visible

**Common Mistakes**:
- ❌ Scene 2 ends with product → Scene 3 starts without product
- ❌ Product too small/obscured in ending frame
- ❌ Product at extreme angle in ending
- ❌ Assuming VEO 3 can recreate branded product from description

### The Frame Continuation Method

**Core Principle**: Use last frame of Scene 1 as starting image for Scene 2

**Why This Works**:
- ✅ Maintains character consistency automatically
- ✅ Preserves environment and lighting
- ✅ Creates natural flow between scenes
- ✅ Avoids jarring cuts or character changes

### The 85/15 Rule for Continuations

**Keep 85% Identical Between Scenes**:
- Same character description (exact wording)
- Same environment details
- Same lighting setup and mood
- Same camera angle and framing

**Change Only 15%**:
- The specific action/movement
- Minor prop additions (if needed)
- Slight camera movement (if necessary)

### Step-by-Step Process

**Step 1: Generate Initial Scene**
```json
{
  "scene": "Scene 1 - Introduction",
  "prompt": "45-year-old father with salt-and-pepper hair checking emergency 
  supplies in dimly lit garage, worried expression, wearing gray t-shirt, 
  cinematic lighting with 2:1 ratio, handheld camera, shallow depth of field"
}
```

**Step 2: Extract Last Frame**
```bash
# FFmpeg method
ffmpeg -sseof -1 -i scene1.mp4 -vframes 1 scene1_ending.jpg

# Or extract at specific timestamp (7.9s for 8s video)
ffmpeg -i scene1.mp4 -ss 00:00:07.900 -vframes 1 scene1_ending.jpg
```

**Step 3: Generate Continuation (85% Same)**
```json
{
  "scene": "Scene 2 - Continuation",
  "starting_image": "scene1_ending.png",
  "prompt": "45-year-old father with salt-and-pepper hair finding water bottle 
  among emergency supplies in dimly lit garage, relieved expression, wearing 
  gray t-shirt, cinematic lighting with 2:1 ratio, handheld camera, shallow 
  depth of field"
}
```

**Notice**: Only changed "checking" → "finding water bottle" and "worried" → "relieved"

### Scene Segmentation Strategy

**Break Your Story into 8-Second Chunks**:
```
0:00-0:08  Scene 1a: Establish crisis/problem
0:08-0:16  Scene 1b: Continue - character reacts
0:16-0:24  Scene 2a: Introduce solution/product
0:24-0:32  Scene 2b: Continue - demonstrate solution
0:32-0:40  Scene 3a: Show transformation/results
0:40-0:48  Scene 3b: Continue - final impact
```

### Transition Management

**Expect 1-2 Second Potential Jump**:
- Trim awkward transition frames
- Add subtle crossfade if needed (0.5s)

**Pro Tip**: Ensure ending frames show clean, usable poses

### When to Start Fresh vs Continue

**Use Frame Continuation When**:
- ✅ Same character in same location
- ✅ Sequential action/story beat
- ✅ Maintaining emotional continuity
- ✅ Same time of day/lighting

**Start Fresh When**:
- ❌ Location change (garage → kitchen)
- ❌ Time jump (day → night)
- ❌ Different character/angle needed
- ❌ Major scene transition

### Production Timeline: 6-Scene Campaign

**Total Duration**: 48 seconds (8s × 6 scenes)
**Total Time**: 8-11 hours
**Total Cost**: $2-5 (using veo3_fast)

| Phase | Duration | Tasks |
|-------|----------|-------|
| **Creative Planning** | 1-2 hours | Storyboard, character design |
| **Scene 1 Prompt** | 30 min | Master prompt with all details |
| **Scene 1 Generate** | 10-15 min | Wait for completion |
| **Extract Frame 1** | 5 min | Download, extract, upload |
| **Scene 2 Prompt** | 20 min | Analyze frame, write continuation |
| **Scene 2 Generate** | 10-15 min | Image-to-video generation |
| **Scenes 3-6** | 3-4 hours | Repeat cycle (4 × ~45min) |
| **Product Compositing** | 1-2 hours | Replace AI products |
| **Assembly & Edit** | 1 hour | Timeline, transitions |
| **Color Grade** | 30 min | Unify look, apply LUT |
| **Audio Mixing** | 1 hour | Voiceover, music, SFX |
| **Final Export** | 15 min | Render and QC |

---

## Critical Success Principles {#critical-success-principles}

### 🎯 The Golden Rules

**1. Never Use Simple Prompts**
- ❌ "knight riding horse"
- ✅ "silver armored knight on black horse riding through misty forest at dawn, cinematic wide shot with dramatic lighting"

**2. Always Include Negative Instructions**
- Essential phrase: "No subtitles, no distortions, no unrealistic proportions, no flickering, no extra characters"
- Prevents 80% of common failures

**3. Specify Everything**
- Time of day (golden hour, sunset, midnight)
- Camera movement (dolly in, pan right, tracking shot)
- Lighting style (soft natural light, dramatic shadows, neon glow)
- Audio cues (spoken dialogue, ambient sounds, music)

**4. Write Continuous Paragraphs**
- VEO 3 processes flowing narrative better than bullet points
- Avoid labeled sections in final prompt

**5. Think Like a Director, Not a Typist**
- You have film director power through prompts
- Provide complete production briefs, not casual descriptions
- **If it's not the model—it's your prompt**

---

## Vertical Video Mastery {#vertical-video-mastery}

### True 9:16 Video Creation with Kie.ai

**The Reality**: VEO 3 outputs 16:9 by default (even with vertical prompts)

**Solution**: Create vertically-framed content within 16:9, then crop in editing

### The Working Formula for 9:16 Content

```
A close-up vertically framed portrait video of [SUBJECT] standing in the 
center of the frame, captured in vertical mode, cinematic lighting, sharp 
focus, shallow depth of field, 9:16 aspect ratio. [SUBJECT ACTION]. 
Optimized for [PLATFORM] with [ENERGY LEVEL] energy and mobile-optimized 
composition.
```

### Platform-Specific Optimizations

**TikTok**:
- High energy, dynamic movement
- "Trending viral style with engaging visuals"
- Centered composition with clear subject
- Hook in first 2 seconds

**Instagram Reels**:
- Polished aesthetic, premium feel
- "Instagram-worthy framing with visual appeal"
- Smooth progression throughout
- Style-conscious composition

**YouTube Shorts**:
- Clear narrative, informative
- "Educational-friendly with good readability"
- Balanced energy, clear visual hierarchy
- Tutorial-friendly framing

**Snapchat**:
- Casual, authentic, fun
- Close-up focused for intimacy
- Immediate impact
- Spontaneous feel

### ⚠️ Post-Production Reality
- Generate with vertically-framed content centered in 16:9
- Check subject is centered and tight before cropping
- Crop to 9:16 in editing software

---

## Character Consistency {#character-consistency}

### The Professional Method: Custom AI Models

**For projects requiring perfect character consistency across 20+ scenes**

**Step 1: Create Character Dataset**
1. Start with one high-quality character image
2. Use VEO 3 "Frames to Video" with prompt: "turns and looks around"
3. Extract 10+ screenshots using Frame Extractor
4. Save multiple angles: front, side, 3/4 view

**Step 2: Train Custom Model (OpenArt)**
1. Upload dataset to OpenArt Characters feature
2. Name your character (e.g., "Marcus")
3. Train model (~10 minutes)
4. Generate unlimited consistent images

**Step 3: Generate Videos with Consistency**
- Use custom model images as video starting frames
- Keep character description identical across all prompts
- Structure: `[CONSISTENT CHARACTER DESC] + [NEW ACTION] + [NEW BACKGROUND]`

**Step 4: Voice Consistency (11 Labs)**
- Export audio from VEO 3 videos
- Use 11 Labs Voice Changer for consistent character voice
- Replace inconsistent VEO 3 audio with unified voice

### Quick Character Consistency (No Training)

**Claude Character Split Method**:
1. Generate full scene prompt
2. Ask Claude: "Split the prompt into character and action"
3. Result: Reusable character description + variable actions
4. Use same character desc for all scenes, change only actions

### Character Consistency Template

**Create once, copy exactly into every scene**:

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

**Critical**: Never deviate from core details across scenes!

---

## Photorealistic Character Creation {#photorealistic-characters}

### The Imperfection Principle

**Critical Rule**: AI defaults to unrealistic perfection. True realism requires **intentional imperfections**.

❌ **What AI Defaults To**: Ultra-realistic texture overload, perfect skin, flawless hair
✅ **What Looks Real**: Scars, pores, stray hairs, uneven skin tone, natural asymmetry

### Essential Character Details

**Use Claude Code Bot with this structure**:
```
I need a detailed character description for VEO 3. Ask me questions about:
1. Age, gender, ethnicity, facial features, body type
2. Skin imperfections: pores, sweat, oil, dirt, marks, cuts, scars, acne
3. Eye details: color, tints, eyelid position, wrinkles, crow's feet
4. Mouth/lips: condition, dryness, texture, natural asymmetry
5. Hair: thin/thick, color, cleanliness, messiness, stray strands
6. Emotional tone and facial expression
7. Clothing: texture, material, style, wear patterns, imperfections
8. Defining human traits that make them unique

Then provide a comprehensive VEO 3 prompt paragraph.
```

### Critical Focus Areas (Where Humans Look)

**1. Eyes (Primary Human Focus)**
- Specify: color, subtle tints, eyelid positions
- Include: surrounding wrinkles, crow's feet, under-eye texture
- Rule: "If an eye looks off, the entire image feels off"

**2. Mouth & Lips (Dialogue Authenticity)**
- Detail: lip condition, dryness, texture, natural asymmetry
- Critical during: any scene with dialogue or speaking
- Rule: Viewers watch mouths during dialogue to verify authenticity

**3. Skin Texture (Realism Foundation)**
- Always include: visible pores, sweat, oil, dirt
- Add imperfections: marks, cuts, uneven tone
- Avoid: AI's default "perfect skin" which looks fake

**4. Hair (The Detail Differentiator)**
- Specify: thin/thick quality, exact color, messiness level
- Always add: stray strands even in "clean" hairstyles
- Prevents: AI's polished, unrealistic hair defaults

### Advanced Lighting for Realism

**Lighting Specification Structure**:
```
[Natural/Artificial] + [Quality: hard/soft] + [Direction] + 
[Shadow type] + [Motivation] + [Exposure ratio]
```

**Exposure Ratios for Cinematic Look**:
- **2:1 or 4:1**: Soft contrast, professional look (RECOMMENDED)
- **1:1**: Flat lighting, no shadows (avoid)
- **32:1**: Harsh contrast, dramatic shadows (use sparingly)

**Example**:
```
"Soft natural lighting from window left, creating 2:1 exposure ratio with 
gentle shadows, motivated by golden hour sun"
```

### Atmospheric Realism Elements

**Add Light Interaction Physics**:
- Dust particles in light beams
- Atmospheric haze or mist
- Heat wave distortion (outdoor scenes)
- Volumetric god rays through windows

**Why It Works**: Shows how light interacts with environment, adding depth and authenticity

### Camera Technical Specifications

**Frame Rate & Settings**:
- Shutter speed: "1/50 for natural motion blur"
- ISO: "ISO 800 for slight grain" (adds texture)
- Depth of field: "Shallow DOF at F2.8" or "Deep focus at F16"

**Lens Character**:
- Vintage lenses: "Vintage Helios lens character"
- Telephoto: "85mm telephoto compression"
- Anamorphic: "Anamorphic lens flares and bokeh"
- Mobile aesthetic: "iPhone 15 Pro Max handheld footage"

**Aperture Guide**:
- **F1.4**: Maximum bokeh, extreme blur
- **F2.8-F4**: Balanced cinematic look (RECOMMENDED)
- **F8-F11**: Sharp environmental detail
- **F16-F22**: Everything in focus (landscapes)

### Color Palette Control (60-30-10 Rule)

**Professional Color Distribution**:
- **60%**: Dominant color (background, main environment)
- **30%**: Secondary color (supporting elements)
- **10%**: Accent pops (highlights, key details)

**Example**:
```
"Color palette: 60% muted blue-gray tones, 30% warm amber lighting, 
10% vibrant red accent on subject's jacket"
```

---

## Commercial-Quality JSON Prompting {#json-prompting}

### Why JSON Prompting Works

**The Core Principle**: JSON transforms vague ideas into precise production briefs.

❌ **What Most People Do**: "A forest at sunset" (hoping for cinematic results)
✅ **What Professionals Do**: Complete production specification with exact technical details

**The Reality**:
- Most AI video failures come from **inadequate prompting**, not AI limitations
- VEO 3 understands camera movement, lighting, sound design, and storytelling
- **If you're getting mid results, it's your prompt, not the model**

### JSON = Production Brief

**Think Like a Director**:
- You're not describing a video—you're **designing an experience**
- JSON provides the complete production brief a film crew would need
- Specificity = The difference between amateur and professional results

**What JSON Controls**:
- Lighting style and motivation
- Camera angles, movements, speeds
- Scene composition and framing
- Motion details and timing
- Audio textures and ambience
- Emotional tone and atmosphere
- Product/subject presentation details

### Master JSON Template

```json
{
  "description": "[One-sentence scene summary with key transformation]",
  "style": "[Specific aesthetic - 'Apple minimalist' not 'modern']",
  "camera": {
    "movement": "[Specific action with speed]",
    "angles": ["[Angle 1 with emotional purpose]", "[Angle 2]"],
    "lens": "[Lens type - '85mm macro' not 'close-up']"
  },
  "lighting": {
    "quality": "[Hard/soft with direction]",
    "mood": "[Emotional result of lighting]",
    "ratio": "[2:1 or 4:1 exposure ratio]"
  },
  "subject": {
    "materials": "[Specific materials with conditions]",
    "physics": "[How subject behaves, not just appears]",
    "transformation": "[Step-by-step if applicable]"
  },
  "environment": {
    "setting": "[Specific location or style]",
    "atmosphere": "[Environmental effects - dust, mist, haze]",
    "background": "[Level of detail and focus]"
  },
  "motion": {
    "speed": "[Slow motion / time-lapse / real-time]",
    "sequence": ["[Action 1]", "[Action 2]", "[Action 3]"]
  },
  "audio": {
    "music": "[Style and emotional arc]",
    "sfx": ["[Specific sound 1]", "[Sound 2]"],
    "ambient": "[Environmental audio layer]"
  },
  "color_palette": "[60% dominant + 30% secondary + 10% accent]",
  "emotional_tone": "[What viewer should feel]",
  "keywords": ["[Production term 1]", "[Term 2]"]
}
```

### JSON vs Paragraph Prompting

| Aspect | JSON Prompting | Paragraph Prompting |
|--------|---------------|---------------------|
| **Best For** | Commercial work, precise control | General content, quick generation |
| **Precision** | Extremely high - production brief level | Moderate - creative description |
| **Learning Curve** | Steeper - requires production knowledge | Easier - natural language |
| **Output Quality** | $100K commercial look | Professional but less controlled |
| **Use Case** | Client work, brand content, advertising | Social media, personal projects |
| **VEO 3 Response** | Responds like receiving director's brief | Interprets creative description |
| **Recommended For** | When every detail matters | 90% of everyday video creation |

### When to Use JSON

**Use JSON for**:
- Commercial/advertising content
- Brand campaigns
- Client deliverables
- Product showcases
- Multiple characters interacting
- Complex camera movements
- Precise lighting requirements
- Detailed audio specifications

**Use Paragraph Prompts for**:
- Social media content
- Personal projects
- Quick generations
- Simple single-character scenes
- Testing iterations

---

## 23 Proven Examples {#proven-examples}

### Quick Reference: Top Performing Prompts

**1. Pen Writing Plants** (Macro Magic)
```
A sleek emerald-green glass fountain pen with gold trim glides slowly 
across crisp parchment, but instead of ink, lush green vines, tiny leaves, 
and blooming flowers sprout instantly from the tip, curling and weaving 
across the page. Background is a warm wooden desk bathed in soft morning 
sunlight, with drifting dust particles in the air. Ultra-detailed macro 
shot, cinematic lighting, shallow depth of field.
```

**2. Coffee Beans Bloom** (ASMR Excellence)
```json
{
  "capture_method": "super slow motion",
  "sequence_breakdown": [
    "water drop lands",
    "drop deforms and is absorbed",
    "CO2 gas releases",
    "bubbles form, swell, and burst",
    "grounds push outward in fractal pattern"
  ],
  "audio_asmr": "crisp micro-phonic 'plink', sustained 'sizzle', gentle 'pop'"
}
```

**3. Nike Running Campaign** (Kinetic Energy)
```json
{
  "camera_progression": "wide landscape → low-angle tracking → high-angle logo reveal",
  "transformation_sequence": "kinetic ripples → motion lines → logo → product",
  "exposure_ratio": "backlit sunset with long directional shadows",
  "frame_rate": "60fps"
}
```

**See full collection of 23 prompts in original documentation**

### Universal Success Patterns

**1. Material Specificity**
- ❌ "A pen" → ✅ "Emerald-green glass fountain pen with gold trim"
- ❌ "Coffee" → ✅ "Coarse grounds with rich range of brown colors"

**2. Audio as Equal Partner**
- Every successful prompt includes audio specification
- ASMR prompts: Micro-sounds at precise moments
- Commercial prompts: Music style + SFX + ambient

**3. Camera as Storyteller**
- Wide → Close-up: Build context then focus
- Low angle: Power, dominance
- High angle: Scale, vulnerability
- Fixed: Let action dominate

**4. Physics Awareness**
- Describe how things *behave*, not just *appear*
- "Spines shimmer with brine droplets"
- "Coffee bloom triggers as CO2 releases"

**5. Step-by-Step Sequences**
- Complex transformations broken into clear steps
- VEO handles sequences when given clear progression

---

## Camera Angles & Storytelling {#camera-storytelling}

### Angles Convey Meaning

**Low Angles** (Camera looking up):
- Suggests: Power, dominance, importance
- Use for: Hero shots, authority figures, moments of triumph
- Example: "Low angle shot looking up at subject, conveying strength"

**High Angles** (Camera looking down):
- Suggests: Vulnerability, weakness, insignificance
- Use for: Defeated moments, showing scale, isolation
- Example: "High angle looking down, emphasizing smallness"

**Eye-Level Angles**:
- Suggests: Equality, neutrality, documentary realism
- Use for: Conversations, relatable moments, natural scenes
- Example: "Eye-level shot creating intimate connection"

**Dutch Angles** (Tilted):
- Suggests: Unease, chaos, disorientation
- Use for: Tension, psychological distress, action
- Example: "Dutch angle with 15-degree tilt creating tension"

### Compositional Techniques

**Rule of Thirds**:
- Place subject on intersection points
- "Subject positioned on right third line, balanced composition"

**Centered Symmetry** (Wes Anderson Style):
- Perfect center framing with symmetrical elements
- "Wes Anderson-style centered symmetrical composition"

**Leading Lines**:
- Use environmental elements to guide eye
- "Leading lines from road converging toward subject"

---

## Workflow Optimization {#workflow-optimization}

### The Paradigm Shift

**Old Way**: Need expensive equipment, technical crew, production expertise
**New Way**: Need production knowledge + ability to communicate with AI

**Critical Understanding**:
- AI video represents shift from **technical skill** to **communicative clarity**
- You don't need equipment anymore—you need **knowledge of production concepts**
- The gap between amateur and professional = **prompt specificity**

### Pre-Production
1. **Write detailed prompts** → Reduces failed generations
2. **Use Claude template** for general content → Saves time
3. **Use JSON for commercial work** → Production brief precision
4. **Plan shot sequence** → Clear vision before generating
5. **Study professional commercials** → Learn what to specify

### Production
1. **Generate in batches** → More efficient workflow
2. **Test variations** → Create multiple takes, pick best
3. **Track successful prompts** → Build reusable library
4. **Think in production terms** → Lighting ratios, camera specs

### Post-Production
1. **Upscale to 4K** → Non-negotiable for quality
2. **Replace audio if needed** → Use 11 Labs for consistency
3. **Edit for flow** → Stitch clips with transitions
4. **Add film grain + chromatic aberration** → Disguise AI origins

---

## Cost Optimization {#cost-optimization}

### API/Programmatic Access
- **Kie.ai**: $1.50 (quality) / $0.38 (fast) - 75% cheaper
- **Features**: Native 9:16, fallback protection, auto-translation
- **Best for**: High-volume production, vertical content

### Credit Saving Strategies
1. Write detailed prompts first (fewer regenerations)
2. Use Fast mode for tests, Quality for finals
3. Generate multiple short clips vs one long video
4. Leverage Claude Code subagent for prompt optimization

### Production Costs

**Single Scene (8s)**:
- veo3_fast: $0.38
- veo3: $1.50

**6-Scene Campaign (48s)**:
- All veo3_fast: ~$2.30
- Mixed (5 fast + 1 quality): ~$3.40
- All veo3: ~$9.00

**Recommendation**: Use veo3_fast for 90% of scenes, veo3 for hero shots only

---

## Troubleshooting Guide {#troubleshooting}

### Common Issues & Solutions

**Issue**: Character appearance changes between scenes
**Cause**: Inconsistent character description across prompts
**Solution**:
- Create master character template
- Copy EXACT description into every scene
- Never paraphrase or "improve" details
- Use distinctive features as anchors
- **CRITICAL**: Ensure ending frames show character's face clearly

**Issue**: Character consistency broken in continuation
**Cause**: Previous ending frame didn't show face
**Solution**:
- Always end scenes with face visible (3/4 profile minimum)
- Plan ahead: If character turns away, ensure they turn back
- Include in prompt: "ending with character's face visible"
- Check ending frame before moving to next scene

**Issue**: Actions feel rushed or incomplete
**Cause**: Too much action crammed into 8 seconds
**Solution**:
- Focus on ONE clear action per scene
- Use "At X seconds" timestamps
- Max 4 distinct 2-second steps serving one action
- Add additional scenes if needed for pacing

**Issue**: Scene N+1 doesn't match Scene N ending
**Cause**: Prompt doesn't accurately describe ending frame state
**Solution**:
- Review ending frame carefully before writing next prompt
- Copy exact pose/position description
- Ensure lighting description matches
- Use image-to-video with uploaded frame

**Issue**: Lighting jumps dramatically between scenes
**Cause**: Unrealistic lighting progression
**Solution**:
- Plan natural time progression upfront
- Use transition scenes for major changes
- Keep lighting direction consistent
- Establish environmental aesthetics at transition point

**Issue**: Props/products don't match real branding
**Cause**: AI invents generic versions
**Solution**:
- Keep product visible throughout all scenes
- Plan for post-production compositing
- Generate with generic descriptions
- Replace AI products with real photography

**Issue**: Environmental elements disappear (trees, buildings)
**Cause**: Not explicitly stated to remain constant
**Solution**:
- State what must remain: "oak tree remains visible throughout"
- Specify changes affect appearance, not existence
- Use fixed camera positions for consistency
- Repeat key elements at each time point

---

## Quick Reference Checklist

### Before Generating:
- [ ] Prompt includes all 10 components
- [ ] Negative instructions included
- [ ] Character imperfections specified (pores, stray hair, skin texture)
- [ ] Lighting exposure ratio defined (2:1 or 4:1 recommended)
- [ ] Atmospheric elements added (dust, haze, mist)
- [ ] Camera angle chosen for story meaning
- [ ] Lens character specified
- [ ] Aperture setting included (F2.8-F4 for cinematic)
- [ ] Color palette follows 60-30-10 rule
- [ ] Time of day specified
- [ ] Camera movement detailed
- [ ] Audio description added
- [ ] Continuous paragraph format (no bullets)

### For Multi-Scene Projects:
- [ ] Story broken into 8-second beats
- [ ] One action per scene identified
- [ ] Character consistency template created
- [ ] Ending frames planned with face visible
- [ ] Scene 1 establishes all character/environment details
- [ ] Transition scenes planned for major changes
- [ ] Product visibility maintained throughout
- [ ] Environmental transition descriptions written
- [ ] Lighting progression mapped naturally

### Settings:
- [ ] Resolution: Highest available
- [ ] Mode: Fast for tests, Quality for finals
- [ ] Audio: Enabled (if needed)
- [ ] Aspect ratio: Match intended platform
- [ ] First frame: Upload previous ending frame (if continuation)

### After Generation:
- [ ] Upscale to 4K using OpenArt
- [ ] Extract last frame for next scene
- [ ] Verify character face visible in ending frame
- [ ] Check continuity with previous scene
- [ ] Replace audio with 11 Labs (if needed for character voice)
- [ ] Add film grain (disguises AI origins)
- [ ] Add chromatic aberration (lens imperfection)
- [ ] Trim transition jumps (if needed)
- [ ] Crop/adjust for vertical (if social media)
- [ ] Save successful prompts for reuse

---

## The Bottom Line

**Success Formula = Detailed Prompts + Intentional Imperfections + Frame Continuity + Always Upscale**

### Core Principles Summary:

1. **Use Claude template** for automatic prompt optimization (general content)
2. **Use JSON prompting** for commercial/professional work (precise control)
3. **Add intentional imperfections** (AI defaults to fake perfection)
4. **Specify exposure ratios** (2:1 or 4:1 for cinematic look)
5. **Include atmospheric elements** (dust, haze, light interaction)
6. **Define camera angles** for story meaning
7. **Never skip negative instructions**
8. **Test with veo3_fast** before veo3
9. **Always upscale to 4K**
10. **Plan frame-to-frame continuity** for long videos

### When to Use Which Method:

**📝 Paragraph Prompts (Claude Template)**:
- Social media content
- Personal projects
- Quick generations
- Simple scenes
- 90% of your use cases

**📊 JSON Prompts (Structured)**:
- Commercial/advertising content
- Brand campaigns
- Client deliverables
- Product showcases
- Precise control requirements

**🎬 Frame-to-Frame Workflow**:
- Long-form content (30+ seconds)
- Narrative storytelling
- Character-driven scenes
- Sequential action sequences
- Professional seamless flow

### Remember:

**"We don't want it perfect. We want it real."**

True photorealism comes from intentional imperfections. Focus on eyes, mouths, skin texture, and hair—these are where humans detect artificial content.

**For Longer Videos**: Use frame-to-frame continuation. Extract last frame with face clearly visible. Use as starting image for next scene with 85% identical prompt.

**VEO 3 Maximum**: 8 seconds per clip (cannot be extended). Plan accordingly.

---

## Additional Resources

- **VEO 3 API Docs**: https://docs.kie.ai/veo3-api
- **Kie.ai Dashboard**: https://kie.ai/dashboard
- **File Upload API**: https://docs.kie.ai/file-upload-api/upload-file-base-64
- **OpenArt Platform**: https://openart.ai
- **Universal Clients**: Check project scripts for automation

---

*VEO 3 rewards detailed, cinematic prompts with technical camera specs. The more specific you are about imperfections, lighting ratios, atmospheric elements, and frame-to-frame continuity, the more realistic and professional your results will be.*

*Last Updated: September 30, 2025*
