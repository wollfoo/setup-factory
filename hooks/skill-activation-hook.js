#!/usr/bin/env node
/**
 * Skill Activation Hook for Claude Code
 * 
 * Triggers on UserPromptSubmit event and suggests appropriate skills
 * based on keyword matching and file patterns.
 * 
 * Cross-platform: Works on Windows (PowerShell) and Unix (Bash)
 */

const fs = require('fs');
const path = require('path');

// Load skill rules
const RULES_PATH = path.join(__dirname, 'skill-rules.json');
const SKILLS_DIR = path.join(__dirname, '..', 'skills');

/**
 * Load and parse skill rules
 */
function loadRules() {
  try {
    const data = fs.readFileSync(RULES_PATH, 'utf8');
    return JSON.parse(data);
  } catch (err) {
    console.error(`[skill-activation] Failed to load rules: ${err.message}`);
    return { rules: [] };
  }
}

/**
 * Match prompt against skill rules
 * @param {string} prompt - User prompt
 * @param {Array} rules - Skill rules
 * @returns {Array} Matched skills sorted by priority
 */
function matchRules(prompt, rules) {
  const promptLower = prompt.toLowerCase();
  const matches = [];

  for (const rule of rules) {
    let score = 0;
    const matchedKeywords = [];

    // Check keyword matches
    for (const keyword of rule.keywords || []) {
      if (promptLower.includes(keyword.toLowerCase())) {
        score += rule.priority || 5;
        matchedKeywords.push(keyword);
      }
    }

    if (score > 0) {
      matches.push({
        skill: rule.skill,
        score,
        priority: rule.priority || 5,
        matchedKeywords,
        filePatterns: rule.filePatterns || []
      });
    }
  }

  // Sort by score (desc), then priority (desc)
  return matches.sort((a, b) => {
    if (b.score !== a.score) return b.score - a.score;
    return b.priority - a.priority;
  });
}

/**
 * Check if skill exists
 * @param {string} skillName - Skill folder name
 * @returns {boolean}
 */
function skillExists(skillName) {
  const skillPath = path.join(SKILLS_DIR, skillName, 'SKILL.md');
  const skillPathAlt = path.join(SKILLS_DIR, skillName, 'skill.md');
  return fs.existsSync(skillPath) || fs.existsSync(skillPathAlt);
}

/**
 * Generate activation suggestion
 * @param {Array} matches - Matched skills
 * @returns {string} Suggestion text
 */
function generateSuggestion(matches) {
  if (matches.length === 0) return '';

  const validMatches = matches.filter(m => skillExists(m.skill));
  if (validMatches.length === 0) return '';

  const top = validMatches[0];
  const others = validMatches.slice(1, 3);

  let suggestion = `[SKILL ACTIVATION] Based on your prompt, consider using the "${top.skill}" skill`;
  suggestion += ` (matched: ${top.matchedKeywords.slice(0, 3).join(', ')}).`;

  if (others.length > 0) {
    suggestion += ` Also relevant: ${others.map(m => m.skill).join(', ')}.`;
  }

  suggestion += ` Load the skill with: @skills/${top.skill}/SKILL.md`;

  return suggestion;
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
    // No input, exit silently
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
    // Invalid JSON, exit silently
    process.exit(0);
  }

  const prompt = hookData.prompt || hookData.message || '';
  if (!prompt) {
    process.exit(0);
  }

  // Load rules and match
  const { rules } = loadRules();
  const matches = matchRules(prompt, rules);

  // Generate and output suggestion
  const suggestion = generateSuggestion(matches);
  if (suggestion) {
    // Output as JSON for Claude to process
    const output = {
      additionalContext: suggestion,
      matchedSkills: matches.slice(0, 3).map(m => ({
        skill: m.skill,
        score: m.score,
        keywords: m.matchedKeywords
      }))
    };
    console.log(JSON.stringify(output));
  }

  // Always exit 0 to be non-blocking
  process.exit(0);
}

main().catch(err => {
  console.error(`[skill-activation] Error: ${err.message}`);
  process.exit(0); // Non-blocking even on error
});
