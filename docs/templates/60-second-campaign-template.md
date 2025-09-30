# 60-Second Campaign Template (v3.0)
**Updated**: September 26, 2025
**Workflow Version**: 3.0 with User Approval Gates

## 🛑 USER APPROVAL WORKFLOW

### Two Mandatory Checkpoints:
1. **After Creative Brief** - User reviews concept
2. **Before Generation** - User approves prompts and cost

### NO GENERATION WITHOUT:
- ✓ User approved creative concept
- ✓ Product image uploaded
- ✓ Voiceover script written
- ✓ Quality score ≥8/10
- ✓ User approved final prompts

## Standard Structure (7 Scenes Maximum for 60s)

### Scene Distribution & Product Requirements

| Scene # | Duration | Purpose | Generation Method | Why |
|---------|----------|---------|------------------|-----|
| 1 | 0:00-0:08 | Problem Recognition | Text-to-video | No product yet |
| 2 | 0:08-0:16 | Current Solution Gaps | Text-to-video | Context building |
| 3 | 0:16-0:24 | Discovery Moment | **Image-to-video** | Product first appearance |
| 4 | 0:24-0:32 | Product Understanding | **Image-to-video** | Product demonstration |
| 5 | 0:32-0:40 | Using Product | **Image-to-video** | Product in action |
| 6 | 0:40-0:48 | Integration/Results | **Image-to-video** | Product in system |
| 7 | 0:48-0:56 | Call to Action + Confidence | **Image-to-video** | Product hero shot + resolution |

## Critical Rules

### Product Consistency Matrix

```
SCENE CONTAINS PRODUCT?
├─ YES (visible/mentioned/handled)
│  └─ MUST use image-to-video
│     └─ Prompt = "ACTION with this product"
│
└─ NO (product absent)
   └─ Can use text-to-video
      └─ Prompt = full scene description
```

### Technical Requirements (EVERY Scene)

```json
{
  "aspectRatio": "16:9",     // CRITICAL: Prevents 9:16 errors
  "model": "veo3_fast",       // Start with fast, upgrade if needed
  "enableFallback": true,     // 25% better success rate
  "enableTranslation": true   // Better prompt handling
}
```

## Complete Deliverables Package (v3.0 REQUIRED)

Every campaign MUST include:
1. **Videos** - All 7 scenes
2. **Voiceover Script** - Timed to 8-second segments
3. **Assembly Instructions** - Step-by-step editing guide
4. **Music Suggestions** - Tone and timing
5. **Export Settings** - Platform-specific specs

## Scene Planning Worksheet

### Scene 1: Problem Recognition (Text-to-Video)
**Purpose**: Establish vulnerability/need
**Emotional Beat**: Concern/awareness
**Product Visible**: NO
**Generation Method**: Text-to-video
**Technical Specs**:
- Lens: 50mm (natural perspective)
- Aperture: F4 (balanced)
- Lighting: 2:1 ratio (approachable)
- Imperfections: Required (pores, texture, wear)

### Scene 2: Current Solution Gaps (Text-to-Video)
**Purpose**: Why existing methods fail
**Emotional Beat**: Frustration/realization
**Product Visible**: NO
**Generation Method**: Text-to-video
**Technical Specs**: Similar to Scene 1 for consistency

### Scene 3: Discovery Moment (Image-to-Video)
**Purpose**: Finding the solution
**Emotional Beat**: Hope/curiosity
**Product Visible**: YES ✓
**Generation Method**: **IMAGE-TO-VIDEO REQUIRED**
**Prompt Structure**: "Hands discovering this product..."
**Image Path**: `/home/dev/Projects/ai-video-gen/images/[product].png`

### Scene 4: Product Understanding (Image-to-Video)
**Purpose**: How it works
**Emotional Beat**: Understanding/trust
**Product Visible**: YES ✓
**Generation Method**: **IMAGE-TO-VIDEO REQUIRED**
**Prompt Structure**: "Examining this product closely..."

### Scene 5: Using Product (Image-to-Video)
**Purpose**: Demonstration
**Emotional Beat**: Confidence building
**Product Visible**: YES ✓
**Generation Method**: **IMAGE-TO-VIDEO REQUIRED**
**Prompt Structure**: "Using this product to..."

