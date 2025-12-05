#!/usr/bin/env node
/**
 * Rules Loader Hook for Claude Code
 * 
 * Triggers on UserPromptSubmit and injects rules/workflows content
 * into the context as additionalContext.
 * 
 * Cross-platform: Works on Windows (PowerShell) and Unix (Bash)
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

// Use user home directory ~/.claude/
const CLAUDE_HOME = path.join(os.homedir(), '.claude');
const RULES_DIR = path.join(CLAUDE_HOME, 'rules');
const WORKFLOWS_DIR = path.join(CLAUDE_HOME, 'workflows');

/**
 * Read all markdown files from a directory
 * @param {string} dir - Directory path
 * @returns {Array} Array of {name, content}
 */
function readMarkdownFiles(dir) {
  const files = [];
  try {
    const entries = fs.readdirSync(dir);
    for (const entry of entries) {
      if (entry.endsWith('.md')) {
        const filePath = path.join(dir, entry);
        const content = fs.readFileSync(filePath, 'utf8');
        files.push({ name: entry, content });
      }
    }
  } catch (err) {
    // Directory doesn't exist or not readable - skip silently
  }
  return files;
}

/**
 * Main hook handler
 */
async function main() {
  let input = '';

  // Read stdin
  try {
    input = fs.readFileSync(0, 'utf8');
  } catch (err) {
    process.exit(0);
  }

  if (!input.trim()) {
    process.exit(0);
  }

  // Parse hook input
  let hookData;
  try {
    hookData = JSON.parse(input);
  } catch (err) {
    process.exit(0);
  }

  const prompt = (hookData.prompt || hookData.message || '').toLowerCase();

  // Only inject on first prompt or when explicitly requested
  const triggerKeywords = ['/load-rules', 'load rules', 'áp dụng rules', 'đọc rules'];
  const shouldInject = triggerKeywords.some(kw => prompt.includes(kw));

  if (!shouldInject) {
    process.exit(0);
  }

  // Read rules and workflows
  const rules = readMarkdownFiles(RULES_DIR);
  const workflows = readMarkdownFiles(WORKFLOWS_DIR);

  if (rules.length === 0 && workflows.length === 0) {
    process.exit(0);
  }

  // Build context
  let context = '## AUTO-LOADED RULES & WORKFLOWS\n\n';

  if (rules.length > 0) {
    context += '### Rules\n';
    for (const rule of rules) {
      context += `\n#### ${rule.name}\n${rule.content}\n`;
    }
  }

  if (workflows.length > 0) {
    context += '\n### Workflows\n';
    for (const wf of workflows) {
      context += `\n#### ${wf.name}\n${wf.content}\n`;
    }
  }

  // Output as JSON
  const output = {
    additionalContext: context,
    loadedFiles: {
      rules: rules.map(r => r.name),
      workflows: workflows.map(w => w.name)
    }
  };

  console.log(JSON.stringify(output));
  process.exit(0);
}

main().catch(err => {
  console.error(`[rules-loader] Error: ${err.message}`);
  process.exit(0);
});
