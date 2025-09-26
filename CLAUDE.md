# CLAUDE.md
Today's Date: 9/26/25

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a VEO 3 AI video generation platform specializing in commercial-grade video production using Google's VEO 3 model via Kie.ai's API integration. The project focuses on creating marketing videos with a 75% cost reduction compared to direct Google API usage.

## Key Commands

### Video Generation with Quality Gates
```bash
# Generate a single video
python3 scripts/veo3_generate.py generate --prompt "Your video idea"

# Generate with quality score enforcement
python3 scripts/veo3_generate.py generate \
  --prompt "Your cinema-grade prompt" \
  --quality-score 8.5

# Generate with product image (now uses Kie.ai native upload)
python3 scripts/veo3_generate.py generate \
  --prompt "Show hands demonstrating this product" \
  --image /images/product.png

# Continue from previous scene (frame-to-video) - NEW
python3 scripts/veo3_generate.py generate \
  --prompt "85% similar prompt with action change" \
  --continue-from [previous-task-id]

# Generate entire campaign batch (now with auto-continuation)
python3 scripts/veo3_generate.py batch h2o-pure

# Check generation status
python3 scripts/veo3_generate.py status --campaign h2o-pure
```

### Dashboard Access
- Check generation status: https://kie.ai/dashboard
- Videos typically complete in 10-15 minutes

## Creative-First Architecture & Workflow

### 7-Phase Creative Workflow (NEW)
1. **Discovery & Intent** → Creative Director understands emotional goals
2. **Research & Analysis** → Competitive landscape and USP discovery
3. **Creative Planning** → Storyboarding and emotional journey mapping
4. **Technical Specification** → Camera, lighting, imperfections planning
5. **Prompt Engineering** → Transform vision into VEO 3 language
6. **Quality Review** → Validate prompts score ≥8/10 before generation
7. **Generation & Iteration** → Execute with quality gates

### Five-Agent System (ENHANCED)
The project uses five specialized Claude Code agents working in sequence:

1. **veo3-creative-director** (`.claude/agents/veo3-creative-director.md`) - NEW
   - Conducts discovery interviews to understand creative intent
   - Creates emotional journey maps and success metrics
   - Ensures every video has clear purpose before technical work

2. **veo3-prompt-architect** (`.claude/agents/veo3-prompt-architect.md`)
   - REQUIRES creative brief before creating any prompts
   - Transforms ideas into cinema-grade VEO 3 prompts
   - Includes ALL imperfections, camera specs, exposure ratios
   - Uses 11-component structure from Essential Mastery Guide

3. **veo3-production-manager** (`.claude/agents/veo3-production-manager.md`)
   - Focuses on technical specifications (camera, lighting, color)
   - Plans scene continuation strategy for longer content
   - Ensures realism elements in every prompt

4. **veo3-quality-review** (`.claude/agents/veo3-quality-review.md`) - NEW
   - Validates every prompt before generation
   - Scores on 4 criteria (min 8/10 required)
   - Prevents costly regeneration through quality gates

5. **veo3-api-optimizer** (`.claude/agents/veo3-api-optimizer.md`)
   - ENFORCES quality gate (no generation if score <8/10)
   - Contains Kie.ai API key: `20108f4bba626227a1bb5e281d1e5a64`
   - Tracks quality metrics with generation results

### API Integration Details

**Kie.ai Endpoints:**
- Generate: `POST https://api.kie.ai/api/v1/veo/generate`
- Status: `GET https://api.kie.ai/api/v1/veo/record-info?taskId=XXX`
- 1080p: `GET https://api.kie.ai/api/v1/veo/get-1080p-video?taskId=XXX`

**Request Structure:**
```python
{
    "prompt": "Your video description",
    "model": "veo3_fast",  # or "veo3" for quality
    "aspectRatio": "16:9",  # or "9:16" for vertical
    "enableFallback": True,  # 25% higher success rate
    "enableTranslation": True,
    "watermark": "Optional brand text",
    "imageUrls": []  # Images uploaded via Kie.ai File Upload API
}
```

**File Upload API (NEW - Preferred for Images):**
- Base64 Upload: Files ≤1MB
- File Stream: Files 1-100MB
- URL Upload: Remote files
- Auto-deleted after 3 days
- Native integration with VEO 3

## Production Workflow

### Creative-First Production Process
1. **Creative Discovery FIRST**: No prompts without understanding intent
2. **Technical Specs REQUIRED**: Camera lens, aperture, exposure ratios
3. **Imperfections MANDATORY**: Pores, sweat, stray hair, atmosphere
4. **Quality Score ENFORCED**: Minimum 8/10 or generation blocked
5. **Scene Continuation**: 85/15 rule for connected segments
6. **No Narration**: Post-production voiceover for control