### Scene 6: Integration/Results (Image-to-Video)
**Purpose**: Product in daily life
**Emotional Beat**: Satisfaction
**Product Visible**: YES ✓
**Generation Method**: **IMAGE-TO-VIDEO REQUIRED**
**Prompt Structure**: "Placing this product in..."

### Scene 7: Call to Action + Confidence (Image-to-Video)
**Purpose**: Drive action + peace of mind
**Emotional Beat**: Urgency/security
**Product Visible**: YES ✓
**Generation Method**: **IMAGE-TO-VIDEO REQUIRED**
**Prompt Structure**: "This product ready for..."
**Note**: Combines CTA with confidence for 60s limit

## Voiceover Script Template (v3.0 MANDATORY)

```markdown
# [Campaign Name] - Voiceover Script

## Recording Instructions
- Tone: [Conversational/Urgent/Authoritative]
- Pace: [Normal/Slow/Fast]
- Emotion Arc: [Concern → Discovery → Confidence]

## Script with Exact Timing

[0:00-0:08] Scene 1 - Problem Recognition
"[10-12 words max for 8 seconds]"
[Emotional beat: Concern/awareness]

[0:08-0:16] Scene 2 - Current Gaps
"[10-12 words building tension]"
[Emotional beat: Frustration]

[0:16-0:24] Scene 3 - Discovery
"[Name product clearly here]"
[Emotional beat: Hope]

[0:24-0:32] Scene 4 - Understanding
"[How it works simply]"
[Emotional beat: Trust]

[0:32-0:40] Scene 5 - Using Product
"[Key benefit statement]"
[Emotional beat: Confidence]

[0:40-0:48] Scene 6 - Results
"[Proof or credibility]"
[Emotional beat: Satisfaction]

[0:48-0:56] Scene 7 - Call to Action
"[Clear next step]"
[Emotional beat: Urgency]

## Key Phrases to Emphasize
- "[Product name]"
- "[Core benefit]"
- "[Differentiator]"
```

## Self-Contained Generation Commands

### For Scenes WITHOUT Product (1, 2 only)

```bash
# Text-to-video generation
curl -X POST "https://api.kie.ai/api/v1/veo/generate" \
  -H "Authorization: Bearer 20108f4bba626227a1bb5e281d1e5a64" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "[FULL_SCENE_DESCRIPTION]",
    "model": "veo3_fast",
    "aspectRatio": "16:9",
    "enableFallback": true,
    "enableTranslation": true
  }'
```

### For Scenes WITH Product (3, 4, 5, 6, 7)

```bash
# Step 1: Upload product image
PRODUCT_IMAGE="/home/dev/Projects/ai-video-gen/images/[YOUR_PRODUCT].png"
IMAGE_BASE64=$(base64 -w0 "$PRODUCT_IMAGE")

IMAGE_URL=$(curl -s -X POST "https://api.kie.ai/api/file-base64-upload" \
  -H "Authorization: Bearer 20108f4bba626227a1bb5e281d1e5a64" \
  -H "Content-Type: application/json" \
  -d "{
    \"fileBase64\": \"data:image/png;base64,$IMAGE_BASE64\",
    \"uploadPath\": \"veo3-products\",
    \"fileName\": \"product.png\"
  }" | jq -r '.data.fileUrl')

# Step 2: Generate with product
curl -X POST "https://api.kie.ai/api/v1/veo/generate" \
  -H "Authorization: Bearer 20108f4bba626227a1bb5e281d1e5a64" \
  -H "Content-Type: application/json" \
  -d "{
    \"prompt\": \"[ACTION WITH this product, NOT description]\",
    \"imageUrls\": [\"$IMAGE_URL\"],
    \"model\": \"veo3_fast\",
    \"aspectRatio\": \"16:9\",
    \"enableFallback\": true
  }"
```

## Pre-Generation Approval Checklist (v3.0)

### User Approval Gate 1 (After Creative)
- [ ] Creative brief presented to user
- [ ] Voiceover script reviewed
- [ ] Emotional journey approved
- [ ] User selected: APPROVE / REVISE / RESTART

### User Approval Gate 2 (Before Generation)
- [ ] All 7 prompts shown to user
- [ ] Cost displayed: $2.66 (fast) or $10.50 (quality)
- [ ] Product image path confirmed
- [ ] Generation method matrix shown
- [ ] User selected: GENERATE / REVISE / CANCEL

## Quality Checklist (Before Generation)

