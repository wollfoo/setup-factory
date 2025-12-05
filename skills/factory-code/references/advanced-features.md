# Advanced Features

Extended thinking, prompt caching, checkpointing, and memory management in Factory Code.

## Extended Thinking

Deep reasoning for complex problems.

### Enable Extended Thinking

**Global configuration:**
```bash
Factory config set thinking.enabled true
Factory config set thinking.budget 15000
```

**Project settings (.factory/settings.json):**
```json
{
  "thinking": {
    "enabled": true,
    "budget": 10000,
    "mode": "auto"
  }
}
```

**Command-line flag:**
```bash
Factory --thinking "architect microservices system"
```

### Thinking Modes

**auto**: Factory decides when to use extended thinking
**manual**: User explicitly requests thinking
**disabled**: No extended thinking

```json
{
  "thinking": {
    "mode": "auto",
    "budget": 10000,
    "minComplexity": 0.7
  }
}
```

### Budget Control

Set token budget for thinking:

```json
{
  "thinking": {
    "budget": 10000,      // Max tokens for thinking
    "budgetPerRequest": 5000,  // Per-request limit
    "adaptive": true      // Adjust based on task complexity
  }
}
```

### Best Use Cases

- Architecture design
- Complex algorithm development
- System refactoring
- Performance optimization
- Security analysis
- Bug investigation

### Example

```bash
Factory --thinking "Design a distributed caching system with:
- High availability
- Consistency guarantees
- Horizontal scalability
- Fault tolerance"
```

## Prompt Caching

Reduce costs by caching repeated context.

### Enable Caching

**API usage:**
```typescript
const response = await client.messages.create({
  model: 'Factory-sonnet-4-5-20250929',
  system: [
    {
      type: 'text',
      text: 'You are a coding assistant...',
      cache_control: { type: 'ephemeral' }
    }
  ],
  messages: [...]
});
```

**CLI configuration:**
```json
{
  "caching": {
    "enabled": true,
    "ttl": 300,
    "maxSize": "100MB"
  }
}
```

### Cache Strategy

**What to cache:**
- Large codebases
- Documentation
- API specifications
- System prompts
- Project context

**What not to cache:**
- User queries
- Dynamic content
- Temporary data
- Session-specific info

### Cache Control

```typescript
// Cache large context
{
  type: 'text',
  text: largeCodebase,
  cache_control: { type: 'ephemeral' }
}

// Update without invalidating cache
{
  type: 'text',
  text: newUserQuery
  // No cache_control = not cached
}
```

### Cost Savings

With caching:
- First request: Full cost
- Subsequent requests: ~90% discount on cached tokens
- Cache TTL: 5 minutes

Example:
```
Without caching:
Request 1: 10,000 tokens @ $3/M = $0.03
Request 2: 10,000 tokens @ $3/M = $0.03
Total: $0.06

With caching (8,000 tokens cached):
Request 1: 10,000 tokens @ $3/M = $0.03
Request 2: 2,000 new + 8,000 cached @ $0.30/M = $0.0024
Total: $0.0324 (46% savings)
```

## Checkpointing

Automatically track and rewind changes.

### Enable Checkpointing

```bash
Factory config set checkpointing.enabled true
```

**Settings:**
```json
{
  "checkpointing": {
    "enabled": true,
    "autoSave": true,
    "interval": 300,
    "maxCheckpoints": 50
  }
}
```

### View Checkpoints

```bash
# List checkpoints
Factory checkpoint list

# View checkpoint details
Factory checkpoint show checkpoint-123
```

### Restore Checkpoint

```bash
# Restore to checkpoint
Factory checkpoint restore checkpoint-123

# Restore to time
Factory checkpoint restore --time "2025-11-06T10:00:00Z"

# Restore specific files
Factory checkpoint restore checkpoint-123 --files src/main.js
```

### Create Manual Checkpoint

```bash
# Create checkpoint with message
Factory checkpoint create "before refactoring auth module"

# Create at important moments
Factory checkpoint create "working state before experiment"
```

### Checkpoint Strategies

**Auto-save checkpoints:**
- Before major changes
- After successful tests
- Every N minutes
- Before destructive operations

**Manual checkpoints:**
- Before risky refactors
- At working states
- Before experiments
- After milestones

### Example Workflow

```bash
# Create checkpoint before risky change
Factory checkpoint create "before performance optimization"

# Make changes
Factory "optimize database queries for 10x performance"

# If something breaks
Factory checkpoint restore "before performance optimization"

# Or continue with improvements
Factory checkpoint create "performance optimization complete"
```

## Memory Management

Control how Factory remembers context across sessions.

### Memory Locations

**global**: Share memory across all projects
**project**: Project-specific memory
**none**: Disable memory

```bash
# Set memory location
Factory config set memory.location project

# Enable memory
Factory config set memory.enabled true
```

### Configuration

```json
{
  "memory": {
    "enabled": true,
    "location": "project",
    "ttl": 86400,
    "maxSize": "10MB",
    "autoSummarize": true
  }
}
```

### Memory Operations

```bash
# View stored memories
Factory memory list

# View specific memory
Factory memory show memory-123

# Clear all memories
Factory memory clear

# Clear old memories
Factory memory clear --older-than 7d

# Clear project memories
Factory memory clear --project
```

### What Gets Remembered

**Automatically:**
- Project structure
- Coding patterns
- Preferences
- Common commands
- File locations

**Explicitly stored:**
- Important context
- Design decisions
- Architecture notes
- Team conventions

### Memory Best Practices

**Project memory:**
- Good for project-specific context
- Shares across team members
- Persists in `.factory/memory/`
- Commit to version control (optional)

**Global memory:**
- Personal preferences
- General knowledge
- Common patterns
- Cross-project learnings

**Disable memory when:**
- Working with sensitive data
- One-off tasks
- Testing/experimentation
- Troubleshooting

### Example

```bash
# Remember project architecture
Factory "Remember: This project uses Clean Architecture with:
- Domain layer (core business logic)
- Application layer (use cases)
- Infrastructure layer (external dependencies)
- Presentation layer (API/UI)"

# Factory will recall this in future sessions
Factory "Add a new user registration feature"
# Factory: "I'll implement this following the Clean Architecture..."
```

## Context Windows

Manage large context effectively.

### Maximum Context

Model context limits:
- Factory Sonnet: 200k tokens
- Factory Opus: 200k tokens
- Factory Haiku: 200k tokens

### Context Management

```json
{
  "context": {
    "maxTokens": 200000,
    "autoTruncate": true,
    "prioritize": ["recent", "relevant"],
    "summarizeLong": true
  }
}
```

### Strategies

**Summarization:**
- Auto-summarize old context
- Keep summaries of large files
- Compress conversation history

**Prioritization:**
- Recent messages first
- Most relevant files
- Explicit user priorities

**Chunking:**
- Process large codebases in chunks
- Incremental analysis
- Parallel processing

## See Also

- Pricing: https://docs.Factory.com/about-Factory/pricing
- Token counting: https://docs.Factory.com/build-with-Factory/token-counting
- Best practices: `references/best-practices.md`
- Configuration: `references/configuration.md`
