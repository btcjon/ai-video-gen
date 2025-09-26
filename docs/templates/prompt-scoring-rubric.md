# VEO 3 Prompt Scoring Rubric

Detailed scoring guide for evaluating prompt quality. Use this to ensure consistent, objective assessment across all prompts.

---

## Scoring Categories & Weights

1. **Technical Completeness** (40%)
2. **Realism Elements** (30%)
3. **Technical Precision** (20%)
4. **Creative Alignment** (10%)

**Minimum Score to Generate**: 8.0/10

---

## 1. TECHNICAL COMPLETENESS (40% Weight)

### 10/10 - Exceptional
- ALL 11 components present and detailed
- Each component enhances the others
- Professional cinematography language throughout
- Could be used as production brief

### 8/10 - Strong
- 10-11 components present
- Most components well-detailed
- Clear technical language
- Minor gaps don't affect generation

### 6/10 - Adequate
- 8-9 components present
- Basic details provided
- Some technical language
- Notable gaps but workable

### 4/10 - Weak
- 6-7 components present
- Minimal detail
- Vague descriptions
- Major gaps affecting quality

### 2/10 - Poor
- <6 components present
- Very vague
- Missing critical elements
- Would generate generic video

### 0/10 - Fail
- Missing majority of components
- No technical detail
- Cannot generate quality video

---

## 2. REALISM ELEMENTS (30% Weight)

### 10/10 - Exceptional
```
Examples of 10/10 realism:
- "Visible pores with natural oil sheen on forehead, few stray hairs escaping from ponytail catching backlight"
- "Dust particles dancing in volumetric light rays through window, creating depth"
- "Fabric showing natural wrinkles at elbows, slight thread wear at collar"
```

### 8/10 - Strong
- 8+ imperfection types specified
- Natural human details clear
- Environmental atmosphere rich
- Materials show wear/texture

### 6/10 - Adequate
- 5-7 imperfection types
- Some human details
- Basic atmosphere mentioned
- Some material realism

### 4/10 - Weak
- 3-4 imperfection types
- Minimal human details
- Little atmosphere
- Generic materials

### 2/10 - Poor
- 1-2 imperfections mentioned
- Too perfect/artificial
- No atmospheric elements
- Flat, CG-like description

### 0/10 - Fail
- No imperfections
- Completely artificial
- No environmental detail
- Would look like animation

---

## 3. TECHNICAL PRECISION (20% Weight)

### 10/10 - Exceptional
```
Example of 10/10 precision:
"Shot with 85mm lens at F2.8 creating shallow depth of field, slow dolly in emphasizing intimacy. Key light from window creates 4:1 exposure ratio with warm 3200K temperature against cool 5600K fill, dust particles visible in light beam."
```

### 8/10 - Strong
**Camera**: Lens + aperture + movement specified
**Lighting**: Ratio + source + quality defined
**Color**: Full 60-30-10 breakdown
**All specs serve creative purpose**

### 6/10 - Adequate
**Camera**: Most specs present
**Lighting**: Ratio OR source defined
**Color**: Basic palette mentioned
**Some technical gaps**

### 4/10 - Weak
**Camera**: Minimal specs
**Lighting**: Vague ("soft lighting")
**Color**: Generic description
**Many technical gaps**

### 2/10 - Poor
**Camera**: No specs
**Lighting**: Very vague
**Color**: Not mentioned
**Lacks technical detail**

### 0/10 - Fail
- No technical specifications
- Would generate random results

---

## 4. CREATIVE ALIGNMENT (10% Weight)

### 10/10 - Exceptional
- Perfect emotional journey match
- Ideal for exact target audience
- Platform optimization perfect
- Clear USP communication
- Exceeds brief requirements

### 8/10 - Strong
- Good emotional alignment
- Appropriate for audience
- Platform considered
- USP present
- Meets brief requirements

### 6/10 - Adequate
- Basic emotional alignment
- Generally appropriate
- Some platform consideration
- USP somewhat clear
- Mostly meets brief

