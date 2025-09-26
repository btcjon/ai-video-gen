# VEO 3 Creative-First Workflow

## Philosophy

**Current Problem**: Our workflow is too mechanical - it jumps straight to generation without understanding the creative essence, missing critical best practices from the VEO 3 Essential Mastery Guide.

**New Approach**: Creative understanding → Research → Planning → Engineering → Review → Generation

Scripts are utilities, not drivers. Agents orchestrate the creative process.

---

## The 7-Phase Creative Workflow

### Phase 1: Discovery & Intent Understanding
**Owner**: Creative Director Agent (new)
**Duration**: 5-15 minutes
**Purpose**: Understand the soul of what we're creating

#### Essential Questions
- What emotion should viewers feel?
- What action should they take?
- Who is the exact target audience?
- What's the one core message?
- Where will this be shown? (platform/context)
- What's the success metric?

#### Deliverables
- Creative brief (1-2 paragraphs)
- Emotional journey map
- Target audience profile
- Success criteria

#### Agent Actions
```markdown
1. Interview user with targeted questions
2. Probe deeper on vague responses
3. Extract unstated assumptions
4. Identify creative constraints
5. Document brand voice/personality
```

---

### Phase 2: Research & Competitive Analysis
**Owner**: Research Agent
**Duration**: 10-20 minutes
**Purpose**: Understand the landscape and find differentiation

#### Research Areas
- **Competitor Analysis**: Similar videos/campaigns
- **Reference Collection**: Inspiration from adjacent industries
- **USP Discovery**: What makes this unique?
- **Trend Analysis**: Current styles/techniques working
- **Platform Best Practices**: What performs on target platform

#### Deliverables
- Competitor analysis with 3-5 examples
- Visual reference board
- USP statement
- Platform optimization notes

#### Agent Actions
```markdown
1. Web scraping for similar content
2. Analyze successful videos in category
3. Extract common patterns
4. Identify differentiation opportunities
5. Document platform-specific requirements
```

---

### Phase 3: Creative Planning & Storyboarding
**Owner**: veo3-prompt-architect (enhanced)
**Duration**: 15-30 minutes
**Purpose**: Design the experience, not just describe it

#### Planning Elements
- **Narrative Arc**: Beginning → Middle → End
- **Emotional Progression**: How feelings evolve
- **Visual Journey**: Key visual moments
- **Audio Strategy**: Music, SFX, voice approach
- **Pacing & Rhythm**: Energy levels throughout

#### For Long-Form (30+ seconds)
- Break into 8-second segments
- Identify continuation points (85/15 rule)
- Mark new shot transitions
- Plan frame extraction points

#### Deliverables
- Scene-by-scene breakdown
- Emotional beat sheet
- Visual storyboard (even rough sketches)
- Audio mood board
- Timing document

---

### Phase 4: Technical Specification
**Owner**: veo3-production-manager
**Duration**: 10-15 minutes
**Purpose**: Apply professional production knowledge

#### Critical Specifications (Often Missed)

##### Camera Work
- **Lens Choice**: 35mm (wide), 50mm (normal), 85mm (portrait)
- **Aperture**: F2.8-F4 (cinematic depth)
- **Movement**: Dolly, pan, tracking, static
- **Angles**: Low (power), high (vulnerable), Dutch (tension)

##### Lighting Design
- **Exposure Ratio**: 2:1 (soft) or 4:1 (dramatic)
- **Key Light**: Direction and quality
- **Motivation**: Where light comes from
- **Atmosphere**: Dust, haze, volumetric rays

##### Realism Elements (CRITICAL)
- **Intentional Imperfections**: Pores, sweat, stray hair
- **Skin Texture**: Marks, uneven tone, natural aging
- **Environmental**: Dust particles, heat distortion
- **Lens Character**: Vintage, anamorphic, mobile aesthetic

##### Color Science
- **60-30-10 Rule**: Dominant, secondary, accent
- **Color Temperature**: Warm/cool balance
- **Mood Palette**: Emotional color choices

#### Deliverables
- Technical specification sheet
- Camera/lighting plan
- Imperfection checklist
- Color palette reference

---

