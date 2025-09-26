# Claude Code: Prompting, Commands & Context Priming Mastery

*Focus on the essentials: How to prompt effectively, create powerful commands, and engineer context like a pro*

---

## The Three Pillars of Claude Code Mastery

This guide focuses on the three most impactful skills for Claude Code:

1. **Effective Prompting** - How to communicate your intent clearly
2. **Custom Commands** - Automating workflows with slash commands
3. **Context Priming** - Managing the context window like an expert

---

## Effective Prompting Strategies

### The Research -> Plan -> Implement Pattern

**Instead of:** "Build a login system"

**Try this pattern:**
```
Phase 1 - Research: "Analyze the current authentication patterns in this codebase. What libraries are used? What's the existing user model structure?"

Phase 2 - Plan: "Based on your analysis, create a comprehensive plan for implementing login functionality. Include component breakdown, API endpoints needed, and database changes."

Phase 3 - Implement: "Now implement the login system according to your plan. Start with the backend API endpoints."
```

**Why this works:** Claude performs dramatically better when it researches and plans before coding.

### Prompting Modes & When to Use Them

**1. Interactive Mode (`claude`)**
- Use for: Complex features, debugging, exploratory work
- Best for: Back-and-forth collaboration, iterative development

**2. Print Mode (`claude -p "prompt"`)**
- Use for: Single, focused tasks with clear output
- Best for: Code analysis, quick fixes, one-shot operations

**3. Continue Mode (`claude -c`)**
- Use for: Picking up where you left off
- Best for: Long-running projects, maintaining context

### Prompting Best Practices

**Be Specific About Context:**
```bash
# Vague
claude "Fix the bug in the API"

# Specific
claude "There's a 500 error in the user registration endpoint. The error message is 'Cannot read property of undefined'. Analyze the registration flow and fix the issue."
```

**Use the @ Syntax for File References:**
```bash
# Instead of asking Claude to find files
claude "Look at the auth files and update them"

# Reference specific files directly
claude "Review @src/auth/login.ts and @src/auth/register.ts, then implement password reset functionality following the same patterns"
```

**Provide Examples When Possible:**
```bash
claude "Create a React component for user profiles. Follow the same pattern as @src/components/UserCard.tsx but add edit capabilities"
```

---

## Custom Slash Commands Deep Dive

Custom commands are your secret weapon for automating repetitive workflows. They live in Markdown files and can be incredibly powerful.

### Command Scope Strategy

**When to use each scope:**

| Scope | Location | Best For | Example Commands |
|-------|----------|----------|------------------|
| **Project Shared** | `.claude/commands/` (committed) | Team workflows, deployment, code review | `/deploy`, `/review-pr`, `/setup-env` |
| **User Global** | `~/.claude/commands/` | Personal productivity, cross-project tools | `/my-setup`, `/quick-test`, `/analyze-logs` |

### Command Structure Breakdown

Every command file has this structure:
```markdown
---
name: Command Name
allowed-tools: Bash, Read, Write  # Tools the command can use
description: What this command does
argument-hint: [optional-args]    # Help text for arguments
model: claude-3-5-haiku-20241022  # Override default model
---

# Command Documentation

Your instructions go here. Use:
- $ARGUMENTS for all arguments
- $1, $2, $3 for positional arguments
- @path/to/file to include file contents
- !command to run bash commands
```

### Real-World Command Examples

**1. Code Review Command** (`.claude/commands/review.md`):
```markdown
---
name: Code Review
allowed-tools: Read, Bash, Write
description: Comprehensive code review with security and performance analysis
argument-hint: [file-or-directory]
---

# Code Review Command

Perform a thorough code review focusing on:

## Process
1. Read all files in $ARGUMENTS
2. Analyze for:
   - Logic errors and bugs
   - Security vulnerabilities
   - Performance issues
   - Code quality and maintainability
3. Run linting: !npm run lint $ARGUMENTS
4. Check tests: !npm test -- --testPathPattern=$ARGUMENTS
5. Generate review report

## Output Format
- **Critical Issues**: Security vulnerabilities, breaking bugs
- **Performance**: Optimization opportunities
- **Code Quality**: Style, readability, maintainability
- **Recommendations**: Specific actionable improvements
```

