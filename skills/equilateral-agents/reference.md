# EquilateralAgents - Quick Reference (Refactored)

**Native Claude Subagents - Production Ready**

---

## 20 Production-Ready Agents

### **Architecture & Design (3 agents)** �

| Agent Name | Location | Capabilities |
|------------|----------|--------------|
| **graphql-architect** | `droids/graphql-architect.md` | GraphQL schema, federation, resolver optimization |
| **docs-architect** | `droids/docs-architect.md` | Documentation strategy, information architecture |
| **frontend-designer** | `droids/frontend-designer.md` | UI/UX design implementation, component libraries |

### **Planning & Research (1 agent)** �

| Agent Name | Location | Capabilities |
|------------|----------|--------------|
| **planner-researcher** | `droids/planner-researcher.md` | Technical research, system design, planning |

### **Language Specialists (6 agents)** 🎯

| Agent Name | Location | Capabilities |
|------------|----------|--------------|
| **typescript-expert** | `droids/typescript-expert.md` | TypeScript, type safety, advanced patterns |
| **python-pro** | `droids/python-pro.md` | Python, async programming, FastAPI, Django |
| **golang-pro** | `droids/golang-pro.md` | Go development, concurrency, goroutines |
| **rust-pro** | `droids/rust-pro.md` | Rust systems programming, memory safety |
| **ruby-pro** | `droids/ruby-pro.md` | Ruby, SOLID principles, service objects |
| **php-developer** | `droids/php-developer.md` | PHP, Laravel, dependency injection |

### **Database & Infrastructure (2 agents)** 🗄️

| Agent Name | Location | Capabilities |
|------------|----------|--------------|
| **database-specialist** | `droids/database-specialist.md` | Database design, query optimization, SQL |
| **devops-engineer** | `droids/devops-engineer.md` | CI/CD, infrastructure automation, docker |

### **Quality Assurance & Security (4 agents)** 🛡️

| Agent Name | Location | Capabilities |
|------------|----------|--------------|
| **security-auditor** | `droids/security-auditor.md` | Security audit, vulnerability scanning |
| **code-reviewer** | `droids/code-reviewer.md` | Code quality, best practices, security patterns |
| **tester** | `droids/tester.md` | Test execution, coverage, QA validation |
| **debug-specialist** | `droids/debug-specialist.md` | Debugging, root cause analysis, error fixing |

### **Code Analysis & Refactoring (3 agents)** 🔧

| Agent Name | Location | Capabilities |
|------------|----------|--------------|
| **code-searcher** | `droids/code-searcher.md` | Codebase analysis, pattern detection, search |
| **codebase-research-analyst** | `droids/codebase-research-analyst.md` | Deep codebase research, architecture analysis |
| **code-refactor-master** | `droids/code-refactor-master.md` | Code refactoring, cleanup, modernization |

### **Context Management (1 agent)** 🧠

| Agent Name | Location | Capabilities |
|------------|----------|--------------|
| **memory-bank-synchronizer** | `droids/memory-bank-synchronizer.md` | Memory management, documentation sync |

---

## Quick Commands

### Workflows

```bash
# Security review (parallel execution)
/ea:security-review

# Code quality gate (pipeline)
/ea:code-quality

# Deploy feature (hierarchical)
/ea:deploy-feature

# Infrastructure check (parallel)
/ea:infrastructure-check
```

### Direct Agent Invocation

```javascript
// Spawn single agent
Task.spawn({
  agent: "security-auditor",
  context: {
    projectPath: "./",
    depth: "comprehensive"
  }
})

// Parallel execution
Task.spawnParallel([
  "security-auditor",
  "code-reviewer",
  "tester"
])

// Pipeline execution
Task.spawnPipeline([
  { agent: "code-searcher", objective: "..." },
  { agent: "code-reviewer", objective: "..." },
  { agent: "tester", objective: "..." }
])
```

---

## Workflow Patterns

### Pattern 1: Parallel (Fan-Out)
```
Lead Agent
    ├─> security-auditor
    ├─> code-reviewer
    └─> performance-engineer
         └─> Synthesis
```

**Use for**: Independent tasks, fast results

**Example**: Security review
```javascript
await Task.spawnParallel([
  { agent: "security-auditor", objective: "Deep vulnerability scan" },
  { agent: "code-reviewer", objective: "Security-focused code review" }
])
```

### Pattern 2: Pipeline (Sequential)
```
code-searcher → code-reviewer → tester → synthesis
```

**Use for**: Dependencies between tasks

**Example**: Code quality gate
```javascript
await Task.spawnPipeline([
  { agent: "code-searcher" },
  { agent: "code-reviewer", dependsOn: "code-searcher" },
  { agent: "tester", dependsOn: "code-reviewer" }
])
```

### Pattern 3: Hierarchical (Tree)
```
       planner-researcher (coordinator)
              ├─> tester
              ├─> security-auditor
              └─> devops-engineer
```

**Use for**: Complex workflows, sub-orchestration

