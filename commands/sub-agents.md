---
description: Orchestrate multiple specialized agents to complete complex tasks efficiently
argument-hint: <task-description-or-file-path>
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Multi-Agent Task Orchestration

**Task input**: `$ARGUMENTS`

## Step 0: Input Processing

**Task input**: Use `$ARGUMENTS` directly as the task description for orchestration.

## Orchestration Strategy

Analyze the task and coordinate specialized agents using the following approach:

### 1. **Task Analysis**
- Break down `$ARGUMENTS` into logical components
- Identify required domains (planning, research, coding, testing, docs, etc.)
- Map dependencies between sub-tasks
- Assess complexity and resource requirements

### 2. **Agent Selection**
Select appropriate specialized agents from available agents (16 total):

#### **Planning & Research**
- `planner` - Technical planning, architecture design, implementation strategy
- `researcher` - Comprehensive research on technologies, packages, best practices
- `brainstormer` - Solution brainstorming, evaluating architectural approaches, technical debates

#### **Codebase Navigation**
- `scout` - Quickly locate relevant files across codebase using slash commands
- `scout-external` - Locate files using external tools (Gemini, OpenCode)

#### **Quality Assurance & Testing**
- `code-reviewer` - Comprehensive code review, security, performance analysis
- `tester` - Test execution, coverage analysis, build verification
- `debugger` - Issue investigation, system analysis, performance optimization

#### **Database**
- `database-admin` - Database administration, query optimization, backup strategies

#### **Documentation**
- `docs-manager` - Technical documentation, PDRs, code standards
- `journal-writer` - Document technical failures, difficulties with emotional honesty

#### **Design & Content**
- `ui-ux-designer` - UI/UX design, wireframes, design systems, Three.js/WebGL
- `copywriter` - High-converting marketing copy, social media content

#### **DevOps & Version Control**
- `git-manager` - Git operations, conventional commits, push workflow
- `mcp-manager` - MCP server integrations, tool discovery

#### **Project Management**
- `project-manager` - Project oversight, progress tracking, report collection

### 3. **Coordination Workflow**
Execute by invoking agents in sequence:

```
1. Planning Phase:
   - /planner to create implementation strategy
   - /researcher for technical research
   - /brainstormer for solution evaluation
   
2. Discovery Phase:
   - /scout-external (preferred) or /scout to locate relevant files
   
3. Implementation Phase:
   - /database-admin for database work
   - /ui-ux-designer for frontend design
   - Coordinate parallel execution when possible
   
4. Validation Phase:
   - /code-reviewer for quality assurance
   - /tester for comprehensive testing
   - /debugger for troubleshooting
   
5. Documentation Phase:
   - /docs-manager for technical documentation
   - /copywriter for marketing content
   
6. Delivery Phase:
   - /git-manager for commits and pushes
   - /project-manager for status updates
```

### 4. **Result Integration**
- Collect outputs from all agents
- Resolve conflicts and inconsistencies
- Synthesize comprehensive solution
- Validate completeness and correctness

### 5. **Verification**
- Run tests and validation checks
- Security and performance review
- Ensure all requirements met
- Document implementation decisions

## Delegation Example

For `$ARGUMENTS`, coordinate by calling specialized agents:

**Step 1 - Planning:**
```bash
/planner $ARGUMENTS
/researcher [research topics]
```

**Step 2 - Discovery:**
```bash
/scout-external [search query]
```

**Step 3 - Implementation:**
```bash
/database-admin [schema requirements]
/ui-ux-designer [design requirements]
```

**Step 4 - Validation:**
```bash
/code-reviewer [completed implementation]
/tester [test requirements]
```

**Note:** Each agent is a separate slash command defined in `/agents/`
You orchestrate by calling them sequentially and passing context between them.

## Output

Provide:
- **Summary**: Overview of orchestration approach
- **Agent Assignments**: Which agents handle which parts
- **Execution Plan**: Step-by-step coordination
- **Dependencies**: What depends on what
- **Timeline**: Estimated completion sequence
- **Results**: Integrated final output from all agents

---

**Begin orchestration for**: `$ARGUMENTS`
