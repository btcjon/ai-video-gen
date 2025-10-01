# CLAUDE.md
**AI Video Generation Platform - VEO 3 via Kie.ai**

## Project Purpose

Frame-to-frame AI video generation for commercial marketing videos using Google's VEO 3 model via Kie.ai API (75% cost reduction vs direct Google API).

## Core Workflow

**Frame-to-Frame Generation**: Each scene's ending frame becomes the next scene's starting image, ensuring perfect visual continuity across character, lighting, environment, and product.

**Critical Rule**: Read `/docs/frame-to-frame-video-workflow.md` first - contains 7 non-negotiable rules for success.

## Scripts Used

This project uses global scripts from `/home/dev/.claude/scripts/`:
- `kie_client.py` - VEO 3 video generation (primary)
- `openai_image_client.py` - Image compositing for product integration

**Import pattern**:
```python
import sys
sys.path.append('/home/dev/.claude/scripts')
from kie_client import KieClient
```

**Full API documentation**: Read the script files directly for complete workflows and examples.

## 7 Critical Rules (Frame-to-Frame)

1. **Face Visible in Ending Frame**: Character face must be visible (3/4 profile or facing camera) in every ending frame for continuity
2. **One Action Per Scene**: Max 4 distinct 2-second steps, all serving ONE primary action
3. **Maintain Continuity**: Ending state of Scene N = Starting state of Scene N+1 (no skipping steps)
4. **Use JSON for Complex Scenes**: Multiple characters, camera moves, precise lighting → Use JSON structure
5. **Plan Transitions**: Major location/time changes need dedicated transition scenes
6. **Establish Environmental Aesthetics**: Set complete visual direction at transition points (day→night, etc.)
7. **Product Visibility Throughout**: Once product exits frame, nearly impossible to reintroduce with brand accuracy

**Full details**: `/docs/frame-to-frame-video-workflow.md`

## Key Project Details

**API**: Kie.ai VEO 3
- Key: `20108f4bba626227a1bb5e281d1e5a64`
- Dashboard: https://kie.ai/dashboard

**Output Structure**:
- Videos: `docs/output/{scene_name}.mp4`
- Ending frames: `docs/output/{scene_name}_ending.jpg`
- Production plans: `production-plans/{campaign}/`

## MANDATORY Workflow

**CRITICAL**: NEVER generate videos with raw prompts. ALWAYS use `veo3-prompt-architect` agent first.

1. Get enhanced prompt from agent with scene concept
2. Generate with `kie_client.py` using enhanced prompt
3. For frame-to-frame: Pass previous ending frame context to agent
4. Repeat for each scene

**Why**: Agent prevents 80% of failures. Costs $0.38-$1.50 per generation - enhancement is critical.

## Project-Specific Workflow Notes

- Always use `veo3-prompt-architect` agent before video generation
- Default output: `docs/output/` directory
- Frame extraction enabled by default for continuity
- Product compositing: Generate scene first, composite product after

## Cost Optimization

- **Testing/Iteration**: veo3_fast ($0.38)
- **Final/Hero**: veo3 ($1.50)
- **7 scenes × veo3_fast** = $2.66 (56 seconds total)
- **Enable fallback**: 25% higher success rate (16:9 only)

## Critical Gotchas

1. **Character Continuity**: Face must be visible at scene endings
2. **Product Continuity**: Keep product in every frame OR plan for compositing
3. **Action Density**: Don't cram multiple actions into 8 seconds
4. **Environmental Transitions**: Explicitly describe night/day aesthetic changes
5. **No Auto-Regen**: If generation fails quality check, it costs money to regenerate
6. **JSON for Complex**: Use JSON structure for multi-character or precise scenes

## Documentation Priority

1. **START HERE**: `/docs/frame-to-frame-video-workflow.md`
2. **Prompt Engineering**: `/docs/veo3_prompt_analysis.md`
3. **Templates**: `/docs/templates/60-second-campaign-template.md`

## Example Campaign

See `/docs/output/h2o_pure_test/` for complete 7-scene frame-to-frame campaign demonstrating all rules and workflows.