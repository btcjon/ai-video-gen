# VEO 3 Essential Mastery Guide: The Only Tips You Need

## Quick Start: The Foundation

### Platform Access
- **Primary**: OpenArt platform → Video → Text → Select "Google VEO 3"
- **Alternative**: Search "VEO 3" on Google → First result → "Try in Gemini"
- **Cost Optimization**: Kie.ai API (75% cheaper for programmatic access)

### Critical Settings
- ✅ **Resolution**: Highest available (1080p) → Always upscale to 4K
- ✅ **Mode**: Normal/Quality (never Fast mode - quality difference too significant)
- ✅ **Audio**: Enable for dialogue/sound, disable for silent content

---

## The Ultimate Prompt Formula

### 10 Essential Components (Use ALL of These)

```
[1. SCENE SETUP] + [2. SUBJECT DESCRIPTION] + [3. BACKGROUND] + 
[4. ACTION] + [5. VIDEO STYLE] + [6. CAMERA SETTINGS] + 
[7. COMPOSITION] + [8. LIGHTING & MOOD] + [9. AUDIO] + 
[10. NEGATIVE INSTRUCTIONS]
```

### Claude Auto-Prompt Template (Copy & Use)

```
Expand it into a full Veo 3 prompt using this structure: 

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

Expand it into a full Veo 3 prompt, but write it as one continuous cinematic paragraph (not bullet points, no section labels).

[YOUR SIMPLE IDEA HERE]
```

**Key**: Replace `[YOUR SIMPLE IDEA HERE]` with your concept and get a perfect VEO 3 prompt every time.

---

## Critical Success Principles

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

---

## Vertical Video (Social Media) Mastery

### The Working Formula for 9:16 Content

```
A close-up vertically framed portrait video of [SUBJECT] standing in the center 
of the frame, captured in vertical mode, cinematic lighting, sharp focus, 
shallow depth of field, 9:16 aspect ratio. [SUBJECT ACTION]. Optimized for 
[PLATFORM] with [ENERGY LEVEL] energy and mobile-optimized composition.
```

### Platform-Specific Optimizations

**TikTok**:
- High energy, dynamic movement
- "Trending viral style with engaging visuals"
- Centered composition with clear subject

**Instagram Reels**:
- Polished aesthetic, premium feel
- "Instagram-worthy framing with visual appeal"
- Smooth progression throughout

**YouTube Shorts**:
- Clear narrative, informative
- "Educational-friendly with good readability"
- Balanced energy, clear visual hierarchy

### ⚠️ Post-Production Reality
- VEO 3 outputs 16:9 by default (even with vertical prompts)
- Solution: Create vertically-framed content within 16:9, then crop in editing
- Check if subject is centered and tight before cropping

---

## Character Consistency for Long Videos

### The Professional Method: Custom AI Models

**Step 1: Create Character Dataset**
1. Start with one high-quality character image
2. Use VEO 3 "Frames to Video" with prompt: "turns and looks around"
3. Extract 10+ screenshots using Frame Extractor tool
4. Save multiple angles: front, side, 3/4 view

**Step 2: Train Custom Model (OpenArt)**
1. Upload dataset to OpenArt Characters feature
2. Name your character (e.g., "Marcus")
3. Train model (~10 minutes)
4. Generate unlimited consistent images

**Step 3: Generate Videos with Consistency**
- Use custom model images as video starting frames
- Keep character description identical across all prompts
- Example structure: `[CONSISTENT CHARACTER DESC] + [NEW ACTION] + [NEW BACKGROUND]`

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

---

## Creating Longer Videos: Scene Continuation Technique

### The 8-Second Problem

**VEO 3 Limitation**: Maximum 8-second clips  
**Solution**: Frame-to-video continuation for seamless longer content

### The Frame Continuation Method

