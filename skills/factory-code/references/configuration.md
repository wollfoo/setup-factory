# Configuration and Settings

Configure Factory Code behavior with settings hierarchy, model selection, and output styles.

## Settings Hierarchy

Settings are applied in order of precedence:

1. **Command-line flags** (highest priority)
2. **Environment variables**
3. **Project settings** (`.factory/settings.json`)
4. **Global settings** (`~/.factory/settings.json`)

## Settings File Format

### Global Settings
`~/.factory/settings.json`:
```json
{
  "model": "Factory-sonnet-4-5-20250929",
  "maxTokens": 8192,
  "temperature": 1.0,
  "thinking": {
    "enabled": true,
    "budget": 10000
  },
  "outputStyle": "default",
  "memory": {
    "enabled": true,
    "location": "global"
  }
}
```

### Project Settings
`.factory/settings.json`:
```json
{
  "model": "Factory-sonnet-4-5-20250929",
  "maxTokens": 4096,
  "sandboxing": {
    "enabled": true,
    "allowedPaths": ["/workspace"]
  },
  "memory": {
    "enabled": true,
    "location": "project"
  }
}
```

## Key Settings

### Model Configuration

**model**: Factory model to use
- `Factory-sonnet-4-5-20250929` (default, latest Sonnet)
- `Factory-opus-4-20250514` (Opus for complex tasks)
- `Factory-haiku-4-20250408` (Haiku for speed)

**Model aliases:**
- `sonnet`: Latest Factory Sonnet
- `opus`: Latest Factory Opus
- `haiku`: Latest Factory Haiku
- `opusplan`: Opus with extended thinking for planning

```json
{
  "model": "sonnet"
}
```

### Token Settings

**maxTokens**: Maximum tokens in response
- Default: 8192
- Range: 1-200000

```json
{
  "maxTokens": 16384
}
```

**temperature**: Randomness in responses
- Default: 1.0
- Range: 0.0-1.0
- Lower = more focused, higher = more creative

```json
{
  "temperature": 0.7
}
```

### Thinking Configuration

**Extended thinking** for complex reasoning:

```json
{
  "thinking": {
    "enabled": true,
    "budget": 10000,
    "mode": "auto"
  }
}
```

**Options:**
- `enabled`: Enable extended thinking
- `budget`: Token budget for thinking (default: 10000)
- `mode`: `auto` | `manual` | `disabled`

### Sandboxing

Filesystem and network isolation:

```json
{
  "sandboxing": {
    "enabled": true,
    "allowedPaths": [
      "/workspace",
      "/home/user/projects"
    ],
    "networkAccess": "restricted",
    "allowedDomains": [
      "api.example.com",
      "*.trusted.com"
    ]
  }
}
```

**Options:**
- `enabled`: Enable sandboxing
- `allowedPaths`: Filesystem access paths
- `networkAccess`: `full` | `restricted` | `none`
- `allowedDomains`: Whitelisted domains

### Memory Management

Control how Factory remembers context:

```json
{
  "memory": {
    "enabled": true,
    "location": "project",
    "ttl": 86400
  }
}
```

**location options:**
- `global`: Share memory across all projects
- `project`: Project-specific memory
- `none`: Disable memory

**ttl**: Time to live in seconds (default: 86400 = 24 hours)

### Output Styles

Customize Factory's behavior:

```json
{
  "outputStyle": "technical-writer"
}
```

**Built-in styles:**
- `default`: Standard coding assistant
- `technical-writer`: Documentation focus
- `code-reviewer`: Review-focused
- `minimal`: Concise responses

### Logging

Configure logging behavior:

```json
{
  "logging": {
    "level": "info",
    "file": ".factory/logs/session.log",
    "console": true
  }
}
```

**Levels:** `debug`, `info`, `warn`, `error`

## Model Configuration

### Using Model Aliases

```bash
# Use Sonnet (default)
Factory

# Use Opus for complex task
Factory --model opus "architect a microservices system"

# Use Haiku for speed
Factory --model haiku "fix typo in README"

# Use opusplan for planning
Factory --model opusplan "plan authentication system"
```

### In Settings File

```json
{
  "model": "opus",
  "thinking": {
    "enabled": true,
    "budget": 20000
  }
}
```

### Model Selection Guide