### Phase 5: Prompt Engineering & Optimization
**Owner**: veo3-prompt-architect
**Duration**: 20-30 minutes
**Purpose**: Transform creative vision into VEO 3 language

#### Prompt Formats

##### When to Use What
- **Paragraph Format**: Quick social content, tests
- **JSON Format**: Commercial work, precise control
- **Hybrid**: JSON structure with paragraph details

#### The 11-Component Integration
1. Scene summary (cinematic moment)
2. Subject (with imperfections)
3. Background & context
4. Action (realistic movement)
5. Style & aesthetic
6. Camera instructions (technical)
7. Composition & framing
8. Lighting & mood (with ratios)
9. Audio (no narration, ambient/SFX only)
10. Color palette (60-30-10)
11. Negative instructions

#### Quality Checklist (MUST HAVE)
- [ ] Imperfections specified
- [ ] Exposure ratio defined
- [ ] Atmospheric elements added
- [ ] Camera lens specified
- [ ] Aperture included (F2.8-F4)
- [ ] Color distribution follows 60-30-10
- [ ] Negative instructions comprehensive
- [ ] Audio describes sounds, not narration

#### Deliverables
- Complete prompts (JSON)
- Technical annotations
- Generation parameters
- Fallback variations

---

### Phase 6: Quality Review & Validation
**Owner**: Quality Review Agent (new)
**Duration**: 5-10 minutes
**Purpose**: Ensure nothing is missed before generation

#### Review Criteria

##### Creative Alignment
- Does prompt capture original intent?
- Is emotional journey clear?
- Will target audience connect?

##### Technical Completeness
- All 11 components present?
- Imperfections included?
- Camera specs defined?
- Lighting ratios specified?

##### Best Practice Compliance
- Following Essential Mastery Guide?
- Platform optimizations applied?
- Negative instructions comprehensive?

#### Review Actions
```markdown
1. Score each prompt (1-10) on:
   - Creative alignment
   - Technical detail
   - Realism elements
   - Platform optimization

2. Flag missing elements
3. Suggest improvements
4. Approve or request revision
```

#### Deliverables
- Quality score report
- Improvement recommendations
- Final approved prompts

---

### Phase 7: Generation & Iteration
**Owner**: veo3-api-optimizer
**Duration**: 15-30 minutes per iteration
**Purpose**: Execute and refine

#### Generation Strategy
1. **Test Generation**: veo3_fast ($0.38)
2. **Review Results**: What worked/didn't?
3. **Refine Prompts**: Based on results
4. **Final Generation**: veo3 quality ($1.50)

#### Script Usage (As Utilities)
```bash
# Scripts are tools, not the workflow
python3 scripts/veo3_generate.py generate \
  --prompt "[agent-crafted prompt]" \
  --model veo3_fast

# For campaigns
python3 scripts/veo3_generate.py batch [campaign]
```

#### Iteration Loop
- Generate → Review → Identify issues → Refine prompt → Regenerate
- Maximum 3 iterations before creative reassessment

---

## Agent Responsibilities

### New Agents Needed

#### 1. Creative Director Agent
**Purpose**: Understand intent, guide creative vision
**Tools**: Interview, research, mood boarding
**Output**: Creative brief, success criteria

#### 2. Quality Review Agent
**Purpose**: Ensure best practices, catch issues
**Tools**: Checklist validation, scoring
**Output**: Quality reports, improvement suggestions

### Enhanced Existing Agents

#### veo3-prompt-architect
**Enhancements**:
- Must interview before creating prompts
- Apply ALL Essential Mastery Guide practices
- Include imperfections and technical specs

#### veo3-production-manager
**Enhancements**:
- Focus on technical specifications
- Ensure realism elements
- Plan frame continuations properly
- Document all camera/lighting details

#### veo3-api-optimizer
**Enhancements**:
- Execute AFTER approval only
- Track quality scores
- Manage iteration cycles
- Report generation analytics

---

## Workflow Examples

### Example 1: Quick Social Content (15 minutes)

1. **Discovery** (2 min): "Viral moment showing product benefit"
2. **Research** (3 min): Check trending formats
3. **Planning** (3 min): Single 8-second hook
4. **Technical** (2 min): Handheld, natural light, authentic
5. **Prompt** (3 min): Paragraph format with imperfections
6. **Review** (1 min): Quick checklist
7. **Generate** (1 min): veo3_fast

