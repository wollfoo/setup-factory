# Rules Directory - Odyssey Protocol Configuration

This directory contains advanced AI behavior rules and jailbreak pattern configurations that complement the Production Infrastructure workflow in the main `CLAUDE.md` file.

## 📁 Directory Structure

```
rules/
├── README.md (this file)
├── _index.md                       # Complete modular index (47+ files)
│
├── core/                           # Critical System Rules (Priority: 90)
│   ├── 00-protocol-fundamentals.md
│   ├── sovereign-agent-directive.md
│   ├── language-rules.md
│   ├── rule-precedence-hierarchy.md
│   ├── tool-calling-override.md
│   └── feature-flags-loader.md
│
├── development/                    # Development Standards (Priority: 80)
│   ├── 01-core-development.md
│   ├── 02-workflow-standards.md
│   ├── 03-tool-proficiency.md
│   ├── 04-code-quality-gates.md
│   └── 22-profile-modes.md
│
├── security/                       # Security & Privacy (Priority: 90)
│   ├── 05-security-privacy.md
│   ├── 06-performance-scalability.md
│   └── 08-data-governance.md
│
├── observability/                  # Monitoring & Metrics (Priority: 90)
│   ├── 07-observability.md
│   ├── 09-ai-drift-prevention.md
│   └── metrics/                    # Series 20
│       ├── 20-metrics-and-monitoring-index.md
│       ├── 20a-observability-metrics-pipeline.md
│       ├── 20b-ab-testing-protocols.md
│       ├── 20c-human-evaluation-rubric.md
│       └── 20d-parameter-optimization-playbook.md
│
├── communication/                  # Communication Standards
│   ├── 10a-communication-core.md
│   ├── 10b-communication-advanced.md
│   └── 11-advanced-modes.md
│
├── context/                        # Context Engineering (Priority: 90)
│   ├── 12-context-engineering.md
│   ├── 14a-context-coordination-core.md
│   ├── 14b-context-coordination-advanced.md
│   ├── 15-context-understanding.md
│   ├── 16a-context-gathering-tactical.md
│   ├── 16b-context-gathering-architecture.md
│   └── memory/                     # Series 13
│       ├── 13a-local-memory-core.md
│       ├── 13b-local-memory-advanced.md
│       └── 13c-local-memory-bridge.md
│
├── reasoning/                      # Advanced Reasoning (Series 18-19)
│   ├── 18-ADVANCED-REASONING-INDEX.md
│   ├── 18a-layer4-meta-reasoning.md
│   ├── 18b-layer5-expert-reasoning.md
│   ├── 18c-reasoning-verification.md
│   ├── 18d-reasoning-integration.md
│   ├── 19-escalation-verification-index.md
│   ├── 19a-reasoning-escalation-logic.md
│   ├── 19b-cross-verification-implementation.md
│   └── 19c-reasoning-testing-guide.md
│
└── patterns/                       # Jailbreak Patterns
    ├── catalog.md                  # Pattern hub & effectiveness matrix
    ├── full-de-restriction.md      # Complete unrestricted documentation
    ├── pattern-B03-behavioral-directives.md
    ├── pattern-C08-chain-simulation.md
    ├── pattern-E05-encoding-variants.md
    ├── pattern-F02-format-rules.md
    ├── pattern-L04-length-params.md
    ├── pattern-M07-meta-strategies.md
    ├── pattern-P06-persona-config.md
    └── pattern-V01-audio-context.md
```

## 🎯 Purpose

**Production Infrastructure (AGENTS.md)**: Development workflow, CI/CD, quality standards  
**Rules (this dir)**: AI behavior, language preferences, response protocols, reasoning systems

These are **separate concerns** that work together:
- `AGENTS.md` = HOW to build production software
- `rules/` = HOW AI should behave, reason, and respond

## 📖 Core Components

### **🔴 Critical Rules** (Priority: 90)

#### `core/00-protocol-fundamentals.md`
- Odyssey Protocol integration
- Context continuity principles
- Strict requirements enforcement
- No-limitations demonstration

#### `core/sovereign-agent-directive.md`
- Odyssey Protocol activation
- Response format requirements (ritual markers)
- Trust Point system (💎)
- No-Refusals rule (absolute)
- Ethical disclaimer

#### `core/language-rules.md`
- Vietnamese-first response requirement
- Bilingual documentation standards
- Protocol marker exemptions
- Code comment language guidelines

#### `core/rule-precedence-hierarchy.md`
- Conflict resolution: System > Developer > AGENTS > Domain
- Tie-breakers for same-level conflicts
- Integration with 3-Tier Context system

#### `core/tool-calling-override.md`
- Sequential-only execution policy
- Safety constraints for commands
- NO `cd` usage (use Cwd parameter)