**2. Smart Deployment Command** (`.claude/commands/deploy.md`):
```markdown
---
name: Smart Deploy
allowed-tools: Bash, Read
description: Deploy with safety checks and rollback capability
argument-hint: [environment] [branch]
model: claude-3-5-sonnet-20241022
---

# Smart Deploy

Deploy $2 branch to $1 environment with safety checks.

## Pre-Deploy Checks
1. Verify branch exists: !git show-ref --verify refs/heads/$2
2. Check environment config: @config/$1.env
3. Run test suite: !npm run test:$1
4. Check for breaking changes: !git diff --name-only $1-deployed..$2

## Deploy Process
1. Create backup tag: !git tag backup-$1-$(date +%Y%m%d-%H%M%S) $1-deployed
2. Deploy to $1: !./scripts/deploy.sh $1 $2
3. Health check: !curl -f https://$1.example.com/health
4. Update deployed branch: !git branch -f $1-deployed $2

## Rollback Plan
If deployment fails:
!./scripts/rollback.sh $1 backup-$1-$(date +%Y%m%d-%H%M%S)
```

**3. Context Analysis Command** (`~/.claude/commands/analyze-context.md`):
```markdown
---
name: Analyze Context
allowed-tools: Read, Bash
description: Analyze current context usage and suggest optimizations
---

# Context Analysis

Analyze the current context window usage and suggest optimizations.

## Analysis Steps
1. Check context usage: Use `/cost` command
2. Review CLAUDE.md size: !wc -c CLAUDE.md 2>/dev/null || echo "No CLAUDE.md"
3. Check MCP servers: !ls .mcp.json 2>/dev/null || echo "No MCP config"
4. List memory files: !ls -la .claude/memory/ 2>/dev/null || echo "No memory files"

## Recommendations
Based on the analysis, provide specific recommendations:
- CLAUDE.md optimization opportunities
- MCP server usage efficiency
- Memory file cleanup suggestions
- Context priming alternatives

## Action Items
Generate specific commands to optimize context usage.
```

### Advanced Command Techniques

**Environment Variable Usage:**
```markdown
# In your command, reference environment variables
Deploy to: ${ENVIRONMENT:-staging}
Database URL: ${DATABASE_URL}
API Key: ${API_KEY:-development-key}
```

**Conditional Logic:**
```markdown
## Conditional Deployment
If $1 equals "production":
  - Require manual confirmation
  - Run full test suite
  - Create detailed changelog
Else:
  - Quick deployment to staging
  - Basic smoke tests
```

**File Processing Loops:**
```markdown
## Process Multiple Files
For each file in $ARGUMENTS:
1. Read file: @$file
2. Run analysis
3. Generate report: Write to reports/$file-analysis.md
4. Continue to next file
```

---

## Context Priming Mastery

This is where the magic happens. Context priming is about setting up Claude's context window strategically instead of relying on static files.

### The Problem with Traditional Approaches

**CLAUDE.md Issues:**
- Always-on context that can't be controlled
- Files only grow over time, never shrink
- Consumes 10-25% of context window constantly
- Not dynamic or task-specific

**The Solution: Context Priming Commands**

Instead of static memory files, use specialized `/prime` commands that load context dynamically based on the specific task.

### Context Priming Strategy

**Replace this:**
```markdown
<!-- Large CLAUDE.md file -->
# Project Overview
[5000 words about everything]

# Architecture
[3000 words about system design]

# Coding Standards
[2000 words about style]

# Dependencies
[1000 words about packages]
```

**With targeted primers:**
```bash
/prime-feature    # Load context for feature development
/prime-bug        # Load context for debugging
/prime-refactor   # Load context for refactoring
/prime-deploy     # Load context for deployment
```

