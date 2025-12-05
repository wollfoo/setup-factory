# Getting Started with Factory Code

Installation, authentication, and setup guide for Factory Code.

## What is Factory Code?

Factory Code is Anthropic's agentic coding tool that lives in the terminal and helps turn ideas into code faster. Key features:

- **Agentic Capabilities**: Autonomous planning, execution, and validation
- **Terminal Integration**: Works directly in command line
- **IDE Support**: Extensions for VS Code and JetBrains IDEs
- **Extensibility**: Plugins, skills, slash commands, and MCP servers
- **Enterprise Ready**: SSO, sandboxing, monitoring, and compliance features

## Prerequisites

### System Requirements
- **Operating Systems**: macOS, Linux, or Windows (WSL2)
- **Runtime**: Node.js 18+ or Python 3.10+
- **API Key**: From Anthropic Console (console.anthropic.com)

### Getting API Key
1. Go to console.anthropic.com
2. Sign in or create account
3. Navigate to API Keys section
4. Generate new API key
5. Save key securely (cannot be viewed again)

## Installation

### Install via npm (Recommended)
```bash
npm install -g @anthropic-ai/factory-code
```

### Install via pip
```bash
pip install factory-code
```

### Verify Installation
```bash
Factory --version
```

## Authentication

### Method 1: Interactive Login
```bash
Factory login
# Follow prompts to enter API key
```

### Method 2: Environment Variable
```bash
# Add to ~/.bashrc or ~/.zshrc
export ANTHROPIC_API_KEY=your_api_key_here

# Or set for single session
export ANTHROPIC_API_KEY=your_api_key_here
Factory
```

### Method 3: Configuration File
Create `~/.factory/config.json`:
```json
{
  "apiKey": "your_api_key_here"
}
```

### Verify Authentication
```bash
Factory "hello"
# Should respond without authentication errors
```

## First Run

### Start Interactive Session
```bash
# In any directory
Factory

# In specific project
cd /path/to/project
Factory
```

### Run with Specific Task
```bash
Factory "implement user authentication"
```

### Run with File Context
```bash
Factory "explain this code" --file app.js
```

## Basic Usage

### Interactive Mode
```bash
$ Factory
Factory Code> help me create a React component
# Factory will plan and execute
```

### One-Shot Mode
```bash
Factory "add error handling to main.py"
```

### With Additional Context
```bash
Factory "refactor this function" --file utils.js --context "make it async"
```

## Understanding the Interface

### Session Start
```
Factory Code v1.x.x
Working directory: /path/to/project
Model: Factory-sonnet-4-5-20250929

Factory Code>
```

### Tool Execution
Factory will show:
- Tool being used (Read, Write, Bash, etc.)
- Tool parameters
- Results or outputs
- Thinking/planning process (if enabled)

### Session End
```bash
# Type Ctrl+C or Ctrl+D
# Or type 'exit' or 'quit'
```

## Common First Commands

### Explore Codebase
```bash
Factory "explain the project structure"
```

### Run Tests
```bash
Factory "run the test suite"
```

### Fix Issues
```bash
Factory "fix all TypeScript errors"
```

### Add Feature
```bash
Factory "add input validation to the login form"
```

## Directory Structure

Factory Code creates `.factory/` in your project:

```
project/
├── .factory/
│   ├── settings.json      # Project-specific settings
│   ├── commands/          # Custom slash commands
│   ├── skills/            # Custom skills
│   ├── hooks.json         # Hook configurations
│   └── mcp.json           # MCP server configurations
└── ...
```

## Next Steps

### Learn Slash Commands
```bash
# See available commands
/help

# Try common workflows
/cook implement feature X
/fix:fast bug in Y
/test
```

### Create Custom Skills
See `references/agent-skills.md` for creating project-specific skills.

### Configure MCP Servers
See `references/mcp-integration.md` for connecting external tools.

### Set Up Hooks
See `references/hooks-and-plugins.md` for automation.

### Configure Settings
See `references/configuration.md` for customization options.

## Quick Troubleshooting

### Authentication Issues
```bash
# Re-login
Factory logout
Factory login

# Verify API key is set
echo $ANTHROPIC_API_KEY
```

### Permission Errors
```bash
# Check file permissions
ls -la ~/.Factory

# Fix ownership
sudo chown -R $USER ~/.Factory
```

### Installation Issues
```bash
# Clear npm cache
npm cache clean --force

# Reinstall
npm uninstall -g @anthropic-ai/factory-code
npm install -g @anthropic-ai/factory-code
```

### WSL2 Issues (Windows)
```bash
# Ensure WSL2 is updated
wsl --update

# Check Node.js version in WSL
node --version  # Should be 18+
```

## Getting Help

- **Documentation**: https://docs.Factory.com/factory-code
- **GitHub Issues**: https://github.com/anthropics/factory-code/issues
- **Support**: support.Factory.com
- **Community**: discord.gg/anthropic

For detailed troubleshooting, see `references/troubleshooting.md`.
