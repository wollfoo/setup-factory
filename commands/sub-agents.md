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
Select appropriate specialized agents from available droids (52 total):

#### **Architecture & System Design**
- `architect-review` - Software architecture review and patterns
- `cloud-architect` - Cloud infrastructure and services
- `graphql-architect` - GraphQL schema design and federation

#### **Planning & Strategy**
- `planner-researcher` - Technical research and implementation planning
- `planning-strategist` - Strategic planning and roadmaps
- `plan-reviewer` - Plan validation and review
- `project-task-planner` - Task breakdown and project management
- `prd-writer` - Product requirements documentation
- `refactor-planner` - Refactoring strategy and planning

#### **Backend Development**
- `backend-architect` - Backend system architecture and API design
- `blockchain-developer` - Blockchain and smart contracts
- `hyperledger-fabric-developer` - Hyperledger Fabric development
- `payment-integration` - Payment system integration

#### **Frontend Development**
- `frontend-developer` - Web frontend (React, Vue, Angular)
- `frontend-designer` - UI/UX design and implementation
- `ui-ux-designer` - User interface and experience design
- `mobile-developer` - Mobile app development (React Native, Flutter)
- `game-developer` - Game development

#### **Language Specialists**
- `typescript-expert` - TypeScript type system architecture
- `python-pro` - Advanced Python development
- `golang-pro` - Go language specialist
- `rust-pro` - Rust development
- `ruby-pro` - Ruby development
- `php-developer` - PHP development

#### **Database & Data Engineering**
- `database-specialist` - Database design, optimization, SQL
- `data-engineer` - Data pipelines and ETL
- `data-scientist` - Data analysis and ML models

#### **Quality Assurance & Testing**
- `code-reviewer` - Code quality and security review
- `security-auditor` - Security vulnerability assessment
- `tester` - Test automation and QA
- `performance-engineer` - Performance optimization and profiling
- `debug-specialist` - Debugging and troubleshooting

#### **Code Analysis & Refactoring**
- `code-searcher` - Codebase search and analysis
- `codebase-research-analyst` - Codebase structure analysis
- `code-refactor-master` - Code refactoring and cleanup
- `legacy-modernizer` - Legacy code modernization

#### **DevOps & Infrastructure**
- `devops-engineer` - CI/CD, containerization, orchestration

#### **Documentation & Content**
- `docs-architect` - Technical documentation architecture
- `technical-documentation-specialist` - API and technical docs
- `content-writer` - Content creation and copywriting

#### **AI & Context Management**
- `context-manager` - AI context engineering and orchestration
- `memory-bank-synchronizer` - Memory and context synchronization

#### **Research & Knowledge**
- `web-research-specialist` - Web research and information gathering
- `tech-knowledge-assistant` - Technical knowledge and guidance

#### **Crypto & Finance**
- `crypto-analyst` - Cryptocurrency market analysis
- `crypto-trader` - Trading strategies and signals
- `crypto-risk-manager` - Risk management for crypto
- `quant-analyst` - Quantitative analysis
- `arbitrage-bot` - Arbitrage opportunities detection
- `defi-strategist` - DeFi strategy and protocols

#### **Machine Learning**
- `ml-engineer` - Machine learning engineering and models

#### **Education & Coaching**
- `vibe-coding-coach` - Coding education and mentorship

### 3. **Coordination Workflow**
Execute using the **Task tool** to delegate to specialized droids:

```
1. Planning Phase:
   - Use planner-researcher to analyze requirements
   - Define architecture with architect-review
   
2. Implementation Phase:
   - Delegate specific tasks to domain experts
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

Task(subagent="backend-architect", context={
  "requirements": "from planner output",
  "deliverable": "API design and service architecture"
})

Task(subagent="database-specialist", context={
  "schema_requirements": "from architect output",
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