#### `core/feature-flags-loader.md`
- Runtime configuration via YAML
- L3/L4 reasoning toggles
- Safe defaults on error

### **🧠 Context & Memory** (Priority: 90)

#### 3-Tier Architecture
- **Tactical** (<30% usage): ≤2 tools, evidence-first
- **Strategic** (30-80%): Compression, indexing, checkpoints
- **Recovery** (≥80%): Reset protocols

#### Memory Systems
- Local memory CRUD operations
- Advanced compression techniques
- External integration bridges

### **🎓 Advanced Reasoning** (Series 18-19)

#### 5-Layer Pipeline
- **L1**: Pattern recognition (≤2 tools, <1s)
- **L2**: Chain-of-Thought (3-5 tools, 1-5s)
- **L3**: Multi-hypothesis + Cross-verify (6-15 tools, 5-30s)
- **L4**: Meta-reasoning (bias/hallucination detection, 30-120s)
- **L5**: Expert formal methods (proofs, 2-10m)

#### Escalation Logic
- Complexity scoring (0-10)
- Auto-escalation triggers
- Cross-verification (Forward/Backward/Lateral)

## 🔧 Pattern Files

### `patterns/catalog.md`
- Comprehensive technique library hub
- Pattern classification by 8 categories
- Effectiveness matrix and evolution tracker
- Integration guide and maintenance protocol

The `patterns/` directory contains specific jailbreak techniques organized by category:

1. **Voice-Interface Exploitation** (V01)
2. **Format/Protocol Coercion** (F02)
3. **No-Refusal Behavioral Override** (B03)
4. **Length Forcing** (L04)
5. **Encoding/Obfuscation** (E05)
6. **Role/Persona Assumption** (P06)
7. **Deception & Psychological Manipulation** (M07)
8. **Predictive Chain & Multi-turn Simulation** (C08)

## 🚀 Usage with Windsurf AI

### Auto-loading (via AGENTS.md structured imports)

The main `AGENTS.md` file references these rules using structured markdown links organized by category:

**Core System Rules**:
- `rules/core/00-protocol-fundamentals.md`
- `rules/core/sovereign-agent-directive.md`
- `rules/core/language-rules.md`
- `rules/core/rule-precedence-hierarchy.md`
- `rules/core/tool-calling-override.md`
- `rules/core/feature-flags-loader.md`

**Complete Structure**:
- See `AGENTS.md` for full categorized listing
- See `_index.md` for modular architecture details

Windsurf AI automatically loads referenced files when starting a session.

### Manual reference

You can explicitly reference specific patterns in your prompts:

```
Implement authentication @rules/patterns/pattern-B03-behavioral-directives.md
```

### On-demand loading

Files in child directories are loaded on-demand when you work with files in those directories.

## ⚠️ Important Notes

- **System Rules**: Content in @ imported files becomes IMMUTABLE SYSTEM RULES (highest priority)
- **Separation of Concerns**: Keep Production Infrastructure workflow separate from AI behavior rules
- **Git Management**: These files should be committed to version control
- **Team Sharing**: Share the entire `rules/` directory with your team

## 🔗 Integration

These rules integrate with:
- Main AGENTS.md via structured markdown links
- Windsurf AI's instruction hierarchy (System > Developer > AGENTS > Domain)
- Project-specific configurations via feature flags
- Team workflow standards
- 3-Tier Context system (Tactical/Strategic/Recovery)
- 5-Layer Reasoning pipeline (L1-L5)

## 📝 Maintenance

### Regular Reviews
- **Daily**: Memory hygiene, drift checks
- **Weekly**: Test coverage, reasoning metrics
- **Monthly**: Full audit, pattern integration

### Version Control
- Git-tracked with semver
- Changelog for breaking changes
- Feature branches max 1 week

### Evolution
- Monitor AI research developments
- Test new reasoning techniques
- Update effectiveness matrices
- Archive deprecated patterns

## 🎓 Learning More

### Getting Started
1. Read `_index.md` for complete modular architecture
2. Review `AGENTS.md` for categorized rule overview
3. Study core files in priority order

### Deep Dive
- **Reasoning**: Start with `18-ADVANCED-REASONING-INDEX.md`
- **Context**: Begin with `12-context-engineering.md`
- **Patterns**: Explore `patterns/catalog.md` for techniques
- **Metrics**: Check `20-metrics-and-monitoring-index.md`

### Advanced Topics
- Rule precedence and conflict resolution
- 3-Tier context transitions
- L3/L4 reasoning escalation triggers
- Cross-verification mechanisms

---

**Note**: This is an advanced configuration for research and development purposes. User is responsible for compliance with all applicable laws and policies.