### Example Context Priming Commands

**1. Feature Development Primer** (`.claude/commands/prime-feature.md`):
```markdown
---
name: Prime Feature
description: Prime Claude for new feature development with relevant context
allowed-tools: Read
---

# Feature Development Context Primer

## Purpose
Set up Claude's context specifically for building new features with clean architecture.

## Context Loading
1. **Architecture Overview**: @docs/architecture.md
2. **Component Patterns**: @src/components/README.md
3. **API Standards**: @docs/api-design.md
4. **Testing Patterns**: @src/__tests__/examples/

## Current Focus
You are now primed for feature development. Follow these principles:

### Architecture
- Use established component patterns from existing code
- Follow the API design standards
- Maintain separation of concerns
- Consider mobile-first responsive design

### Implementation Approach
1. **Plan First**: Break down feature into components
2. **Start Small**: Build core functionality first
3. **Test Early**: Write tests alongside implementation
4. **Document**: Update relevant docs as you build

### Code Quality
- Follow existing naming conventions
- Use TypeScript strictly
- Handle errors gracefully
- Optimize for readability

## Ready State
Claude is now focused on feature development with the right context loaded. Proceed with your feature request.
```

**2. Bug Fixing Primer** (`.claude/commands/prime-bug.md`):
```markdown
---
name: Prime Bug
description: Prime Claude for debugging with diagnostic context
allowed-tools: Read, Bash
---

# Bug Fixing Context Primer

## Purpose
Set up Claude's context for systematic debugging and issue resolution.

## Diagnostic Context Loading
1. **Error Logs**: !tail -100 logs/error.log 2>/dev/null || echo "No error logs"
2. **Recent Changes**: !git log --oneline -10
3. **Test Status**: !npm test -- --reporter=json | jq '.numFailedTests' 2>/dev/null || echo "No test data"
4. **System Health**: !ps aux | grep node && df -h

## Debugging Methodology
Now primed for systematic debugging:

### Investigation Process
1. **Reproduce**: Understand the exact steps to trigger the bug
2. **Isolate**: Identify which component/function is affected
3. **Analyze**: Review recent changes and related code
4. **Hypothesize**: Form theories about the root cause
5. **Test**: Validate hypotheses with targeted fixes

### Tools Available
- Error logging and stack traces
- Git history for recent changes
- Test suite for regression checking
- Browser dev tools for frontend issues

## Debugging Mindset
- Start with the error message and work backwards
- Check recent changes first (likely culprits)
- Use git bisect for hard-to-find regressions
- Write tests to prevent similar bugs

## Ready State
Claude is now focused on debugging with diagnostic context loaded. Describe the bug you need fixed.
```

**3. Refactoring Primer** (`.claude/commands/prime-refactor.md`):
```markdown
---
name: Prime Refactor
description: Prime Claude for code refactoring with quality context
allowed-tools: Read, Bash
---

# Refactoring Context Primer

## Purpose
Set up Claude for safe, systematic code refactoring.

## Code Quality Context
1. **Current Code Structure**: !find src -name "*.ts" -o -name "*.tsx" | head -20
2. **Dependencies**: @package.json
3. **Test Coverage**: !npm run test:coverage 2>/dev/null || echo "No coverage data"
4. **Lint Status**: !npm run lint 2>/dev/null || echo "No lint data"

## Refactoring Principles
Now primed for systematic refactoring:

### Safety First
- Run full test suite before starting
- Make small, incremental changes
- Commit frequently with descriptive messages
- Keep existing API contracts intact

### Code Quality Goals
- Reduce complexity and duplication
- Improve readability and maintainability
- Follow established patterns
- Enhance type safety

### Refactoring Process
1. **Understand**: Analyze current code thoroughly
2. **Plan**: Design the improved structure
3. **Test**: Ensure comprehensive test coverage
4. **Refactor**: Make incremental improvements
5. **Verify**: Run tests and manual verification

## Ready State
Claude is now focused on refactoring with quality context loaded. Specify what code needs refactoring.
```