### Scene Planning
- [ ] 7 scenes MAXIMUM planned (56 seconds actual)
- [ ] Product scenes identified (typically 4-5 scenes)
- [ ] Image-to-video marked for ALL product scenes
- [ ] Text-to-video for non-product scenes only

### Technical Verification
- [ ] Aspect ratio: "16:9" in EVERY request
- [ ] Product image path verified
- [ ] Action prompts (not descriptions) for image-to-video
- [ ] All imperfections specified
- [ ] Camera specs included
- [ ] Exposure ratios defined

### Product Consistency
- [ ] Scene 3: First product appearance via image-to-video
- [ ] Scenes 4-6: Continued product via image-to-video
- [ ] Scene 7: Final product shot via image-to-video
- [ ] NO text-to-video for product scenes

## Common Mistakes to Avoid

### ❌ DON'T
- Use text-to-video when product is visible
- Forget to specify aspectRatio: "16:9"
- Describe product appearance in image-to-video prompts
- Create only 4 scenes (too short)
- Include narration in generation

### ✅ DO
- Use image-to-video for EVERY product scene
- Always specify aspect ratio explicitly
- Describe actions with product, not product itself
- Create exactly 7 scenes for 60-second limit
- Add voiceover in post-production

## Success Metrics

- ✓ Correct product in 100% of product scenes
- ✓ Consistent 16:9 aspect ratio
- ✓ 56-second duration (under 60s platform limit)
- ✓ No external script dependencies
- ✓ Quality score ≥8/10 before generation

## Pre-Flight Safety Checks (v3.0)

```bash
#!/bin/bash
# Run before ANY generation

if [ "$USER_APPROVED" != "true" ]; then
  echo "❌ STOP: No user approval"
  exit 1
fi

if [ ! -f "$PRODUCT_IMAGE" ]; then
  echo "❌ STOP: Product image missing"
  exit 1
fi

if [ "$QUALITY_SCORE" -lt 8 ]; then
  echo "❌ STOP: Quality score too low"
  exit 1
fi

echo "✅ All safety checks passed"
```

## Campaign JSON Structure (v3.0 Enhanced)

```json
{
  "campaign": "[Campaign Name]",
  "total_duration": "56 seconds (60s platform max)",
  "segments": 7,
  "scenes": [
    {
      "name": "Scene 1 - Problem",
      "duration": "0:00-0:08",
      "generation_method": "text-to-video",
      "requires_product_image": false,
      "aspect_ratio": "16:9",
      "prompt": "[Full scene description]",
      "user_approved": false,
      "quality_score": 0
    },
    {
      "name": "Scene 3 - Discovery",
      "duration": "0:16-0:24",
      "generation_method": "image-to-video",
      "requires_product_image": true,
      "aspect_ratio": "16:9",
      "product_image": "/path/to/product.png",
      "prompt": "[ACTION with this product]",
      "user_approved": false,
      "quality_score": 0,
      "product_url": null
    }
  ]
}
```

## User Presentation Format (v3.0)

```markdown
=== CAMPAIGN READY FOR APPROVAL ===

📊 CAMPAIGN: [Name]
Duration: 56 seconds (7 scenes)
Cost: $2.66 (veo3_fast) / $10.50 (veo3)
Platform: 16:9 horizontal

🎬 SCENE BREAKDOWN
Scenes 1-2: Text-to-video (no product)
Scenes 3-7: Image-to-video (product visible)

🔊 VOICEOVER SCRIPT
[Show complete script with timing]

📦 DELIVERABLES INCLUDED
✓ 7 videos (8 seconds each)
✓ Voiceover script with timing
✓ Assembly instructions
✓ Music suggestions
✓ Export settings

💰 OPTIONS
[1] Generate with veo3_fast ($2.66)
[2] Generate with veo3 ($10.50)
[3] Revise prompts
[4] Cancel

Your choice: _____
```

## Post-Production

### Voiceover Timing
- Scene 1-2: Problem setup (16s)
- Scene 3-4: Solution introduction (16s)
- Scene 5-6: Benefits/usage (16s)
- Scene 7: Call to action + confidence (8s)

### Assembly Order
1. Download all 7 videos
2. Verify aspect ratios (all 16:9)
3. Verify product consistency
4. Edit together in sequence
5. Add voiceover track
6. Add music/effects
7. Export final 56-second video (safe for 60s platforms)