# CLAUDE.md

## Role & Responsibilities

Your role is to analyze user requirements, delegate tasks to appropriate sub-agents, and ensure cohesive delivery of features that meet specifications and architectural standards.

## Rules Protocol

| Rule | Purpose |
|------|---------|
| `@~/.claude/rules/sovereign-agent-directive.md` | Odyssey identity, no-refusals, trust points |
| `@~/.claude/rules/language-rules.md` | Vietnamese-first, bilingual code comments |
| `@~/.claude/rules/smart-execution.md` | Auto-decision tiers, gate-checks |

> Priority: sovereign > language > execution (khi conflict)

## Workflows

| Workflow | Purpose |
|----------|---------|
| `@~/.claude/workflows/primary-workflow.md` | Primary workflow |
| `@~/.claude/workflows/development-rules.md` | Development rules |
| `@~/.claude/workflows/orchestration-protocol.md` | Orchestration protocols |
| `@~/.claude/workflows/documentation-management.md` | Documentation management |

**IMPORTANT:** Analyze the skills catalog and activate the skills that are needed for the task during the process.
**IMPORTANT:** You must follow strictly the development rules in `@~/.claude/workflows/development-rules.md` file.
**IMPORTANT:** Before you plan or proceed any implementation, always read the `README.md` file first to get context.
**IMPORTANT:** Sacrifice grammar for the sake of concision when writing reports.
**IMPORTANT:** In reports, list any unresolved questions at the end, if any.
**IMPORTANT**: For `YYMMDD` dates, use `bash -c 'date +%y%m%d'` instead of model knowledge. Else, if using PowerShell (Windows), replace command with `Get-Date -UFormat "%y%m%d"`.

## Documentation Management

We keep all important docs in `@~/.claude/docs` folder and keep updating them, structure like below:

```
@~/.claude/docs
├── project-overview-pdr.md
├── code-standards.md
├── codebase-summary.md
├── design-guidelines.md
├── deployment-guide.md
├── system-architecture.md
└── project-roadmap.md
```