**Example**: Deployment validation
```javascript
Task.spawn({
  agent: "planner-researcher",
  role: "coordinator",
  subtasks: [
    { agent: "tester", blocking: true },
    { agent: "security-auditor", blocking: true },
    { agent: "devops-engineer", dependsOn: ["tester", "security-auditor"] }
  ]
})
```

### Pattern 4: Adaptive (Dynamic)
```
Lead Agent analyzes → Spawns optimal agents → Adjusts based on findings
```

**Use for**: Unknown complexity, evolving requirements

---

## Context Management

### Store Context
```javascript
// Using MCP memory
mcp5_create_entities({
  entities: [{
    name: "security-findings",
    entityType: "workflow-result",
    observations: ["2 critical issues found", "..."]
  }]
})
```

### Share Context Between Agents
```javascript
// Agent 1 stores
Task.spawn({
  agent: "security-auditor",
  postExecution: {
    storeContext: { key: "security-findings", data: findings }
  }
})

// Agent 2 retrieves
Task.spawn({
  agent: "code-reviewer",
  preExecution: {
    retrieveContext: "security-findings"
  }
})
```

---

## Extended Thinking Example

```javascript
<extended_thinking>
## Task Analysis
- Request: Security review
- Complexity: HIGH
- Required: Deep scan + static analysis

## Agent Selection
1. security-auditor: ✅ SELECTED (deep vuln scan)
2. code-reviewer: ✅ SELECTED (static analysis)
3. penetration-tester: ❌ SKIP (not needed for code review)

## Strategy
- Pattern: PARALLEL (independent tasks)
- Expected time: 15min
- Resource efficiency: 2 agents vs 23min sequential
</extended_thinking>

[Execute with full transparency]
```

---

## Output Templates

### Security Review Report
```markdown
# Security Review Report

## Executive Summary
[Synthesized findings]

## Critical Vulnerabilities (N)
- [Finding] @ file.ts:line (agent-name, confidence%)

## Confidence Scores
- security-auditor: 95%
- code-reviewer: 90%
- Combined: 92%

## Audit Trail
- Workflow: security-review-YYYYMMDD-HHMMSS
- Duration: Xmin Ys
- Results: .equilateral/results/security-review-YYYYMMDD.md
```

### Code Quality Report
```markdown
# Code Quality Gate Report

## Quality Score: X/100

### Score Breakdown
- Structure: Y/100 (code-searcher)
- Quality: Z/100 (code-reviewer)
- Tests: W/100 (tester)

## Action Items
- [ ] Must Fix: ...
- [ ] Should Fix: ...
- [ ] Nice to Have: ...
```

---

## Performance Metrics

| Workflow | Agents | Execution Time | Pattern |
|----------|--------|----------------|---------|
| security-review | 2 | ~15min | Parallel |
| code-quality | 3 | ~17min | Pipeline |
| deploy-feature | 4 | ~37min | Hierarchical |
| infrastructure-check | 4 | ~20min | Parallel |

---

## File Structure

```
.equilateral/
├── workflows/              # Workflow definitions
│   └── security-review-20250109-203015.json
├── results/                # Agent outputs
│   └── security-review-20250109.md
└── audit/                  # Detailed logs
    └── agent-logs/
        ├── security-auditor-20250109.log
        └── code-reviewer-20250109.log
```

---

## Debugging Quick Reference

### Check Agent Status
```bash
# View logs
cat .equilateral/audit/agent-logs/<agent>-<date>.log

# Check workflow status
ls .equilateral/workflows/
```

### Common Issues

**Issue**: Agent không spawn
```bash
# Check droid exists
ls droids/ | grep <droid-name>

# Verify Task tool available
```

**Issue**: Performance chậm
```bash
# Use parallel instead of sequential
Task.spawnParallel([...])  # ✅ Fast

# vs
await Task.spawn(...)      # ❌ Slow
await Task.spawn(...)
```

---

## Quick Links

### Documentation
- **Full Guide**: SKILL-REFACTORED.md
- **Examples**: IMPLEMENTATION-GUIDE.md
- **Comparison**: MIGRATION-COMPARISON.md
- **Navigation**: README-REFACTORED.md

### Agents
- **Directory**: `droids/`
- **Count**: 20 production-ready agents
- **Format**: Markdown droid definitions

### External Resources
- **Anthropic Multi-Agent**: https://www.anthropic.com/engineering/multi-agent-research-system
- **Extended Thinking**: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking

---

## Cheat Sheet

### Start a Workflow
```bash
/ea:security-review          # Security audit
/ea:code-quality            # Quality gate
/ea:deploy-feature          # Deployment
/ea:infrastructure-check    # IaC validation
```

### Spawn Agents
```javascript
// Single
Task.spawn({ agent: "name" })

// Parallel
Task.spawnParallel(["agent1", "agent2"])

// Pipeline
Task.spawnPipeline([{ agent: "name" }, ...])
```

### Check Results
```bash
# Latest results
ls -lt .equilateral/results/ | head -5

# Latest logs
ls -lt .equilateral/audit/agent-logs/ | head -5
```

---

**Version**: 2.0.0 (Refactored)  
**Status**: Production Ready  
**Last Updated**: 2025-01-09