### 4/10 - Weak
- Weak emotional connection
- Audience mismatch possible
- Platform ignored
- USP unclear
- Partially meets brief

### 2/10 - Poor
- Wrong emotional tone
- Wrong audience
- No platform optimization
- No USP
- Doesn't meet brief

### 0/10 - Fail
- Completely misaligned
- Would not achieve goals

---

## SCORING MATRIX

| Component | Weight | Your Score | Weighted |
|-----------|--------|------------|----------|
| Technical Completeness | 40% | ___/10 | ___ |
| Realism Elements | 30% | ___/10 | ___ |
| Technical Precision | 20% | ___/10 | ___ |
| Creative Alignment | 10% | ___/10 | ___ |
| **TOTAL** | 100% | | **___/10** |

---

## AUTOMATIC FAILURE CONDITIONS

Any of these = 0/10 Overall:
- ❌ Contains narration voice
- ❌ No imperfections at all
- ❌ No camera specifications
- ❌ No lighting information
- ❌ Completely misses creative brief

---

## SCORE INTERPRETATION

### 9.0-10.0: EXCEPTIONAL
- Generate immediately with veo3 ($1.50)
- Archive as reference example
- Share as best practice

### 8.0-8.9: STRONG
- Approved for generation
- Use veo3_fast first, then veo3
- Minor improvements optional

### 7.0-7.9: NEEDS IMPROVEMENT
- Identify 2-3 key improvements
- Quick revision required
- Re-score after changes

### 6.0-6.9: SIGNIFICANT GAPS
- Major revision needed
- Return to architect
- List specific requirements

### Below 6.0: REJECT
- Fundamental issues
- Return to creative director
- Needs complete rework

---

## SCORING EXAMPLES

### Example 1: High-Scoring Prompt (9.2/10)
```
"Middle-aged father with visible worry lines and stubble, sweat beading on forehead with visible pores, checking emergency supplies in garage. Shot with 50mm lens at F2.8, slow push-in dolly revealing concern. Natural light from garage door creates 4:1 exposure ratio, dust particles visible in light beam. 60% warm earth tones from wooden shelves, 30% cool concrete gray, 10% red emergency kit accent. Ambient garage sounds, no narration (no subtitles). Avoid perfect skin, CGI look."
```
- Technical: 10/10 (all components)
- Realism: 9/10 (excellent imperfections)
- Precision: 9/10 (detailed specs)
- Creative: 8/10 (matches brief)

### Example 2: Low-Scoring Prompt (4.5/10)
```
"Man looking at supplies in garage. Nice lighting. Professional video quality. Make it look good and realistic."
```
- Technical: 3/10 (missing most)
- Realism: 2/10 (no imperfections)
- Precision: 2/10 (no specs)
- Creative: 5/10 (vague match)

---

## IMPROVEMENT GUIDE

### To Improve Technical Completeness:
- Add missing components
- Expand descriptions
- Use cinematography terms
- Include all 11 elements

### To Improve Realism:
- Add skin imperfections
- Include stray hairs
- Describe atmosphere
- Add material texture

### To Improve Precision:
- Specify exact lens (mm)
- Define aperture (F-stop)
- State exposure ratio
- Detail color percentages

### To Improve Creative Alignment:
- Review creative brief
- Match emotional journey
- Consider platform needs
- Emphasize USP

---

## CALIBRATION NOTES

### Common Scoring Mistakes:
1. Being too lenient on imperfections
2. Accepting vague lighting descriptions
3. Not penalizing missing camera specs
4. Overlooking creative misalignment

### Scoring Consistency Tips:
1. Always check against creative brief first
2. Count imperfections explicitly
3. Look for specific numbers (mm, F-stop, ratios)
4. Evaluate if prompt could be filmed exactly as written

---

## Document & Learn

After scoring each prompt:
1. Note what raised the score
2. Identify what lowered it
3. Document patterns
4. Share successful examples
5. Update rubric if needed

**Save scores to**: `/production-plans/[campaign]/quality/scores.md`