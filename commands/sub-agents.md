---
description: Orchestrate multiple specialized agents to complete complex tasks efficiently
argument-hint: <task-description-or-file-path>
---

# Multi-Agent Task Orchestration

**Task input**: `$ARGUMENTS`

## Step 0: Input Processing

**FIRST**, check if `$ARGUMENTS` contains a file reference:

### Case 1: Pure file path
If `$ARGUMENTS` is ONLY a file path (e.g., `/full/path/file.md`):
- Use **Read** tool to load the file content
- Use file content as the task description

### Case 2: Instruction with file reference
If `$ARGUMENTS` contains instruction text AND mentions a file (e.g., `implement /full/path/file.md`, `read /full/path/file.md and build`):
- Extract file name(s) from the text
- Use **Read** tool to load file content(s)
- Combine file content with the instruction context

### Case 3: Plain text instruction
If `$ARGUMENTS` is plain text without file references:
- Use directly as the task description

**Task to coordinate**: Content processed from `$ARGUMENTS` (file content + instructions)

## Orchestration Strategy

Analyze the task and coordinate specialized agents using the following approach:

### 1. **Task Analysis**
- Break down `$ARGUMENTS` into logical components
- Identify required domains (backend, frontend, database, security, etc.)
- Map dependencies between sub-tasks
- Assess complexity and resource requirements

### 2. **Agent Selection**
Select appropriate specialized agents from available droids (20 total):

#### **Architecture & Design**
- `graphql-architect` - GraphQL schema design and federation
- `docs-architect` - Technical documentation architecture
- `frontend-designer` - UI/UX design and implementation

#### **Planning & Research**
- `planner-researcher` - Technical research and implementation planning

#### **Language Specialists**
- `typescript-expert` - TypeScript type system architecture
- `python-pro` - Advanced Python development
- `golang-pro` - Go language specialist
- `rust-pro` - Rust development
- `ruby-pro` - Ruby development
- `php-developer` - PHP development

#### **Database & Infrastructure**
- `database-specialist` - Database design, optimization, SQL
- `devops-engineer` - CI/CD, containerization, orchestration

#### **Quality Assurance & Security**
- `code-reviewer` - Code quality and security review
- `security-auditor` - Security vulnerability assessment
- `tester` - Test automation and QA
- `debug-specialist` - Debugging and troubleshooting

#### **Code Analysis & Refactoring**
- `code-searcher` - Codebase search and analysis
- `codebase-research-analyst` - Codebase structure analysis
- `code-refactor-master` - Code refactoring and cleanup

#### **Context Management**
- `memory-bank-synchronizer` - Memory and context synchronization

### 3. **Coordination Workflow**
Execute using the **Task tool** to delegate to specialized droids:

```
1. Planning Phase:
   - Use planner-researcher to analyze requirements
   - Use codebase-research-analyst for existing code analysis
   
2. Implementation Phase:
   - Delegate specific tasks to domain experts (e.g., python-pro, typescript-expert)
   - Coordinate parallel execution when possible
   
3. Validation Phase:
   - code-reviewer for quality assurance
   - security-auditor for security review
   - tester for comprehensive testing
   
4. Documentation Phase:
   - docs-architect for technical documentation
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

For `$ARGUMENTS`, use Task tool like:
```
Task(subagent="planner-researcher", context={
  "task": "$ARGUMENTS",
  "focus": "architecture and implementation plan"
})

Task(subagent="python-pro", context={
  "requirements": "from planner output",
  "deliverable": "API implementation and core logic"
})

Task(subagent="database-specialist", context={
  "schema_requirements": "from planner output",
  "optimization_focus": "query performance"
})
```

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
