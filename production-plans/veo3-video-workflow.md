# VEO 3 Video Creation Workflow

## Quick Start Command
```bash
# Simple video generation
"Create a TikTok video about [YOUR IDEA]"

# The agents will handle everything automatically
```

## Essential Information to Collect

### 1. **Core Video Concept** (Required)
- **What**: The main idea or story you want to tell
- **Example**: "A chef making sushi with dramatic knife skills"

### 2. **Target Platform** (Recommended)
- **TikTok**: Vertical (9:16), high energy, 8 seconds
- **Instagram Reels**: Vertical (9:16), polished aesthetic, 8 seconds
- **YouTube Shorts**: Vertical (9:16), informative, 8 seconds
- **General**: Horizontal (16:9), cinematic, 8 seconds
- **Default**: If not specified, creates horizontal cinematic

### 3. **Visual Style** (Optional)
- **Cinematic**: Professional film look (default)
- **Commercial**: Product-focused, premium
- **Social Media**: Vibrant, engaging
- **Documentary**: Realistic, informative
- **Horror/Comedy/etc**: Genre-specific moods

### 4. **Production Type** (Optional)
- **Single Video**: One-off creation
- **Series**: Multiple related videos with consistency
- **Campaign**: Brand/product variations
- **Batch**: Multiple unrelated videos

### 5. **Character Requirements** (If Applicable)
- **No Characters**: Default landscapes/objects
- **Single Character**: Describe once, reuse
- **Multiple Characters**: Specify each character
- **Consistent Character**: Same character across scenes

## Workflow Process

### Step 1: Information Gathering
```yaml
Minimum Required:
- Video idea/concept

Automatic Defaults:
- Platform: General (16:9 horizontal)
- Style: Cinematic
- Quality: High (veo3 model)
- Duration: 8 seconds
```

### Step 2: Prompt Generation
The **veo3-prompt-architect** agent automatically:
1. Expands your simple idea
2. Adds 10 essential components
3. Optimizes for target platform
4. Includes negative instructions
5. Formats for Kie.ai API

### Step 3: Production Management
The **veo3-production-manager** agent handles:
1. Project organization
2. Scene sequencing (if series)
3. Character consistency tracking
4. Batch coordination
5. Output organization

### Step 4: API Execution
The **veo3-api-optimizer** agent manages:
1. Cost optimization (veo3 vs veo3_fast)
2. API calls to Kie.ai
3. Progress monitoring
4. Error recovery
5. Video download

### Step 5: Delivery
- Video saved to organized project folder
- Metadata and analytics provided
- Ready for post-production editing

## Usage Examples

### Example 1: Simple TikTok Video
```
User: "Create a TikTok video about a barista making latte art"

System automatically:
- Platform: TikTok (9:16 vertical)
- Style: Social media engaging
- Energy: High
- Duration: 8 seconds
- Cost: $0.38 (fast mode for social)
```

### Example 2: Professional Commercial
```
User: "Create a Nike commercial showing shoes being assembled"

System automatically:
- Platform: General (16:9 horizontal)
- Style: Commercial premium
- Quality: High (veo3)
- Watermark: Nike
- Cost: $1.50 (quality mode)
```

### Example 3: Video Series with Character
```
User: "Create a 3-part Instagram series about a chef's morning routine"

System handles:
- Character consistency across videos
- Platform optimization for Instagram
- Series coordination
- Total cost: $1.14 (3 x $0.38)
```

### Example 4: Batch Social Media Content
```
User: "Create social media videos for: morning coffee, workout, sunset"

System processes:
- 3 separate videos
- Platform detection per video
- Batch optimization
- Cost efficiency through grouping
```

## Interactive Prompts

The workflow can ask clarifying questions:

```
Assistant: I'll create your video! Quick questions:
1. Which platform? (TikTok/Instagram/YouTube/General)
2. Any specific style? (or I'll choose best match)
3. Single video or series?

Or just say "surprise me" and I'll optimize automatically!
```

## Cost Breakdown

| Video Type | Model | Cost | Use Case |
|------------|-------|------|----------|
| Social Media | veo3_fast | $0.38 | TikTok, Reels, Shorts |
| Professional | veo3 | $1.50 | Commercials, Brand |
| Test/Preview | veo3_fast | $0.38 | Iteration, Testing |
| Final/Hero | veo3 | $1.50 | High-quality output |

## Advanced Options

### Character Consistency Workflow
```
1. Generate character with green screen
2. Reuse across multiple scenes
3. Maintain description consistency
4. Track character metadata
```

### Campaign Management
```
1. Define brand and concept
2. Create variations
3. A/B testing versions
4. Analytics and reporting
```

### Platform Optimization
```
TikTok: viral, trending, engaging
Instagram: aesthetic, polished, stylish
YouTube: informative, clear, educational
```

## Quick Commands

```bash
# Fastest generation
"Quick TikTok about [idea]"

# High quality
"Professional video about [idea]"

# Series
"Create 5 Instagram videos about [topic]"

# With character
"Video series with consistent character doing [actions]"

# Commercial
"[Brand] commercial showing [concept]"
```

## Error Handling

The system automatically handles:
- API failures (fallback protection)
- Rate limiting (queue management)
- Generation failures (retry logic)
- Quality issues (parameter adjustment)

## Output Structure

```
project_name_timestamp/
├── raw_videos/         # Original downloads
├── vertical_content/   # Platform-specific
│   ├── tiktok/
│   ├── instagram/
│   └── youtube/
├── commercial_content/ # Brand videos
├── metadata/          # Analytics & reports
└── project_info.json  # Configuration
```

## Tips for Best Results

1. **Be Specific**: "chef making sushi" > "cooking video"
2. **Mention Platform**: Enables automatic optimization
3. **Describe Style**: Helps set mood and tone
4. **Use Series**: For consistent narratives
5. **Batch Similar**: Group related videos for efficiency

## Minimum Viable Request

```
"Make a video about [anything]"
```

The system will:
- Create cinematic horizontal video
- Use quality mode
- Apply best practices
- Deliver in ~2-5 minutes

## Complete Request Example

```
"Create a viral TikTok video series (3 parts) about a robot learning to dance,
with consistent character, high energy, neon aesthetic, for a tech brand campaign"
```

System handles:
- 3 videos with same robot character
- Vertical 9:16 format
- TikTok optimization
- Neon visual style
- Brand watermark
- Series coordination
- Cost: $1.14 total