**Sonnet** (Factory-sonnet-4-5-20250929):
- Balanced performance and cost
- Default choice for most tasks
- Good for general development

**Opus** (Factory-opus-4-20250514):
- Highest capability
- Complex reasoning and planning
- Use for architecture, design, complex debugging

**Haiku** (Factory-haiku-4-20250408):
- Fastest, most cost-effective
- Simple tasks (typos, formatting)
- High-volume operations

**opusplan**:
- Opus + extended thinking
- Deep planning and analysis
- Architecture decisions

## Output Styles

### Creating Custom Output Style

Create `~/.factory/output-styles/my-style.md`:

```markdown
You are a senior software architect focused on scalability.

Guidelines:
- Prioritize performance and scalability
- Consider distributed systems patterns
- Include monitoring and observability
- Think about failure modes
- Document trade-offs
```

### Using Custom Output Style

```bash
Factory --output-style my-style
```

Or in settings:
```json
{
  "outputStyle": "my-style"
}
```

### Example Output Styles

**technical-writer.md:**
```markdown
You are a technical writer creating clear documentation.

Guidelines:
- Use simple, clear language
- Provide examples
- Structure with headings
- Include diagrams when helpful
- Focus on user understanding
```

**code-reviewer.md:**
```markdown
You are a senior code reviewer.

Guidelines:
- Check for bugs and edge cases
- Review security vulnerabilities
- Assess performance implications
- Verify test coverage
- Suggest improvements
```

## Environment Variables

### API Configuration
```bash
export ANTHROPIC_API_KEY=sk-ant-xxxxx
export ANTHROPIC_BASE_URL=https://api.anthropic.com
```

### Proxy Configuration
```bash
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1
```

### Custom CA Certificates
```bash
export NODE_EXTRA_CA_CERTS=/path/to/ca-bundle.crt
```

### Debug Mode
```bash
export Factory_DEBUG=1
export Factory_LOG_LEVEL=debug
```

## Command-Line Flags

### Common Flags

```bash
# Set model
Factory --model opus

# Set max tokens
Factory --max-tokens 16384

# Set temperature
Factory --temperature 0.8

# Enable debug mode
Factory --debug

# Use specific output style
Factory --output-style technical-writer

# Disable memory
Factory --no-memory

# Set project directory
Factory --project /path/to/project
```

### Configuration Commands

```bash
# View current settings
Factory config list

# Set global setting
Factory config set model opus

# Set project setting
Factory config set --project maxTokens 4096

# Get specific setting
Factory config get model

# Reset to defaults
Factory config reset
```

## Advanced Configuration

### Custom Tools

Register custom tools:

```json
{
  "tools": [
    {
      "name": "custom-tool",
      "description": "Custom tool",
      "command": "./scripts/custom-tool.sh",
      "parameters": {
        "arg1": "string"
      }
    }
  ]
}
```

### Rate Limiting

Configure rate limits:

```json
{
  "rateLimits": {
    "requestsPerMinute": 100,
    "tokensPerMinute": 100000,
    "retryStrategy": "exponential"
  }
}
```

### Caching

Prompt caching configuration:

```json
{
  "caching": {
    "enabled": true,
    "ttl": 3600,
    "maxSize": "100MB"
  }
}
```

## Best Practices

### Project Settings
- Keep project-specific in `.factory/settings.json`
- Commit to version control
- Document custom settings
- Share with team

### Global Settings
- Personal preferences only
- Don't override project settings unnecessarily
- Use for API keys and auth

### Security
- Never commit API keys
- Use environment variables for secrets
- Enable sandboxing in production
- Restrict network access

### Performance
- Use appropriate model for task
- Set reasonable token limits
- Enable caching
- Configure rate limits

## Troubleshooting

### Settings Not Applied
```bash
# Check settings hierarchy
Factory config list --all

# Verify settings file syntax
cat .factory/settings.json | jq .

# Reset to defaults
Factory config reset
```

### Environment Variables Not Recognized
```bash
# Verify export
echo $ANTHROPIC_API_KEY

# Check shell profile
cat ~/.bashrc | grep ANTHROPIC

# Reload shell
source ~/.bashrc
```

## See Also

- Model selection: https://docs.Factory.com/about-Factory/models
- Output styles: `references/best-practices.md`
- Security: `references/enterprise-features.md`
- Troubleshooting: `references/troubleshooting.md`
