# Scene Continuation Guide - Creating Longer VEO 3 Videos

Based on insights from YouTube tutorials, here's how to create longer, seamless videos by chaining scenes together.

## The Problem
VEO 3 generates 8-second clips. To create longer content, we need to connect multiple scenes smoothly.

## The Solution: Frame-to-Video Continuation

### Core Technique
1. Generate Scene 1 normally
2. Extract the **last frame** of Scene 1
3. Use that frame as the **starting image** for Scene 2
4. Keep prompts **85% similar** between scenes (only modify key actions)

### Why This Works
- Maintains character consistency
- Preserves environment/lighting
- Creates natural flow between scenes
- Avoids jarring cuts or character changes

## Implementation Strategy

### Step 1: Initial Scene
```json
{
  "name": "Scene 1 - Introduction",
  "prompt": "45-year-old father checking emergency supplies in garage",
  "aspect_ratio": "16:9"
}
```

### Step 2: Continuation Scene
```json
{
  "name": "Scene 2 - Continuation",
  "continue_from": "Scene 1",
  "prompt": "45-year-old father finding H2O Pure bottle among emergency supplies",
  "similarity": "85%",
  "changes": "Only changed action from 'checking' to 'finding bottle'"
}
```

## Best Practices

### 1. Prompt Similarity Rule
**Keep 85% Same:**
- Same character description
- Same environment
- Same lighting/mood
- Same camera angle

**Only Change 15%:**
- The specific action
- Minor prop additions
- Slight camera movement

### 2. Transition Planning
- Expect 1-2 seconds of "jump" at transition
- Plan to trim in editing
- Generate 10-second clips, use 8 seconds

### 3. Scene Segmentation
Break your story into 8-second chunks:
```
0:00-0:08 - Establish crisis
0:08-0:16 - Show problem
0:16-0:24 - Introduce solution
0:24-0:32 - Demonstrate product
0:32-0:40 - Show results
```

## Technical Implementation

### Current Capability
Our workflow uses **image-to-video** which is perfect for this:
```bash
# Scene 1
python3 scripts/veo3_generate.py generate --prompt "Scene 1 prompt"

# After Scene 1 completes, extract last frame
# Then Scene 2 using that frame:
python3 scripts/veo3_generate.py generate \
  --prompt "Scene 1 prompt with minor modification" \
  --image /path/to/last-frame.png
```

### Future Enhancement
Add automatic frame extraction:
```python
def continue_scene(previous_task_id, new_prompt):
    # 1. Download video from previous task
    # 2. Extract last frame
    # 3. Use as image for next generation
    # 4. Keep prompt 85% similar
```

## Practical Example: H2O Pure Campaign

### Traditional Approach (What We Have)
- 4 separate unconnected scenes
- Different angles/perspectives
- Risk of character inconsistency

### Continuous Approach (Enhancement)
```
Scene 1a (0-8s): Father at window watching grid fail
Scene 1b (8-16s): [Continue from 1a] Father turning to check supplies
Scene 2a (16-24s): [Continue from 1b] Father in garage with broken filter
Scene 2b (24-32s): [Continue from 2a] Father discovering H2O Pure
Scene 3a (32-40s): [New shot] Hands demonstrating product
Scene 3b (40-48s): [Continue from 3a] Water clearing transformation
Scene 4a (48-56s): [New shot] Family gathering
Scene 4b (56-64s): [Continue from 4a] Family drinking purified water
```

## Common Issues & Solutions

### Issue: Audio Generation Failures
**Solution:** We already generate without narration - perfect!

### Issue: Character Changes Between Scenes
**Solution:** Use frame continuation + identical character description

### Issue: Jumpy Transitions
**Solution:** Generate 10s, use middle 8s, trim transitions

### Issue: Prompt Complexity Confusion
**Solution:** Keep prompts simple, modify minimally

## Quick Implementation Checklist

- [ ] Break story into 8-second segments
- [ ] Plan which scenes need continuation
- [ ] Keep character descriptions identical
- [ ] Modify only 15% of prompt between scenes
- [ ] Use last frame as starting image
- [ ] Plan for transition trimming
- [ ] Test with veo3_fast first

## Cost Optimization

### Current: 4 scenes × $0.38 = $1.52
### Continuous: 8 segments × $0.38 = $3.04

**But you get:**
- 64 seconds instead of 32 seconds
- Smoother transitions
- Better narrative flow
- Professional quality

## Conclusion

Frame-to-video continuation is the key to professional long-form VEO 3 content. By keeping prompts similar and using last frames as starting points, we can create seamless narratives that rival traditional video production.