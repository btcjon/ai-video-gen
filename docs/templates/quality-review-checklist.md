# VEO 3 Prompt Quality Review Checklist

Use this checklist to validate EVERY prompt before generation. No prompt should generate without scoring at least 8/10.

---

## Prompt Information
**Campaign**:
**Scene/Segment**:
**Reviewer**:
**Date**:
**Prompt Version**:

---

## Component Analysis (40% of score)

### Essential Components Present

1. [ ] **Scene Summary** - Clear cinematic moment described
2. [ ] **Subject Description** - Detailed with imperfections
3. [ ] **Background & Context** - Environment fully described
4. [ ] **Action** - Realistic movement for 8 seconds
5. [ ] **Style & Aesthetic** - Cinematic/photorealistic specified
6. [ ] **Camera Instructions** - Lens, aperture, movement, angle
7. [ ] **Composition & Framing** - Shot type defined
8. [ ] **Lighting & Mood** - Exposure ratio, source, atmosphere
9. [ ] **Audio Elements** - Ambient only, no narration
10. [ ] **Color Palette** - 60-30-10 distribution
11. [ ] **Negative Instructions** - Comprehensive list

**Components Score**: ___/11 components present
**Rating**:
- 11/11 = 10 points
- 10/11 = 8 points
- 9/11 = 6 points
- <9/11 = FAIL

---

## Realism Elements (30% of score)

### Imperfection Checklist

**Skin Details**:
- [ ] Pores mentioned explicitly
- [ ] Natural oil/sweat described
- [ ] Texture variations included
- [ ] Subtle blemishes/marks
- [ ] Age-appropriate details

**Hair Details**:
- [ ] Stray hairs specified
- [ ] Natural movement described
- [ ] Texture mentioned
- [ ] Imperfect styling noted

**Environmental**:
- [ ] Dust particles described
- [ ] Atmospheric haze included
- [ ] Natural wear/weathering
- [ ] Realistic materials

**Imperfections Count**: ___/12
**Rating**:
- 10-12 = 10 points
- 7-9 = 7 points
- 4-6 = 5 points
- <4 = FAIL

---

## Technical Precision (20% of score)

### Specifications Checklist

**Camera**:
- [ ] Lens specified (35/50/85/100mm)
- [ ] Aperture defined (F1.4/2.8/4/8)
- [ ] Movement described (dolly/pan/static)
- [ ] Angle defined (low/high/eye-level)

**Lighting**:
- [ ] Exposure ratio (2:1/4:1/8:1)
- [ ] Key light source and direction
- [ ] Fill light described
- [ ] Light motivation clear

**Color**:
- [ ] 60% dominant specified
- [ ] 30% secondary defined
- [ ] 10% accent identified
- [ ] Temperature mentioned

**Technical Count**: ___/12
**Rating**:
- 11-12 = 10 points
- 8-10 = 7 points
- 5-7 = 5 points
- <5 = FAIL

---

## Creative Alignment (10% of score)

### Brief Compliance

- [ ] Matches emotional journey from brief
- [ ] Appropriate for target audience
- [ ] Optimized for specified platform
- [ ] Supports success metrics
- [ ] Differentiates from competition

**Alignment Count**: ___/5
**Rating**:
- 5/5 = 10 points
- 4/5 = 8 points
- 3/5 = 6 points
- <3/5 = FAIL

---

## Critical Failures (Automatic Rejection)

Check for these deal-breakers:

- [ ] ❌ Contains narration (should be post-production only)
- [ ] ❌ Dialogue exceeds 10 words
- [ ] ❌ Missing "(no subtitles)" directive
- [ ] ❌ No imperfections specified
- [ ] ❌ No exposure ratio defined
- [ ] ❌ No atmospheric elements
- [ ] ❌ Vague descriptions ("nice", "good", "beautiful")
- [ ] ❌ Technical specs missing
- [ ] ❌ Doesn't match creative brief

**Any boxes checked = AUTOMATIC FAIL**

---

## Format Validation

### For Paragraph Format:
- [ ] ONE continuous paragraph
- [ ] No bullet points
- [ ] No section breaks
- [ ] All components integrated seamlessly
- [ ] Flows naturally

### For JSON Format (Commercial):
- [ ] Valid JSON structure
- [ ] All required fields present
- [ ] Nested objects correct
- [ ] Values properly formatted

---

## Scoring Summary

### Category Scores
1. **Component Completeness** (40%): ___/10
2. **Realism Elements** (30%): ___/10
3. **Technical Precision** (20%): ___/10
4. **Creative Alignment** (10%): ___/10

### Final Calculation
(Score 1 × 0.4) + (Score 2 × 0.3) + (Score 3 × 0.2) + (Score 4 × 0.1) = **___/10**

### Overall Status
- [ ] **✅ APPROVED** (Score ≥8.0)
- [ ] **⚠️ REVISE** (Score 6.0-7.9)
- [ ] **❌ REJECT** (Score <6.0)

---

## Required Improvements (If Not Approved)

### Missing Elements:
1.
2.
3.

### Specific Revisions Needed:

**Current**:
```
[Paste problematic section]
```

**Suggested**:
```
[Provide improved version]
```

### Priority Fixes:
1. **CRITICAL**:
2. **IMPORTANT**:
3. **NICE TO HAVE**:

---

## Revision Tracking

### Revision 1
- **Issues Fixed**:
- **New Score**: ___/10
- **Status**:

### Revision 2
- **Issues Fixed**:
- **New Score**: ___/10
- **Status**:

---

## Final Approval

**Final Score**: ___/10
**Generation Approved**: Yes / No
**Model Recommendation**: veo3_fast ($0.38) / veo3 ($1.50)
**Approved By**:
**Timestamp**:

---

## Quality Patterns (For Learning)

### What Worked Well:

### Common Issues Found:

### Recommendations for Future:

---

## Quick Reference - Minimum Requirements

Every prompt MUST have:
1. ✓ Imperfections (pores, sweat, stray hair)
2. ✓ Camera specs (lens + aperture + movement)
3. ✓ Exposure ratio (2:1 or 4:1 typical)
4. ✓ Atmospheric elements (dust, haze)
5. ✓ 60-30-10 color distribution
6. ✓ NO narration (ambient only)
7. ✓ "(no subtitles)" included
8. ✓ Comprehensive negative instructions

**Missing ANY = Cannot proceed to generation**

---

## Next Steps

1. **If APPROVED (≥8/10)**: Send to veo3-api-optimizer for generation
2. **If REVISE (6-7.9)**: Return to veo3-prompt-architect with specific improvements
3. **If REJECT (<6)**: Return to veo3-creative-director to clarify intent
4. **Document**: Save to `/production-plans/[campaign]/quality/review-[scene].md`