**Core Principle**: Use the last frame of Scene 1 as the starting image for Scene 2

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
  "prompt": "45-year-old father with salt-and-pepper hair checking emergency supplies in dimly lit garage, worried expression, wearing gray t-shirt, cinematic lighting with 2:1 ratio, handheld camera, shallow depth of field"
}
```

**Step 2: Extract Last Frame**
- Download completed video
- Extract final frame as PNG/JPG
- Save as starting point for next scene

**Step 3: Generate Continuation (85% Same)**
```json
{
  "scene": "Scene 2 - Continuation",
  "starting_image": "scene1_last_frame.png",
  "prompt": "45-year-old father with salt-and-pepper hair finding water bottle among emergency supplies in dimly lit garage, relieved expression, wearing gray t-shirt, cinematic lighting with 2:1 ratio, handheld camera, shallow depth of field"
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

**Expect 1-2 Second "Jump"**:
- Generate 10-second clips when possible
- Use middle 8 seconds in editing
- Trim awkward transition frames
- Add subtle crossfade if needed (0.5s)

**Pro Tip**: Generate slightly longer than needed, trim to smoothest section

### Practical Example: Product Commercial

**Traditional Approach (Disconnected)**:
- 4 separate scenes × 8s = 32 seconds
- Different angles, inconsistent look
- Character appearance varies

**Continuous Approach (Professional)**:
```
Scene 1a (0-8s):   Man at window watching crisis unfold
Scene 1b (8-16s):  [FROM 1a] Man turning to check supplies
Scene 2a (16-24s): [FROM 1b] Man in garage discovering problem
Scene 2b (24-32s): [FROM 2a] Man finding product solution
Scene 3a (32-40s): [NEW SHOT] Hands demonstrating product
Scene 3b (40-48s): [FROM 3a] Product working, water clearing
Scene 4a (48-56s): [NEW SHOT] Family gathering with product
Scene 4b (56-64s): [FROM 4a] Family satisfied, drinking water
```

**Result**: 64 seconds of seamless narrative vs 32 seconds of disconnected clips

### When to Start Fresh vs Continue

**Use Frame Continuation When**:
- ✅ Same character in same location
- ✅ Sequential action/story beat
- ✅ Maintaining emotional continuity
- ✅ Same time of day/lighting

**Start Fresh When**:
- ✅ Location change (garage → kitchen)
- ✅ Time jump (day → night)
- ✅ Different character/angle needed
- ✅ Major scene transition

### Technical Implementation

**With Image-to-Video Feature**:
```
1. Generate Scene 1 normally
2. Download video when complete
3. Extract last frame (use video editor or:
   ffmpeg -sseof -1 -i video.mp4 -frames:v 1 last_frame.png)
4. Upload last_frame.png as starting image
5. Use 85% same prompt with 15% action change
6. Generate Scene 2
```

**Claude Code Prompt for Continuation**:
```
I have this scene prompt:
[PASTE SCENE 1 PROMPT]

Create a continuation prompt that:
- Keeps 85% identical (character, environment, lighting, camera)
- Changes only the action to: [NEW ACTION]
- Maintains exact same character description
- Preserves lighting and mood
```

### Cost Optimization

**Standard Approach**: 4 scenes × $0.38 = $1.52 (32 seconds)  
**Continuous Approach**: 8 segments × $0.38 = $3.04 (64 seconds)

**Value**: 2× length, professional flow, seamless narrative = Worth the investment

### Common Issues & Solutions

**Issue**: Character looks different in continuation  
**Solution**: Copy/paste exact character description, use last frame as starting image

**Issue**: Lighting/environment changes  
**Solution**: Include specific lighting details in both prompts identically

**Issue**: Jumpy transitions even with continuation  
**Solution**: Generate 10s clips, trim first/last seconds where jump occurs

**Issue**: Lost track of prompt variations  
**Solution**: Document each scene with exact prompt used, build template library

### Quick Implementation Checklist

Before starting scene continuation:
- [ ] Break story into 8-second beats
- [ ] Identify which scenes need continuation
- [ ] Write Scene 1 with complete character/environment details
- [ ] Generate Scene 1 and extract last frame
- [ ] Copy Scene 1 prompt, change only action (15%)
- [ ] Use last frame as starting image for Scene 2
- [ ] Test with veo3_fast first (20 credits)
- [ ] Plan for 1-2 second transition trimming in post

### Pro Tips for Seamless Continuations

1. **Action Continuity**: End Scene 1 mid-movement, continue that movement in Scene 2
2. **Eye-Line Match**: Keep character looking same direction between scenes
3. **Audio Bridge**: Use consistent ambient sound to mask visual transitions
4. **Micro-Movements**: Small actions (turning head, reaching) work better for continuations
5. **Safety Overlap**: Generate slight action overlap to give editing flexibility

---

## Photorealistic Character Creation

### The Imperfection Principle

**Critical Rule**: AI defaults to unrealistic perfection. True realism requires **intentional imperfections**.

❌ **What AI Defaults To**: Ultra-realistic texture overload, perfect skin, flawless hair  
✅ **What Looks Real**: Scars, pores, stray hairs, uneven skin tone, natural asymmetry

### Essential Character Details (Use Claude Code Bot)

**Create a Claude Code subagent with this prompt structure**:
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
"Soft natural lighting from window left, creating 2:1 exposure ratio with gentle shadows, motivated by golden hour sun"

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

**Example**: "Color palette: 60% muted blue-gray tones, 30% warm amber lighting, 10% vibrant red accent on subject's jacket"

### Advanced Prompting with Claude Code

**Step 1: Image Analysis (Upload existing reference)**
```
Analyze this image using JSON breakdown. Identify:
- Character details and imperfections
- Lighting setup and exposure ratio
- Color palette distribution (60-30-10)
- Camera settings and lens character
- Atmospheric elements present

Then enhance the prompt for better realism.
```

**Step 2: Enhanced Generation**
Claude Code will provide improved prompt with specific imperfections and technical details

---

## Commercial-Quality Videos (Use JSON Prompting)

### Why JSON Prompting Works

**The Core Principle**: JSON transforms vague ideas into precise production briefs.

❌ **What Most People Do**: "A forest at sunset" (hoping for cinematic results)  
✅ **What Professionals Do**: "Give me a drone shot of misty pine forest at golden hour, 2:1 exposure ratio, slow ascending movement, volumetric god rays, ambient forest sounds"

**The Reality**: 
- Most AI video failures come from **inadequate prompting**, not AI limitations
- VEO 3 understands camera movement, lighting, sound design, and storytelling—you just need to speak its language
- **If you're getting mid results, it's your prompt, not the model**

### JSON = Production Brief (Not Rough Ideas)

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

### JSON Prompt Structure (Professional Ads)

```json
{
  "description": "[Brand] product formation from raw elements",
  "style": "cinematic realistic commercial",
  "camera": {
    "movement": "slow tracking shot across assembly process",
    "angles": ["macro close-ups", "wide establishing shots"]
  },
  "lighting": "dramatic studio lighting with focused spotlights",
  "environment": "minimal dark studio background",
  "elements": {
    "materials": ["component 1", "component 2", "component 3"],
    "assembly": "materials form into final product"
  },
  "motion": "smooth transformation sequence",
  "ending": "completed product with brand logo reveal",
  "text": "[Brand Tagline]",
  "keywords": ["precision", "craftsmanship", "innovation"]
}
```

### Real-World JSON Examples

**1. Beverage Ad (Luxury Coffee)**
```json
{
  "description": "Premium coffee being poured into glass mug",
  "style": "Starbucks luxury commercial aesthetic",
  "camera": {
    "movement": "slow dolly in from medium to close-up",
    "angles": ["side angle at 45 degrees", "focus on steam rising"]
  },
  "lighting": "soft golden hour lighting with 2:1 ratio, backlit steam",
  "environment": "minimal café background with bokeh depth of field",
  "liquid_dynamics": "rich dark coffee with visible texture, steam rising",
  "motion": "smooth pour in slow motion",
  "audio": "gentle pour sounds, ambient café atmosphere, subtle music",
  "emotional_tone": "warmth, comfort, luxury morning ritual"
}
```

**2. Tech Product Reveal (Apple Style)**
```json
{
  "description": "Smartphone rotating on pedestal with dramatic reveal",
  "style": "Apple commercial aesthetic, minimalist and premium",
  "camera": {
    "movement": "slow 360-degree rotation around product",
    "angles": ["eye-level close-up", "dramatic low angle finish"]
  },
  "lighting": "dramatic studio spotlights with edge lighting, deep blacks",
  "environment": "pure black background, floating in space aesthetic",
  "product_details": "phone slowly rotating, screen glowing, metallic edges catching light",
  "motion": "smooth rotation over 6 seconds with pause at hero angle",
  "audio": "subtle electronic ambience, futuristic tones, silence for impact",
  "timing": "build anticipation, hold on hero shot at end"
}
```

**3. Fashion Lookbook**
```json
{
  "description": "Model showcasing streetwear in urban environment",
  "style": "editorial fashion film with gritty urban vibe",
  "camera": {
    "movement": "handheld follow shot, organic movement",
    "angles": ["medium shot to full body", "dynamic angles"]
  },
  "lighting": "natural golden hour with urban shadows, 4:1 ratio",
  "environment": "industrial urban setting, graffiti walls, concrete textures",
  "wardrobe_details": "oversized jacket, distressed denim, statement accessories",
  "motion": "confident walking, natural gestures, attitude-driven movement",
  "audio": "urban ambient sounds, subtle hip-hop beat, street atmosphere",
  "editorial_vibe": "confident, stylish, authentic street culture"
}
```

**4. Creator Intro (Personal Brand)**
```json
{
  "description": "Content creator introducing themselves in home studio",
  "style": "professional yet authentic YouTube creator aesthetic",
  "camera": {
    "movement": "static medium shot, slight push in for emphasis",
    "angles": ["eye-level, centered composition for connection"]
  },
  "lighting": "three-point lighting setup, soft key light, rim light separation",
  "environment": "clean studio background with subtle props showing personality",
  "subject_details": "friendly expression, natural gestures, welcoming presence",
  "motion": "subtle hand gestures, authentic body language, confident posture",
  "audio": "clear voice, warm tone, professional studio sound",
  "personality_traits": "approachable, knowledgeable, authentic, energetic"
}
```

**5. Epic Travel/Drone Sequence**
```json
{
  "description": "Breathtaking mountain landscape with dramatic drone movement",
  "style": "cinematic travel commercial with epic scale",
  "camera": {
    "movement": "ascending drone shot starting low, rising to reveal landscape",
    "altitude": "start at 20 feet, rise to 200 feet over 8 seconds",
    "angles": ["low angle climb to overhead establishing shot"]
  },
  "lighting": "golden hour with dramatic god rays through mountain peaks",
  "environment": "misty pine forest, mountain peaks, vast landscape",
  "atmospheric_conditions": "morning mist in valleys, volumetric light beams",
  "motion": "slow deliberate ascent revealing landscape scale progressively",
  "audio": "ambient wind, distant nature sounds, subtle epic score building",
  "emotional_tone": "awe, wonder, adventure, majestic scale"
}
```

### Three-Step Claude Code Workflow for JSON

**Step 1: Generate Optimized Concept**
```
Create a commercial ad concept for [BRAND] featuring [PRODUCT] with [CONCEPT]. 
Think like a creative director planning a $100,000 commercial.
Include all production details: lighting, camera, motion, audio, atmosphere.
```

**Step 2: Convert to JSON Structure**
```
Convert this commercial concept into JSON prompt format with these fields:
- description (overview of the scene)
- style (specific commercial aesthetic - be exact: "Apple minimalist" or "Nike high-energy")
- camera (movement types, angles, specific technical specs)
- lighting (setup, ratios, motivation, quality)
- environment (setting details, atmosphere, background)
- [product-specific] (liquid_dynamics, wardrobe_details, product_details, etc.)
- motion (specific movements, timing, speed)
- audio (sounds, music, ambience - be specific)
- emotional_tone (what should the viewer feel?)
- timing (if specific beats or pacing matter)

Make it detailed like a real production brief.
```

**Step 3: Feed to VEO 3**
Copy the JSON structure directly into VEO 3 prompt field. The structured format gives VEO 3 the complete production blueprint it needs.

### JSON Template Strategy

**The Power of Templates**:
- Create once, reuse infinitely with modifications
- Swap products, styles, settings while keeping structure
- Build a library of proven templates for different use cases

**Template Customization**:
```json
// Base Template: Product Reveal
{
  "description": "[SWAP PRODUCT] floating on dark background",
  "style": "[SWAP BRAND AESTHETIC] commercial style",
  "camera": {
    "movement": "[KEEP OR MODIFY] slow rotation",
    "angles": "[ADJUST AS NEEDED] dramatic angles"
  },
  // ... rest of structure remains consistent
}
```

---

## 12 Proven JSON Examples (Copy & Customize)

### Product Reveals & Transformations

**1. Coffee Bloom (Hyper-Realistic ASMR)**
```json
{
  "description": "Hyper-realistic slow-motion macro video focusing on coffee bloom. Single drop of water falling onto freshly ground coffee.",
  "subject": {
    "main": "pristine glistening water drop",
    "coffee_details": "coarse grounds with rich range of brown colors"
  },
  "scene": {
    "lighting": "single dramatic spotlight creating deep shadows and intense highlights",
    "background": "minimalist out-of-focus blur of deep blacks and grays",
    "mood": "warm cinematic glow"
  },
  "action": {
    "capture_speed": "super slow motion",
    "sequence": [
      "water drop lands on coffee grounds",
      "coffee bloom effect triggers as CO2 releases",
      "tiny bubbles form, swell, and burst",
      "grounds push outward in fractal pattern"
    ]
  },
  "audio": {
    "primary_sounds": [
      "crisp micro-phonic 'plink' as drop hits",
      "sustained 'sizzle' and 'hiss' as gas releases",
      "gentle 'pop' as bubbles burst"
    ],
    "style": "highly detailed ASMR-like audio"
  },
  "camera": "static extreme close-up macro",
  "visual_style": "hyper-realistic commercial, high-resolution 4K"
}
```

**2. Pen Writing Plants (Creative Magic)**
```json
{
  "description": "Sleek emerald-green glass fountain pen with gold trim glides across crisp parchment, but instead of ink, lush green vines, tiny leaves, and blooming flowers sprout instantly from the tip, curling and weaving across the page.",
  "scene": {
    "location": "warm wooden desk",
    "lighting": "soft morning sunlight with drifting dust particles",
    "atmosphere": "serene, magical"
  },
  "camera": {
    "shot_type": "ultra-detailed macro shot",
    "depth_of_field": "shallow"
  },
  "visual_style": {
    "aesthetic": "cinematic photorealistic",
    "lighting_mood": "warm morning glow"
  },
  "motion": "pen glides slowly, vines sprout and curl organically",
  "keywords": ["macro cinematography", "botanical magic", "organic growth"]
}
```

**3. Nike Running Campaign (Kinetic Energy)**
```json
{
  "shot": {
    "composition": "wide landscape with centered runner → low-angle close tracking of feet → high-angle logo reveal morphing into product",
    "lens": "anamorphic for wide sweep, 50mm for footwork tracking",
    "frame_rate": "60fps",
    "camera_movement": "ground-level tracking, lateral sweep, final pullback from logo to sneaker"
  },
  "subject": {
    "description": "runner sprints across shifting terrain, movement generating energy trails that form Nike logo before crystallizing into product",
    "wardrobe": "sleek modern athletic wear in black and white"
  },
  "visual_details": {
    "action": "runner's feet strike releasing kinetic ripples; form dissolves into motion lines swirling upward into swoosh logo, pulsing and reassembling into pristine sneaker",
    "special_effects": "motion streak trails, slow-motion impacts, morphing energy particles, ripple crystallization"
  },
  "cinematography": {
    "lighting": "backlit sunset with long directional shadows, warm edge lighting",
    "color_palette": "deep blacks, soft whites, warm golds, electric silver accents",
    "tone": "epic, modern, kinetically poetic"
  },
  "audio": {
    "music": "percussive electronic with heartbeat tempo, evolving into orchestral hit at product reveal",
    "sound_effects": "impact thuds, trailing whooshes, logo crystallization chime"
  }
}
```

**4. L'Oréal Billboard (Reality-Bending)**
```json
{
  "description": "Surreal billboard in Times Square. Massive digital display shows beautiful woman's face—flawless and radiant. But her hair defies the screen, flowing beyond the billboard into the real world, swaying in actual wind as if breaking boundary between ad and reality.",
  "scene": {
    "location": "Times Square, New York City",
    "lighting": "neon reflections light up street below",
    "atmosphere": "surreal, boundary-breaking"
  },
  "visual_elements": {
    "billboard": "massive digital display with woman's face",
    "special_effect": "hair flows from screen into real world",
    "physics": "hair sways in actual wind",
    "branding": "iconic L'Oréal logo elegantly displayed"
  },
  "style": "surreal reality-bending commercial"
}
```

### Assembly & Unboxing Effects

**5. IKEA Flat Pack Assembly**
```json
{
  "description": "Cinematic shot of sunlit Scandinavian bedroom. Sealed IKEA box trembles, opens, and flat pack furniture assembles rapidly into serene styled room highlighted by yellow IKEA throw on bed. No text.",
  "style": "cinematic",
  "camera": "fixed wide angle",
  "lighting": "natural warm with cool accents",
  "room": "Scandinavian bedroom",
  "elements": [
    "IKEA box (logo visible)",
    "bed with yellow throw",
    "bedside tables",
    "lamps",
    "wardrobe",
    "shelves",
    "mirror",
    "plants"
  ],
  "motion": "box opens, furniture assembles precisely and rapidly",
  "ending": "calm modern space with yellow IKEA accent",
  "keywords": ["16:9", "Scandinavian", "fast assembly", "warm & cool tones"]
}
```

**6. Louis Vuitton Embroidery**
```json
{
  "description": "Fixed wide-angle shot of dark velvet surface. Golden LV logo shimmers midair, begins to disassemble into thousands of tiny gold threads flowing downward like liquid embroidery. Threads weave into detailed Louis Vuitton handbag silhouette. Final stitch completes, bag rises gently, leather glowing, gold zipper glides open revealing soft interior glow.",
  "style": "cinematic, luxurious, elegant",
  "camera": "fixed wide angle",
  "lighting": "moody spotlight with warm golden highlights and gentle falloff",
  "environment": "black velvet tabletop with soft shadows and refined texture",
  "elements": [
    "gold LV monogram logo",
    "golden embroidery threads",
    "Louis Vuitton handbag silhouette",
    "glowing leather texture",
    "gold zipper movement",
    "interior light reveal"
  ],
  "motion": {
    "type": "logo-to-thread-to-object",
    "details": "LV logo dissolves into gold threads, threads form bag, bag opens"
  },
  "audio": {
    "music": "subtle cinematic string swell with harp accents",
    "sfx": "gentle thread weaving sounds, leather flexing, zipper slide"
  }
}
```

**7. Tesla Showroom Reveal**
```json
{
  "description": "Minimalist Tesla-branded crate magically opens revealing fully formed Tesla vehicle and instantly assembled sleek showroom around it.",
  "style": "cinematic futuristic",
  "camera": "fixed wide angle with subtle zooms on key transformations",
  "lighting": "controlled high-tech, transitioning from dim to bright and clean",
  "elements": [
    "Tesla-branded crate (glowing seams)",
    "Tesla vehicle (Model 3/Y/Cybertruck)",
    "charging station",
    "minimalist display panels",
    "sleek showroom furniture",
    "ambient lighting elements"
  ],
  "motion": "crate panels retract smoothly, car revealed, showroom elements rise/unfold precisely",
  "ending": "pristine inviting Tesla showroom with car as centerpiece",
  "keywords": ["Tesla", "magic assembly", "innovation", "clean design"]
}
```

### Mythical & Atmospheric

**8. Maserati: The Trident's Call**
```json
{
  "core_concept": "From ocean depths, Neptune's trident unleashes power, summoning vortex of water and light that forges Maserati MC20.",
  "action_sequence": [
    {"step": 1, "description": "Camera glides over seabed, discovers massive ancient bronze trident half-buried. Begins to glow with brilliant aquamarine light."},
    {"step": 2, "description": "Glowing trident unleashes power, creating massive swirling underwater vortex. Sand, bubbles, light pulled into powerful spin."},
    {"step": 3, "description": "Within vortex, chaotic currents hydro-dynamically sculpted into sleek Maserati MC20. Trident logo on grille materializes first. Water-form solidifies into metallic white."},
    {"step": 4, "description": "Car rockets upward, bursts through ocean surface in spectacular slow-motion explosion. Lands perfectly on wet black-sand beach at twilight."}
  ],
  "visual_style": {
    "aesthetic": "cinematic, hyper-realistic, elegant, mythical",
    "resolution": "8K",
    "lighting": "dark mysterious underwater with brilliant trident glow. Breach shot dramatic with soft twilight"
  },
  "camera_work": "slow exploratory glide. Circle glowing trident. Caught in vortex spinning. Follow rocket ascent, epic slow motion breach. End on low wide-angle beach shot"
}
```

**9. Sand Colosseum Formation**
```json
{
  "description": "Ultra-realistic cinematic macro shot. Laboratory setting with warm moody lighting. Single water droplet slowly falls from glass pipette onto cracked ancient clay surface inside petri dish. As droplet hits, ancient Roman stone bubbles up and rises, magically forming the Colosseum in exquisite detail.",
  "scene": {
    "location": "clean laboratory setting",
    "lighting": "warm moody lighting with dust particles and light rays",
    "background": "soft focus"
  },
  "action": {
    "sequence": [
      "water droplet falls from glass pipette",
      "droplet hits cracked clay surface",
      "ancient Roman stone bubbles up",
      "Colosseum structure forms in detail"
    ],
    "style": "timelapse-style organic growth, pieces assembling from inside outward"
  },
  "camera": "ultra-realistic cinematic macro, close and focused throughout",
  "audio": "slow orchestral soundtrack",
  "visual_style": "cinematic realism with magical elements"
}
```

**10. Corona Beach Rave (Environment Explosion)**
```json
{
  "description": "Cinematic close-up of cold dewy Corona bottle on weathered beach table. Begins to hum, vibrate. Bottle cap pops—entire environment unfolds from inside: palm trees rise, lights string themselves, speakers assemble mid-air, sand shifts into dance floor. DJ booth builds from driftwood. Beach rave is born.",
  "style": "cinematic, magical realism",
  "camera": "starts ultra close, zooms out and cranes overhead as world expands",
  "lighting": "sunset turning to neon—golden hour into party glow",
  "environment": "quiet beach → high-energy beach rave",
  "elements": [
    "Corona bottle (condensation dripping)",
    "pop-top cap in slow motion",
    "sand morphing into dance floor",
    "palm trees rising",
    "neon lights snapping on",
    "DJ booth building itself",
    "crowd materializing mid-dance",
    "fire pit lighting"
  ],
  "motion": "explosion of elements from bottle, rapid time-lapse assembly",
  "ending": "Corona bottle in foreground, beach rave in full swing behind"
}
```

### Character & ASMR

**11. Alien Spaceship Tour (Character Vlog)**
```json
{
  "scene_summary": "Excited alien frog creature gives walking tour of spaceship's drive room.",
  "character": {
    "type": "alien frog creature",
    "personality": ["expressive", "excited", "high energy"],
    "features": "expressive amphibian eyes, expressive mouth and face, fluid gestures",
    "accent": "gen z"
  },
  "environment": {
    "location": "spaceship drive room",
    "key_object": "glop perpetugooper - large machine emitting warm glow with glass cylinder filled with orange slime"
  },
  "action_sequence": [
    {
      "camera": "tracks as he walks left",
      "dialogue": "And if you're hungry and you want some za we got the glop perpetu-gooper",
      "gesture": "touches large machine"
    },
    {
      "dialogue": "You just think za and bloop!",
      "result": "floating pizza forms inside machine"
    },
    {
      "gesture": "glances at pizza, looks at camera with excitement",
      "dialogue": "Manifest your dinner bro!"
    }
  ],
  "visuals": {
    "lighting": ["diffuse studio lighting", "warm bounce from machine", "soft shadows"],
    "style": "soft cinematic color grading, tonemapped HDR"
  }
}
```

**12. ASMR Sea Urchin (Hyper-Focus)**
```json
{
  "shot": {
    "composition": "extreme close-up, 85mm macro lens, razor-thin depth of field",
    "camera_motion": "slow dolly-in from floor level, rising toward mouth as jaws part",
    "film_grain": "digital clean with iridescent chrome LUT"
  },
  "subject": {
    "description": "20-year-old Mediterranean girl with curly auburn hair, green eyes",
    "wardrobe": "minimalist black t-shirt, leather bracelet, silver stud earrings"
  },
  "scene": {
    "location": "minimalist white studio with RGB LED backlighting and glass desk",
    "environment": "soft electric-blue neon outlines, ambient LED glow spills across surfaces"
  },
  "visual_details": {
    "action": "lifts vibrant purple sea urchin with glowing spines using black lacquered chopsticks, slowly guides toward open mouth revealing metallic silver dental work",
    "props": "spiky purple sea urchin, black lacquered chopsticks, Blue Yeti binaural mic",
    "physics": "urchin spines shimmer with brine droplets, interior fluoresces under UV light"
  },
  "cinematography": {
    "lighting": "soft overhead ring light + 365nm UV bar for purple fluorescence, rim light on facial contours",
    "tone": "clinical, hypnotic, hyper-focused",
    "color_palette": "white, electric purple, iridescent silver"
  },
  "audio": {
    "primary_sounds": "delicate lacquer clink, soft spine rustle, wet suction as spines part past lips, controlled exhale",
    "ambient": "ultra-low studio hum",
    "technical_effects": "binaural recording, -12 dBFS peaks"
  }
}
```

### How to Use These Examples

**Copy → Customize → Create**:
1. Pick example closest to your concept
2. Swap specific elements (brand, product, setting)
3. Keep structure for proven results
4. Feed to VEO 3

**Template Customization Guide**:
- **description**: Change subject, keep detail level
- **style**: Swap brand aesthetic ("Apple minimalist" → "Nike athletic")
- **camera**: Adjust angles, keep technical specificity
- **lighting**: Modify mood, keep ratio/motivation details
- **elements**: Replace products, maintain structure
- **motion**: Adapt timing, preserve smoothness
- **audio**: Change sounds, keep ASMR-level detail

---

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

### Critical JSON Insights

**1. Specificity = Professional Results**
- Vague: "nice lighting" → Specific: "soft golden hour with 2:1 exposure ratio, backlit with rim light"
- Vague: "camera moves" → Specific: "slow dolly in from medium to close-up over 5 seconds"

**2. Production Concepts Matter**
- Understanding lighting ratios, camera movements, and timing is what separates pro from amateur
- You don't need equipment anymore—you need knowledge

**3. JSON Bridges Human Vision to AI Execution**
- It's a shared language between your creative intent and VEO 3's capabilities
- Structured data matches AI's computational nature with human creative requirements

**Bottom Line**: Use JSON for commercial/professional work where precision matters. Use paragraph prompts (Claude template) for everything else.

### Commercial Video Types
- Product assembly/unboxing
- Brand storytelling
- Social media campaigns
- Client deliverables ($500-1000+ per video)

---

## The 15 Most Powerful Tips

### Prompting Excellence

**1. Think Like a Director, Not a Typist**
- You have film director power through prompts
- Provide complete production briefs, not casual descriptions
- If it's not the model—it's your prompt

**2. Be Hyper-Specific**
- More descriptive = better results
- Include materials, textures, colors, emotions
- "Soft golden hour with 2:1 ratio" > "nice lighting"

**3. Use Cinematic Language**
- "Wide shot dolly in" > "camera moves forward"
- "Golden hour with warm tones" > "nice lighting"
- Speak the language VEO 3 understands

**4. Lock Style Early**
- First sentence sets the tone
- "Apple minimalist commercial" vs "Nike high-energy athletic"
- Be specific about brand aesthetics

**5. Design Experiences, Not Just Videos**
- Don't describe—design the complete viewer experience
- Include emotional journey, sensory details, atmosphere
- Think: What should the viewer feel?

**6. Repeat Key Elements**
- Want red armor? Say "red armor" twice
- Repetition reinforces important details

**7. Always Add "High Quality Audio"**
- Dramatically improves audio generation success rate
- Specify exact sounds: "gentle pour, ambient café, subtle music"

### Technical Controls

**6. Plan for 8-Second Limit**
- Each clip is maximum 8 seconds
- Design action/dialogue to fit timeframe

**7. Storyboard First**
- Sketch shot sequence before generating
- Prevents wasted credits on unplanned content

**8. Use Consistent Naming**
- Same character names across clips: "Alex the pilot"
- Helps AI maintain character consistency

**9. Test Fast vs Quality**
- As of September 2025: minimal difference
- Test both modes for important shots

**10. Save Successful Prompts**
- Build personal library of what works
- Reuse proven formulas

### Advanced Techniques

**11. JSON for Precision Control**
- Use structured prompts for commercial work
- Provides exact specifications for camera, lighting, audio

**12. Impossible Camera Moves**
- Not limited by reality: "camera swooping through keyhole"
- Embrace surreal cinematography

**13. Add Text in Post**
- VEO 3 fails at text generation
- Always add titles/captions in editing

**14. Upload High-Quality Images**
- Image-to-video quality depends on source
- Low quality input = disappointing output

**15. Always Upscale**
- Use OpenArt upscale feature for 4K output
- Essential for professional results

---

## Camera Angles & Storytelling

### Angles Convey Meaning

**Low Angles** (Camera looking up):
- Suggests: Power, dominance, importance
- Use for: Hero shots, authority figures, moments of triumph
- Example: "Low angle shot looking up at subject, conveying strength and dominance"

**High Angles** (Camera looking down):
- Suggests: Vulnerability, weakness, insignificance  
- Use for: Defeated moments, showing scale, isolation
- Example: "High angle looking down on subject, emphasizing smallness and vulnerability"

**Eye-Level Angles**:
- Suggests: Equality, neutrality, documentary realism
- Use for: Conversations, relatable moments, natural scenes
- Example: "Eye-level shot creating intimate connection with subject"

**Dutch Angles** (Tilted):
- Suggests: Unease, chaos, disorientation
- Use for: Tension, psychological distress, action sequences
- Example: "Dutch angle with 15-degree tilt creating visual tension"

### Compositional Techniques

**Rule of Thirds**:
- Place subject on intersection points
- "Subject positioned on right third line, creating balanced composition"

**Centered Symmetry** (Wes Anderson Style):
- Perfect center framing with symmetrical elements
- "Wes Anderson-style centered symmetrical composition with balanced frame"

**Leading Lines**:
- Use environmental elements to guide eye to subject
- "Leading lines from road converging toward subject in distance"

---

## Workflow Optimization

### The Paradigm Shift

**Old Way**: Need expensive equipment, technical crew, production expertise  
**New Way**: Need production knowledge + ability to communicate with AI

**Critical Understanding**:
- AI video represents a shift from **technical skill** to **communicative clarity**
- You don't need equipment anymore—you need **knowledge of production concepts**
- The gap between amateur and professional results = **prompt specificity**

### Pre-Production
1. **Write detailed prompts** → Reduces failed generations
2. **Use Claude template** for general content → Saves time, improves consistency
3. **Use JSON for commercial work** → Production brief precision
4. **Plan shot sequence** → Clear vision before generating
5. **Study professional commercials** → Learn what elements to specify

### Production
1. **Generate in batches** → More efficient workflow
2. **Test variations** → Create multiple takes, pick best
3. **Track successful prompts** → Build reusable library
4. **Think in production terms** → Lighting ratios, camera specs, timing

### Post-Production
1. **Upscale to 4K** → Non-negotiable for quality
2. **Replace audio if needed** → Use 11 Labs for consistency
3. **Edit for flow** → Stitch clips with transitions
4. **Add film grain + chromatic aberration** → Disguise AI origins

---

## Cost Optimization

### API/Programmatic Access
- **Kie.ai**: $1.50 (quality) / $0.38 (fast) - 75% cheaper than Google direct
- **Features**: Native 9:16, fallback protection, auto-translation
- **Best for**: High-volume production, vertical content

### Credit Saving Strategies
1. Write detailed prompts first (fewer regenerations)
2. Use Fast mode for tests, Quality for finals
3. Generate multiple short clips vs one long video
4. Leverage Claude Code subagent for prompt optimization

---

## Common Mistakes to Avoid

❌ **Using simple, Claude-style conversational prompts** → VEO 3 needs cinematic detail  
❌ **Skipping negative instructions** → Causes unwanted elements  
❌ **Using Fast Mode for final output** → Quality difference too significant  
❌ **Not upscaling videos** → 1080p insufficient for professional use  
❌ **Low-quality source images** → Degrades image-to-video results  
❌ **Rushing prompt creation** → Wastes credits on failed generations  
❌ **Expecting perfect text generation** → Always fails, add in post  
❌ **Inconsistent character descriptions** → Breaks character continuity

---

## Quick Reference Checklist

### Before Generating:
- [ ] Prompt includes all 10 components
- [ ] Negative instructions included
- [ ] **Character imperfections specified** (pores, stray hair, skin texture)
- [ ] **Lighting exposure ratio defined** (2:1 or 4:1 recommended)
- [ ] **Atmospheric elements added** (dust, haze, mist)
- [ ] **Camera angle chosen for story meaning** (low/high/eye-level)
- [ ] **Lens character specified** (vintage/telephoto/anamorphic)
- [ ] **Aperture setting included** (F2.8-F4 for cinematic)
- [ ] **Color palette follows 60-30-10 rule**
- [ ] Time of day specified
- [ ] Camera movement detailed
- [ ] Audio description added
- [ ] Continuous paragraph format (no bullets)

### For Long-Form Content (30+ seconds):
- [ ] Story broken into 8-second beats
- [ ] Identified which scenes need continuation vs fresh start
- [ ] Scene 1 prompt includes complete character/environment details
- [ ] Plan to extract last frame for Scene 2 starting image
- [ ] Scene 2 prompt is 85% identical (only action changes)
- [ ] Budget for continuation: 2× scenes, 2× cost, 2× length

### Settings:
- [ ] Resolution: Highest available
- [ ] Mode: Test with Fast (20 credits) first, then Quality (100 credits)
- [ ] Audio: Enabled (if needed)
- [ ] Aspect ratio: Match intended platform
- [ ] First frame: Upload Midjourney image OR last frame from previous scene

### After Generation:
- [ ] Upscale to 4K using OpenArt
- [ ] Extract last frame (if planning continuation)
- [ ] Replace audio with 11 Labs cloned voice (for creator content)
- [ ] Add film grain (disguises AI origins)
- [ ] Add chromatic aberration (lens imperfection)
- [ ] Trim transition jumps (first/last 1-2 seconds if needed)
- [ ] Crop/adjust for vertical (if social media)
- [ ] Save successful prompts for reuse

---

## The Bottom Line

**Success Formula = Detailed Prompts + Intentional Imperfections + Proper Settings + Always Upscale**

### Core Principles:
1. **Use Claude template** for automatic prompt optimization (general content)
2. **Use JSON prompting** for commercial/professional work (precise control)
3. **Add intentional imperfections** (AI defaults to fake perfection)
4. **Specify exposure ratios** (2:1 or 4:1 for cinematic look)
5. **Include atmospheric elements** (dust, haze, light interaction)
6. **Define camera angles** for story meaning (low = power, high = vulnerability)
7. **Never skip negative instructions**
8. **Test with Fast mode** (20 credits) before Quality (100 credits)
9. **Always upscale to 4K**

### When to Use Which Method:

**📝 Paragraph Prompts (Claude Template)**:
- Social media content
- Personal projects  
- Quick generations
- General video creation
- 90% of your use cases

**📊 JSON Prompts (Structured)**:
- Commercial/advertising content
- Brand campaigns
- Client deliverables
- Product showcases
- Precise control requirements

**🎬 Scene Continuation (Frame-to-Video)**:
- Long-form content (30+ seconds)
- Narrative storytelling
- Character-driven scenes
- Sequential action sequences
- Professional seamless flow

### Advanced Workflows:
- **Character consistency**: Train custom AI models (OpenArt) or use Claude character splitting method
- **Longer videos**: Use frame-to-video continuation with 85/15 rule (85% same prompt, 15% new action)
- **Vertical content**: Use vertical-optimized prompts, then crop in post
- **Post-production**: Add film grain + chromatic aberration to disguise AI origins
- **Voice replacement**: Use 11 Labs for consistent audio (optional for creator content)

### Remember:
**"We don't want it perfect. We want it real."**

True photorealism comes from intentional imperfections, not AI's default ultra-realistic texture overload. Focus on eyes, mouths, skin texture, and hair details—these are where humans detect artificial content.

**For Longer Videos**: Use frame-to-video continuation. Extract last frame of Scene 1, use as starting image for Scene 2 with 85% identical prompt. Only change the specific action (15%).

**Use JSON prompting for commercial work** where precise control over every element matters. Use paragraph prompts with the Claude template for everything else.

---

*VEO 3 rewards detailed, cinematic prompts with technical camera specs. The more specific you are about imperfections, lighting ratios, and atmospheric elements, the more realistic your results will be.*
