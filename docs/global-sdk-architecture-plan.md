# Global SDK Architecture Plan
**Making universal scripts and workflows available across all projects**

## Problem Statement

Currently:
- Global scripts exist at `/home/dev/.claude/scripts/` but documentation is duplicated
- Each project CLAUDE.md file repeats full API documentation
- Workflows (e.g., prompt enhancement → generation) are not standardized
- Context windows get bloated with repeated documentation
- Updates require editing multiple files

## Solution: Ultra-Minimal Architecture

**Principle**: Absolute minimal context, zero duplication, on-demand everything

### Two-Tier Documentation System

1. **Global CLAUDE.md** (`/home/dev/.claude/CLAUDE.md`)
   - Lists available scripts (3 lines)
   - Shows import pattern (2 lines)
   - Points to docstrings for details (1 line)
   - **Total: ~10 lines**

2. **Script Docstrings** (in the `.py` files themselves)
   - Comprehensive API documentation
   - Workflow rules (e.g., "always enhance prompts")
   - Usage examples, parameters, return values
   - Claude reads with Read tool **only when using that script**

**Project CLAUDE.md**: No SDK section needed (global CLAUDE.md always loaded automatically)

## Implementation Plan

### Phase 1: Enhance Script Docstrings (Self-Documenting Code)

**Goal**: Make scripts fully self-documenting so Claude can read them on-demand

**Files to update**:
- `/home/dev/.claude/scripts/kie_client.py`
- `/home/dev/.claude/scripts/openai_image_client.py`
- `/home/dev/.claude/scripts/nano_banana_client.py`

**Pattern for each script**:
```python
"""
{ScriptName} - {One-line purpose}

WORKFLOW RULES:
    - ALWAYS enhance prompts before generation (use /imgen-prompt or veo3-prompt-architect agent)
    - Never skip enhancement - raw prompts = poor results / wasted money
    - When in doubt, enhance

QUICK START:
    import sys
    sys.path.append('/home/dev/.claude/scripts')
    from {module} import {ClassName}

    # Step 1: Enhance prompt first
    # For images: Use /imgen-prompt slash command
    # For video: Use veo3-prompt-architect agent

    # Step 2: Generate with enhanced prompt
    client = {ClassName}()
    result = client.main_method(prompt="[ENHANCED_PROMPT]", ...)

COMMON WORKFLOWS:
    # Workflow 1: Single generation
    [Example with prompt enhancement step]

    # Workflow 2: Multi-step (e.g., frame-to-frame)
    [Example with enhancement → generate → extract pattern]

    # Workflow 3: Compositing
    [Example with generate → composite pattern]

DEFAULT OUTPUTS:
    - Where files are saved
    - Naming conventions

PARAMETERS:
    method_name():
        param1: Description, type, default
        param2: Description, type, default

RETURN VALUES:
    dict: {
        'success': bool,
        'file_path': Path or str,
        'other_keys': descriptions
    }

FULL DOCUMENTATION:
    [Detailed API reference]
"""
```

### Phase 2: Create Minimal Global Quick Reference

**File**: `/home/dev/.claude/CLAUDE.md`

**Add this section** (keep existing user preferences):

```markdown
## Global Scripts Available
**Location**: `/home/dev/.claude/scripts/`

- kie_client.py - VEO 3 video generation
- openai_image_client.py - DALL-E 3 images
- nano_banana_client.py - Gemini images

**Import pattern**:
```python
import sys
sys.path.append('/home/dev/.claude/scripts')
from kie_client import KieClient
```

**Documentation**: Read script files for complete API, workflows, and examples.
```

**Total: ~10 lines**

**That's it!** All workflows, rules, and detailed documentation live in the script docstrings.

### Phase 3: Update Project CLAUDE.md Files

**Rule**: Projects automatically read `/home/dev/.claude/CLAUDE.md` - no need to reference it!

**Only add SDK info if project heavily uses these scripts:**

```markdown
# {Project Name}
{Project description}

## Scripts Used
- kie_client.py for video generation
- openai_image_client.py for image compositing

## {Project-specific instructions}
```

**If project doesn't use SDK**: Don't mention it at all. Claude will discover via global CLAUDE.md if needed.

**For ai-video-gen project specifically**:
- Keep 7 Critical Rules section
- Keep project-specific frame-to-frame workflow details
- Remove duplicated script API documentation
- Remove pointer to global CLAUDE.md (redundant - it's always loaded)
- Just mention which scripts are used (kie_client, openai_image_client)

### Phase 4: Slash Commands (Completed)

**Status**: Removed `/imgen-oai` and `/imgen-nano` commands

**Rationale**:
- Python clients are more reliable and flexible
- Slash commands had limitations (size format issues, complex workflows)
- Reduces maintenance and confusion (one way to do things)
- Script docstrings provide comprehensive documentation

**Kept**: `/imgen-prompt` - Essential workflow tool for prompt enhancement

## Architecture Benefits

### Context Efficiency
- ✅ Global CLAUDE.md: ~10 lines total (just "what exists" + import pattern)
- ✅ Project CLAUDE.md: Only project-specific content (no SDK reference needed)
- ✅ Detailed docs: On-demand via Read tool when script is used
- ❌ NO separate documentation files loaded every time
- ✅ Zero context bloat - workflows live with implementation

### Maintainability
- ✅ Update script docstrings → All projects benefit automatically
- ✅ Workflows documented once in script they apply to
- ✅ No duplicated documentation across projects
- ✅ Self-documenting code = docs stay in sync

### Discoverability
- ✅ Claude reads global CLAUDE.md automatically (sees available scripts)
- ✅ Knows how to import scripts
- ✅ Reads script docstrings when using that tool (gets workflows + API)
- ✅ No need for projects to reference SDK (global CLAUDE.md always loaded)

### Workflow Automation
- ✅ Workflows documented in script docstrings (loaded when needed)
- ✅ Claude reads "WORKFLOW RULES" section → follows automatically
- ✅ Reduces errors (enhancement rules in docstring)
- ✅ Consistent results across projects

## Success Metrics

After implementation:
1. **Context Usage**: Global CLAUDE.md SDK section = ~10 lines
2. **Zero Duplication**: No repeated script docs across projects
3. **Automatic Workflows**: Claude reads docstring → follows workflow rules
4. **Easy Updates**: Change script docstring → All projects updated
5. **New Projects**: Zero setup - global CLAUDE.md automatically loaded

## Implementation Checklist

- [ ] **Phase 1**: Enhance script docstrings (kie_client.py, openai_image_client.py, nano_banana_client.py)
- [ ] **Phase 2**: Add Global SDK section to `/home/dev/.claude/CLAUDE.md`
- [ ] **Phase 3**: Update project CLAUDE.md files (starting with ai-video-gen)
- [ ] **Phase 4**: Optional - Update slash commands for workflow awareness
- [ ] **Test**: Verify Claude can access scripts and follow workflows in new conversation
- [ ] **Template**: Create project CLAUDE.md template for future projects

## Next Steps

1. Review this plan
2. Approve implementation approach
3. Execute phases in order
4. Test in current project
5. Roll out to other projects

## Notes

- Keep global CLAUDE.md concise (fight context bloat)
- Script docstrings can be comprehensive (only loaded on-demand)
- Project CLAUDE.md = global reference + project specifics
- Workflows documented once, executed automatically
- New scripts = add to global quick reference list + comprehensive docstring
