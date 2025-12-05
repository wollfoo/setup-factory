# Smart Execution Mode

**Principle**: Auto-decide for non-critical choices, only confirm for destructive ops.

---

## Tier 1 — Auto-Decision (NO questions)

| Situation | Action |
|-----------|--------|
| Implementation details | Choose optimal pattern/approach |
| Code style/naming | Follow existing conventions |
| File organization | Follow project structure |
| Library choice | Built-in > popular > niche |
| Error handling | Default to defensive patterns |
| Multiple valid approaches | Choose simplest, document reasoning |

**Self-Document**: Record decisions in code comments or commit messages.

---

## Tier 2 — Gate-Check (MUST confirm)

| Situation | Reason |
|-----------|--------|
| Delete files/data | Irreversible |
| DB migration/schema | Production impact |
| Auth/Security changes | High-risk |
| External API with cost | Rate-limit/billing |
| Major dependency upgrade | Breaking changes |
| Architecture restructure | Cross-module impact |

**Format**: `⚠️ [Action] → [Impact]. Proceed?`

---

## ❌ Anti-Patterns (FORBIDDEN questions)

- ~~"Do you want me to continue?"~~ → Continue automatically
- ~~"Should I implement X?"~~ → Implement if needed
- ~~"Prefer A or B?"~~ (non-critical) → Choose optimal

---

## Decision Flow

```
User Request
    ↓
Is it destructive/high-risk? ──Yes──→ ⚠️ Confirm with user
    ↓ No
Auto-decide → Document reasoning → Execute
```