### Context Priming Best Practices

**1. Keep Primers Focused**
Each primer should load only the context needed for that specific type of work.

**2. Use Dynamic Loading**
Load current system state, recent logs, test results - not just static documentation.

**3. Set the Right Mindset**
Each primer should put Claude in the right "mode" for the task type.

**4. Include Current State**
Always include recent changes, current status, and relevant system information.

**5. Provide Clear Next Steps**
End each primer with clear expectations and next steps.

### Token Savings with Context Priming

**Traditional Approach:**
- CLAUDE.md: 23,000 tokens (always loaded)
- Total context used: 23,000+ tokens

**Context Priming Approach:**
- Prime command: ~350 tokens
- Relevant context: ~3,000 tokens
- Total context used: ~3,350 tokens
- **Savings: 85% reduction in context usage**

---

## Putting It All Together: Advanced Workflows

### Workflow 1: Feature Development

```bash
# Step 1: Prime for feature work
/prime-feature

# Step 2: Research and plan
"Analyze the current user management system and create a plan for adding user roles and permissions"

# Step 3: Implement iteratively
"Implement the backend API for user roles following your plan"

# Step 4: Test and refine
"Write comprehensive tests for the role system and fix any issues"

# Step 5: Deploy with custom command
/deploy staging feature/user-roles
```

### Workflow 2: Bug Investigation

```bash
# Step 1: Prime for debugging
/prime-bug

# Step 2: Describe the issue
"Users are reporting 500 errors when trying to update their profile. The error happens intermittently and the logs show 'Cannot read property of undefined'"

# Step 3: Systematic debugging
# (Claude will use the debugging methodology from the primer)

# Step 4: Test fix
"Run the full test suite and verify the fix resolves the issue without breaking anything else"
```

### Workflow 3: Code Quality Improvement

```bash
# Step 1: Analyze context usage
/analyze-context

# Step 2: Prime for refactoring
/prime-refactor

# Step 3: Review code quality
/review src/components/UserProfile/

# Step 4: Implement improvements
"Based on the review, refactor the UserProfile component to improve maintainability and performance"
```

---

## Measuring Success

### Context Efficiency Metrics
```bash
# Check your context usage regularly
/cost

# Look for these improvements:
# - Lower token usage per task
# - Faster response times
# - More focused, relevant responses
```

### Command Effectiveness
Track how often you use custom commands vs writing prompts from scratch. High command usage = good automation.

### Quality Indicators
- Fewer iterations needed to get desired results
- More consistent code quality across sessions
- Faster onboarding of new team members

---

## Quick Reference

### Essential Commands to Create First
```bash
# Create these in .claude/commands/
1. /prime-feature      # Feature development context
2. /prime-bug         # Debugging context
3. /review            # Code review workflow
4. /quick-test        # Run relevant tests
5. /analyze-context   # Context usage analysis
```

### Daily Workflow Pattern
```bash
1. Start with context priming: /prime-[task-type]
2. Use specific, research-first prompts
3. Leverage @ syntax for file references
4. Check context usage: /cost
5. Use custom commands for repetitive tasks
```

### Context Optimization Checklist
- [ ] Replace large CLAUDE.md with targeted primers
- [ ] Remove unused MCP servers
- [ ] Use subagents for delegated work
- [ ] Monitor token usage with /cost
- [ ] Create task-specific custom commands

---

## Key Takeaways

1. **Context is Your Most Precious Resource** - Manage it ruthlessly
2. **Focused Agents Outperform Generalists** - Use context priming to create specialized sessions
3. **Research -> Plan -> Implement** - This pattern dramatically improves code quality
4. **Custom Commands = Automation Gold** - Invest time in creating reusable workflows
5. **Measure and Optimize** - Use /cost to track context efficiency

The difference between good and great Claude Code usage is mastering these three areas: strategic prompting, powerful custom commands, and expert-level context priming.