### Post-Production Audio Strategy
- Generate videos WITHOUT narration
- Add professional voiceover in post-production
- Benefits: Perfect timing, consistent voice, no cutoff issues
- Tools: 11Labs, ElevenLabs, or record your own

### Cost Optimization
- **Testing/Social**: Use veo3_fast ($0.38)
- **Hero/Commercial**: Use veo3 ($1.50)
- **Batch Processing**: Group similar videos for efficiency
- **Fallback**: Enable for 25% higher success rate

## Project Structure (Simplified)

```
/scripts/                      # Unified generation scripts
  veo3_generate.py            # Main unified generator (text-to-video & image-to-video)
  veo3_image.py               # Legacy image-to-video helper (if needed)

/production-plans/             # Campaign organization
  h2o-pure/                   # Example campaign folder
    prompts/
      final-prompts.json      # Standard 4-scene version
      h2o-pure-continuous-flow.json  # NEW: 8-segment extended version
    tasks/                    # Auto-generated task tracking

/data/                        # General task tracking

/docs/                        # VEO 3 documentation
  veo3-essential-mastery-guide.md  # CRITICAL: Full technical requirements
  VEO3-CREATIVE-WORKFLOW.md       # 7-phase creative process
  templates/                      # NEW workflow templates
    discovery-interview-template.md
    technical-specification-sheet.md
    quality-review-checklist.md
    prompt-scoring-rubric.md
    imperfection-library.md

/.claude/agents/              # Claude Code agents
  veo3-prompt-architect.md   # Creates cinema-grade prompts
  veo3-production-manager.md # Orchestrates campaigns
  veo3-api-optimizer.md      # API integration (contains API key)

/images/                      # Product images
  6mL H2O Pure_square.png

/output/                      # Downloaded videos

VEO3-QUICK-START.md          # Quick start guide
WORKFLOW-REVIEW.md           # Workflow analysis
SCENE-CONTINUATION-GUIDE.md  # Frame continuation technique
```

## Critical Requirements (VEO 3 Essential Mastery Guide)

### Mandatory in EVERY Prompt
1. **Intentional Imperfections**:
   - Visible pores, natural oil/sweat sheen
   - Stray hairs (even in neat styles)
   - Skin texture variations, subtle asymmetry
   - Clothing wrinkles and wear

2. **Camera Specifications**:
   - Lens type: 35mm/50mm/85mm/100mm
   - Aperture: F1.4/F2.8/F4/F8
   - Movement: dolly/pan/tracking/static
   - Angle: low/high/eye-level/Dutch

3. **Lighting Architecture**:
   - Exposure ratio: 2:1 (soft) or 4:1 (dramatic)
   - Key light source and direction
   - Atmospheric elements: dust particles, volumetric rays, haze

4. **Color Science**:
   - 60% dominant color
   - 30% secondary color
   - 10% accent color

### Quality Gates (NEW)
- **Creative Brief Required**: No prompts without intent understanding
- **Quality Score ≥8/10**: Enforced before generation
- **Command**: `python3 scripts/veo3_generate.py generate --prompt "..." --quality-score 8.5`

## Critical Implementation Notes

### Audio & Vocals Strategy
- **NO NARRATION IN PROMPTS** - Add voiceover in post-production
- Character dialogue OK if under 10 words
- Focus on ambient sounds and effects in prompts
- Include "(no subtitles)" directive
- **Post-Production**: Use 11Labs, recorded voiceover, or AI voice tools
- **Benefits**: No cutoff issues, perfect timing, consistent voice

### Common Issues
- Status endpoints may return 404 - use dashboard or callbacks
- Videos take 10-15 minutes - plan accordingly
- Fallback only works with 16:9 aspect ratio
- 1080p processing takes additional 1-2 minutes after 720p

### Workflow Templates (NEW)
- **Discovery**: `/docs/templates/discovery-interview-template.md`
- **Technical Specs**: `/docs/templates/technical-specification-sheet.md`
- **Quality Review**: `/docs/templates/quality-review-checklist.md`
- **Scoring**: `/docs/templates/prompt-scoring-rubric.md`
- **Imperfections**: `/docs/templates/imperfection-library.md`

### Best Practices (Creative-First)
- **Quick Start**: Read `VEO3-QUICK-START.md` for basics
- **Long Content**: Read `SCENE-CONTINUATION-GUIDE.md` for 64s+ videos
- **Testing**: Always use veo3_fast ($0.38) before veo3 ($1.50)
- **Continuation**: Extract last frame, use as `--image` for next scene
- **85% Rule**: Keep prompts 85% similar between connected scenes
- **Segmentation**: Break stories into 8-second chunks
- **Products**: Use `--image` flag for exact representation
- **Status**: Check https://kie.ai/dashboard (10-15 min per segment)