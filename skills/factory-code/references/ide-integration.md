# IDE Integration

Use Factory Code with Visual Studio Code and JetBrains IDEs.

## Visual Studio Code

### Installation

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Factory Code"
4. Click Install
5. Authenticate with API key

### Features

**Inline Chat**
- Press Ctrl+I (Cmd+I on Mac)
- Ask questions about code
- Get suggestions in context
- Apply changes directly

**Code Actions**
- Right-click on code
- Select "Ask Factory"
- Get refactoring suggestions
- Fix bugs and issues

**Diff View**
- See proposed changes
- Accept/reject modifications
- Review before applying
- Staged diff comparison

**Terminal Integration**
- Built-in Factory terminal
- Run commands via Factory
- Execute tools directly
- View real-time output

### Configuration

**.vscode/settings.json:**
```json
{
  "Factory.apiKey": "${ANTHROPIC_API_KEY}",
  "Factory.model": "Factory-sonnet-4-5-20250929",
  "Factory.maxTokens": 8192,
  "Factory.autoSave": true,
  "Factory.inlineChat.enabled": true,
  "Factory.terminalIntegration": true
}
```

### Keyboard Shortcuts

**Default shortcuts:**
- `Ctrl+I`: Inline chat
- `Ctrl+Shift+C`: Open Factory panel
- `Ctrl+Shift+Enter`: Submit to Factory
- `Escape`: Close Factory chat

**Custom shortcuts (.vscode/keybindings.json):**
```json
[
  {
    "key": "ctrl+alt+c",
    "command": "Factory.openChat"
  },
  {
    "key": "ctrl+alt+r",
    "command": "Factory.refactor"
  }
]
```

### Workspace Integration

**Project-specific Factory settings:**

.vscode/Factory.json:
```json
{
  "skills": [".factory/skills/project-skill"],
  "commands": [".factory/commands"],
  "mcpServers": ".factory/mcp.json",
  "outputStyle": "technical-writer"
}
```

### Common Workflows

**Explain Code:**
1. Select code
2. Right-click → "Ask Factory"
3. Type: "Explain this code"

**Refactor:**
1. Select function
2. Press Ctrl+I
3. Type: "Refactor for better performance"

**Fix Bug:**
1. Click on error
2. Press Ctrl+I
3. Type: "Fix this error"

**Generate Tests:**
1. Select function
2. Right-click → "Ask Factory"
3. Type: "Write tests for this"

## JetBrains IDEs

Supported IDEs:
- IntelliJ IDEA
- PyCharm
- WebStorm
- PhpStorm
- GoLand
- RubyMine
- CLion
- Rider

### Installation

1. Open Settings (Ctrl+Alt+S)
2. Go to Plugins
3. Search "Factory Code"
4. Click Install
5. Restart IDE
6. Authenticate with API key

### Features

**AI Assistant Panel**
- Dedicated Factory panel
- Context-aware suggestions
- Multi-file awareness
- Project understanding

**Inline Suggestions**
- As-you-type completions
- Contextual code generation
- Smart refactoring hints
- Error fix suggestions

**Code Reviews**
- Automated code reviews
- Security vulnerability detection
- Best practice recommendations
- Performance optimization tips

**Refactoring Support**
- Smart rename
- Extract method
- Inline variable
- Move class

### Configuration

**Settings → Tools → Factory Code:**
```
API Key: [Your API Key]
Model: Factory-sonnet-4-5-20250929
Max Tokens: 8192
Auto-complete: Enabled
Code Review: Enabled
```

**Project Settings (.idea/Factory.xml):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="FactorySettings">
    <option name="model" value="Factory-sonnet-4-5-20250929" />
    <option name="skillsPath" value=".factory/skills" />
    <option name="autoReview" value="true" />
  </component>
</project>
```

### Keyboard Shortcuts

**Default shortcuts:**
- `Ctrl+Shift+A`: Ask Factory
- `Alt+Enter`: Quick fixes with Factory
- `Ctrl+Alt+L`: Format with Factory suggestions

**Custom shortcuts (Settings → Keymap → Factory Code):**
```
Ask Factory: Ctrl+Shift+C
Refactor with Factory: Ctrl+Alt+R
Generate Tests: Ctrl+Alt+T
Code Review: Ctrl+Alt+V
```

### Integration with IDE Features

**Version Control:**
- Review commit diffs with Factory
- Generate commit messages
- Suggest PR improvements
- Analyze merge conflicts

**Debugger:**
- Explain stack traces
- Suggest fixes for errors
- Debug complex issues
- Analyze variable states

**Database Tools:**
- Generate SQL queries
- Optimize database schema
- Write migration scripts
- Explain query plans

### Common Workflows

**Generate Boilerplate:**
1. Right-click in editor
2. Select "Generate" → "Factory Code"
3. Choose template type

**Review Changes:**
1. Open Version Control panel
2. Right-click on changeset
3. Select "Review with Factory"

**Debug Error:**
1. Hit breakpoint
2. Right-click in debugger
3. Select "Ask Factory about this"

## CLI Integration

Use Factory Code from IDE terminal:

```bash
# In VS Code terminal
Factory "explain this project structure"

# In JetBrains terminal
Factory "add error handling to current file"
```

## Best Practices

### VS Code

**Workspace Organization:**
- Use workspace settings for team consistency
- Share .vscode/Factory.json in version control
- Document custom shortcuts
- Configure output styles per project

**Performance:**
- Limit inline suggestions in large files
- Disable auto-save for better control
- Use specific prompts
- Close unused editor tabs

### JetBrains

**Project Configuration:**
- Enable Factory for specific file types only
- Configure inspection severity
- Set up custom code review templates
- Use project-specific skills

**Performance:**
- Adjust auto-complete delay
- Limit scope of code analysis
- Disable for binary files
- Configure memory settings

## Troubleshooting

### VS Code

**Extension Not Loading:**
```bash
# Check extension status
code --list-extensions | grep Factory

# Reinstall
code --uninstall-extension anthropic.factory-code
code --install-extension anthropic.factory-code
```

**Authentication Issues:**
- Verify API key in settings
- Check environment variable
- Re-authenticate in extension
- Review proxy settings

### JetBrains

**Plugin Not Responding:**
```
File → Invalidate Caches / Restart
Settings → Plugins → Factory Code → Reinstall
```

**Performance Issues:**
- Increase IDE memory (Help → Edit Custom VM Options)
- Disable unused features
- Clear caches
- Update plugin version

## See Also

- VS Code extension: https://marketplace.visualstudio.com/items?itemName=anthropic.factory-code
- JetBrains plugin: https://plugins.jetbrains.com/plugin/factory-code
- Configuration: `references/configuration.md`
- Troubleshooting: `references/troubleshooting.md`