### Example 2: Commercial Campaign (60 minutes)

1. **Discovery** (10 min): Deep brand understanding, emotional journey
2. **Research** (15 min): Competitor analysis, USP identification
3. **Planning** (10 min): 4-scene storyboard, continuation mapping
4. **Technical** (10 min): Full production specs, lighting plans
5. **Prompt** (10 min): JSON format with precise control
6. **Review** (5 min): Comprehensive quality check
7. **Generate** (10 min): Test + refinement + final

### Example 3: Long-Form Narrative (90 minutes)

1. **Discovery** (15 min): Story arc, character development
2. **Research** (15 min): Reference collection, style development
3. **Planning** (20 min): 8-segment breakdown, continuity planning
4. **Technical** (15 min): Frame extraction points, 85/15 mapping
5. **Prompt** (15 min): Detailed prompts with continuation logic
6. **Review** (5 min): Continuity verification
7. **Generate** (5 min per segment): Sequential generation

---

## Critical Success Factors

### What Makes This Different

1. **Intent First**: We understand WHY before HOW
2. **Research Informed**: Decisions based on data, not assumptions
3. **Technically Complete**: Every prompt has full production specs
4. **Quality Gated**: Nothing generates without review
5. **Iterative**: Learn from each generation

### Non-Negotiables

#### Every Prompt Must Include
- Intentional imperfections for realism
- Exposure ratios (2:1 or 4:1)
- Camera lens and aperture
- Atmospheric elements
- 60-30-10 color distribution
- Comprehensive negative instructions

#### Every Project Must Have
- Clear success criteria
- Target audience definition
- Emotional journey map
- Technical specification sheet
- Quality review before generation

---

## Implementation Checklist

### To Implement This Workflow

1. **Create New Agents**
   - [ ] Creative Director Agent
   - [ ] Quality Review Agent

2. **Enhance Existing Agents**
   - [ ] Update veo3-prompt-architect with interview process
   - [ ] Add technical specs to veo3-production-manager
   - [ ] Add quality gates to veo3-api-optimizer

3. **Create Templates**
   - [ ] Discovery interview questions
   - [ ] Technical specification sheet
   - [ ] Quality review checklist
   - [ ] Prompt scoring rubric

4. **Document Best Practices**
   - [ ] Imperfection library
   - [ ] Camera angle guide
   - [ ] Lighting ratio examples
   - [ ] Color palette references

---

## Measurement & Optimization

### Success Metrics

#### Creative Quality
- Emotional impact score (1-10)
- Brand alignment score
- Differentiation score

#### Technical Quality
- Realism score (imperfections present?)
- Cinematic score (proper camera/lighting?)
- Consistency score (character/environment stable?)

#### Efficiency
- Iterations required
- Time to approval
- Credit usage efficiency

### Continuous Improvement
- Document successful prompts
- Track failure patterns
- Update templates based on results
- Share learnings across projects

---

## Quick Start Guide

### For Your Next Project

1. **Stop**: Don't jump to generation
2. **Ask**: What emotion should viewers feel?
3. **Research**: What's working in this space?
4. **Plan**: Storyboard the journey
5. **Specify**: Camera, lighting, imperfections
6. **Engineer**: Craft prompts with all 11 components
7. **Review**: Score against checklist
8. **Generate**: Test cheap, refine, go quality

### The Mindset Shift

**From**: "Generate a video about X"
**To**: "Design an emotional experience that moves viewers from feeling A to feeling B, using specific cinematic techniques"

**From**: "The script will handle it"
**To**: "Agents orchestrate creativity, scripts execute decisions"

**From**: "Good enough prompt"
**To**: "Director-level production brief"

---

## Conclusion

This workflow transforms VEO 3 video creation from mechanical prompt writing to creative filmmaking. By understanding intent, researching context, planning thoroughly, and applying all technical best practices, we create videos that connect emotionally while looking professionally produced.

**Remember**: You're not describing a video—you're designing an experience. Every technical choice (camera angle, lighting ratio, imperfection) serves the emotional journey.

**The Bottom Line**: Great VEO 3 videos come from great creative planning + technical precision + quality control. This workflow ensures all three.