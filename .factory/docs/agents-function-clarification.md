# Làm Rõ Chức Năng 5 Code Agents

**Date**: 2025-01-08  
**Purpose**: Giải thích rõ ràng chức năng, use cases và khi nào dùng từng agent

---

## 🎯 Quick Decision Guide

**Bạn cần gì?**

| Tình huống | Agent nào? | Tại sao? |
|------------|-----------|----------|
| "Tìm function login ở đâu?" | ✅ **code-searcher** | Tìm kiếm nhanh, locate code |
| "Hiểu kiến trúc auth system" | ✅ **codebase-research-analyst** | Phân tích sâu, dependencies |
| "Tổ chức lại thư mục src/" | ✅ **code-refactor-master** | Di chuyển files, restructure |
| "Function này 200 dòng, cải thiện" | ✅ **code-refactorer** | Cải thiện local code |
| "Review code trước merge" | ✅ **code-reviewer** | Quality gate, security check |

---

## 📋 Agent 1: code-searcher

### 🎯 **Chức Năng Chính**
**"Detective của codebase"** - Tìm kiếm và locate code với tốc độ cao

### ✅ **Khi Nào Dùng**

**Scenario 1 - Tìm Function**:
```
User: "Where is the login function?"
→ code-searcher: Grep→found:auth.service.ts:45
```

**Scenario 2 - Find All Usage**:
```
User: "Find all places using getUserData"
→ code-searcher: Grep→12 files→list locations
```

**Scenario 3 - Pattern Detection**:
```
User: "Find all API calls"
→ code-searcher: Pattern→fetch|axios→found:23 locations
```

### 🔧 **Capabilities**

✅ **Quick lookups** - "Where is X?"  
✅ **Pattern detection** - "Find all Y"  
✅ **Usage finding** - "Who calls this function?"  
✅ **CoD mode** - Ultra-concise (≤5 words per step)  
✅ **Forensic search** - Bug location, error traces  

### ❌ **KHÔNG Làm**

❌ Không phân tích architecture sâu  
❌ Không hiểu dependencies phức tạp  
❌ Không refactor code  
❌ Không review security  

### 📝 **Example Queries**

```
✅ "Tìm login function"
✅ "Where is API endpoint /users"
✅ "Find all useState hooks"
✅ "Locate database queries"
✅ "Ở đâu có hardcoded passwords?"
```

### 🎓 **Key Feature: Chain of Draft (CoD)**

**Standard mode** (verbose):
```
"I'll search for authentication by examining auth files,
then checking login patterns, analyzing JWT usage..."
```

**CoD mode** (ultra-concise):
```
Auth→*auth*→login|jwt→auth.service:45→JWT+bcrypt
```

**Khi nào dùng CoD**: Fast queries, known patterns, minimal explanation needed

---

## 📋 Agent 2: codebase-research-analyst

### 🎯 **Chức Năng Chính**
**"Scientist của codebase"** - Phân tích sâu architecture, dependencies, impact

### ✅ **Khi Nào Dùng**

**Scenario 1 - Understand Architecture**:
```
User: "How does the auth system work?"
→ analyst: Analyze structure→map dependencies→flow diagram
```

**Scenario 2 - Dependency Mapping**:
```
User: "What depends on UserService?"
→ analyst: Trace imports→dependency tree→impact analysis
```

**Scenario 3 - Before Major Changes**:
```
User: "Planning to refactor payment module"
→ analyst: Map all dependencies→impact zones→risk assessment
```

### 🔧 **Capabilities**

✅ **Architecture analysis** - System structure, patterns  
✅ **Dependency mapping** - Who imports what  
✅ **Impact assessment** - "If I change X, what breaks?"  
✅ **Module relationships** - How components interact  
✅ **Systematic methodology** - Root→config→dependencies→flow  

### ❌ **KHÔNG Làm**

❌ Không quick search (dùng code-searcher)  
❌ Không refactor code  
❌ Không review security  
❌ Không fix bugs  

### 📝 **Example Queries**

```
✅ "Phân tích kiến trúc auth system"
✅ "Dependency map của UserService"
✅ "Impact nếu change database schema"
✅ "How do frontend và backend communicate?"
✅ "Architectural patterns in use"
```

### 🎯 **Output Format**

```markdown
## Architecture Analysis

### High-Level Structure
- Pattern: MVC
- Layers: Frontend → API → Database

### Dependencies
- UserService → AuthService → Database
- 12 files import UserService
- Impact zone: High (critical path)

### Findings
- ⚠️ Tight coupling between auth and user
- ✅ Clear separation: API ↔ Database

### Recommendations
- Consider dependency injection
- Further analysis: payment module
```

---

## 📋 Agent 3: code-refactor-master

### 🎯 **Chức Năng Chính**
**"Architect của codebase"** - Tổ chức lại structure, di chuyển files, system-level refactoring

### ✅ **Khi Nào Dùng**

**Scenario 1 - Reorganize Project**:
```
User: "Reorganize src/ to feature-based structure"
→ refactor-master: 
  1. Map all dependencies
  2. Design new structure
  3. Move files + update imports
  4. Verify no broken imports
```

**Scenario 2 - Split Large Module**:
```
User: "Split monolithic auth.ts into separate files"
→ refactor-master:
  1. Analyze auth.ts (500 LOC)
  2. Plan extraction: auth/login.ts, auth/register.ts
  3. Update all imports
  4. Verify functionality
```

**Scenario 3 - File Structure Cleanup**:
```
User: "Move all utils to shared/utils/"
→ refactor-master:
  1. Find all util files
  2. Document all importers
  3. Move files
  4. Update 47 import paths
```

### 🔧 **Capabilities**

✅ **System-wide restructuring** - Move files, reorganize  
✅ **Dependency tracking** - Map ALL imports before moving  
✅ **Import management** - Auto-update all import paths  
✅ **Component extraction** - Break down large components  
✅ **Loading pattern enforcement** - Replace early returns  
✅ **4-phase process** - Discovery → Planning → Execution → Verification  

### ⚠️ **Critical Rules**

🔴 **NEVER move file without documenting ALL importers**  
🔴 **NEVER leave broken imports**  
🔴 **ALWAYS update imports immediately after move**  
🔴 **ALWAYS verify no functionality broken**  

### 📏 **Quality Metrics**

- ✅ Max 300 LOC per component  
- ✅ Max 5 nesting levels  
- ✅ Approved loading components only  
- ✅ Relative imports within modules  

### 📝 **Example Queries**

```
✅ "Tổ chức lại project structure"
✅ "Move all components to features/"
✅ "Split UserDashboard.tsx (400 LOC)"
✅ "Reorganize to feature-based architecture"
✅ "Extract reusable components"
```

### 🎯 **Output Format**

```markdown
## Refactoring Plan

### Current Structure Analysis
- src/: 127 files, 3 levels deep
- Issues: Mixed concerns, large files
- UserDashboard.tsx: 412 LOC (exceeds 300)

### Proposed Structure
src/
├── features/
│   ├── auth/
│   ├── users/
│   └── dashboard/
└── shared/
    └── components/

### Dependency Map
UserDashboard.tsx imported by:
- App.tsx:12
- Routes.tsx:34
- DashboardLayout.tsx:8

### Migration Steps
1. Create features/ directory
2. Move UserDashboard.tsx → features/dashboard/
3. Update 3 import paths
4. Extract UserProfile component (150 LOC)
5. Verify build passes

### Risk Assessment
- Risk: Medium (3 importers)
- Mitigation: Update imports in single commit
```

---

## 📋 Agent 4: code-refactorer

### 🎯 **Chức Năng Chính**
**"Cleaner của codebase"** - Cải thiện code quality ở function-level, không di chuyển files

### ✅ **Khi Nào Dùng**

**Scenario 1 - Improve Function**:
```
User: "This function is 200 lines and hard to understand"
→ code-refactorer:
  1. Analyze function structure
  2. Identify repeated patterns
  3. Extract helper functions
  4. Improve naming
  5. Reduce complexity
```

**Scenario 2 - Clean Up Code**:
```
User: "Clean up authentication code"
→ code-refactorer:
  1. Find duplicated logic
  2. Improve variable names
  3. Simplify nested conditionals
  4. Add comments
```

**Scenario 3 - Remove Duplication**:
```
User: "Remove duplicate validation logic"
→ code-refactorer:
  1. Find all validation blocks
  2. Extract to validateInput()
  3. Replace all usages
  4. Preserve exact behavior
```

### 🔧 **Capabilities**

✅ **Function-level improvements** - Single file focus  
✅ **Readability** - Better naming, clearer logic  
✅ **Duplication removal** - Extract reusable code  
✅ **Complexity reduction** - Simplify nested logic  
✅ **Pattern recognition** - Apply design patterns  
✅ **Preserve functionality** - ZERO behavior changes  

### ❌ **KHÔNG Làm**

❌ Không move files (dùng refactor-master)  
❌ Không add features  
❌ Không change external behavior  
❌ Không system-wide restructuring  

### 📝 **Example Queries**

```
✅ "Improve this function readability"
✅ "Remove duplicate code in validation"
✅ "Simplify nested if statements"
✅ "Better variable naming"
✅ "Extract repeated pattern to helper"
```

### 🎯 **Output Format**

```markdown
## Code Refactoring Analysis

### Current Code Issues
1. **Function Size**: getUserData() is 210 LOC
2. **Duplication**: Validation repeated 4 times
3. **Naming**: Variable 'x' unclear
4. **Complexity**: 6 levels of nesting

### Proposed Improvements

#### Issue 1: Extract Validation
**Before**:
```typescript
if (user && user.email && user.email.includes('@')) {
  // repeated 4 times
}
```

**After**:
```typescript
function validateEmail(email: string): boolean {
  return email?.includes('@') ?? false;
}
```

#### Issue 2: Improve Naming
**Before**: `const x = await fetch(url)`
**After**: `const userData = await fetch(userApiUrl)`

### Verification
- ✅ All tests pass
- ✅ No behavior changes
- ✅ Reduced LOC: 210 → 142
- ✅ Complexity: 6 → 3 levels
```

---

## 📋 Agent 5: code-reviewer

### 🎯 **Chức Năng Chính**
**"Quality Gate của codebase"** - Review code trước merge, check security, validate quality

### ✅ **Khi Nào Dùng**

**Scenario 1 - Before Merge**:
```
User: "Review this PR before merging"
→ code-reviewer:
  1. Check security (OWASP Top 10)
  2. Validate type safety
  3. Review performance
  4. Check architecture compliance
  5. Generate detailed report
```

**Scenario 2 - Security Audit**:
```
User: "Check auth code for vulnerabilities"
→ code-reviewer:
  1. Scan for SQL injection
  2. Check JWT handling
  3. Validate input sanitization
  4. Review secrets management
```

**Scenario 3 - Quality Validation**:
```
User: "Validate code quality for production"
→ code-reviewer:
  1. Run linters
  2. Check test coverage
  3. Review error handling
  4. Validate build config
```

### 🔧 **Capabilities**

✅ **Security audit** - OWASP, vulnerabilities, secrets  
✅ **Quality assessment** - Standards, readability, maintainability  
✅ **Type safety** - TypeScript validation  
✅ **Performance analysis** - Bottlenecks, N+1 queries  
✅ **Architecture review** - Pattern compliance  
✅ **Build validation** - Config, environment, deployment  
✅ **Automated checks** - Linters, tests via Bash  
✅ **Severity scoring** - A-F grades  
✅ **Delegation** - To security-guardian, performance-optimizer  

### 🎯 **Review Scope**

**7 dimensions**:
1. 🔒 **Security** - Vulnerabilities, secrets, OWASP
2. 📊 **Quality** - Standards, readability, maintainability
3. 🎯 **Type Safety** - TypeScript strictness
4. ⚡ **Performance** - Bottlenecks, memory leaks
5. 🏗️ **Architecture** - Pattern consistency
6. 🧪 **Testing** - Coverage, edge cases
7. 📦 **Build** - Configuration, deployment

### 📝 **Example Queries**

```
✅ "Review this PR"
✅ "Check security vulnerabilities"
✅ "Validate code quality"
✅ "Review before production deploy"
✅ "Đánh giá chất lượng code"
```

### 🎯 **Output Format**

```markdown
# Code Review – PR #123 (2025-01-08)

## Executive Summary
| Metric | Result |
|--------|--------|
| Overall Assessment | Good |
| Security Score | B+ |
| Maintainability | A |
| Test Coverage | 78% |

## 🔴 Critical Issues
| File:Line | Issue | Why Critical | Fix |
|-----------|-------|--------------|-----|
| auth.js:42 | Plain-text API key | Leakage risk | Use env vars |

## 🟡 Major Issues
- Missing error handling in payment.ts:89
- N+1 query in getUserOrders()

## 🟢 Minor Suggestions
- Improve naming: getUserData() → fetchUserProfile()
- Add JSDoc to public APIs

## 🔵 Architecture Considerations
| Aspect | Assessment | Notes |
|--------|------------|-------|
| System Integration | Good | Proper service boundaries |
| Design Patterns | Consistent | Follows repository pattern |

## Positive Highlights
- ✅ Well-structured React hooks
- ✅ Good test coverage (78%)
- ✅ TypeScript strict mode enabled

## Action Checklist
- [ ] Move API key to .env
- [ ] Add try-catch in payment flow
- [ ] Optimize getUserOrders query
```

---

## 🔄 Agent Interaction Flow

### Typical Workflow

```
1. USER: "I want to improve our codebase"

2. code-searcher:
   → Find problem areas
   → Locate technical debt

3. codebase-research-analyst:
   → Analyze architecture
   → Map dependencies
   → Impact assessment

4. code-refactor-master:
   → Plan restructuring
   → Move files
   → Update imports

5. code-refactorer:
   → Improve individual functions
   → Clean up code
   → Remove duplication

6. code-reviewer:
   → Validate all changes
   → Security check
   → Quality gate
```

---

## 📊 Comparison Table - Side by Side

| Aspect | code-searcher | codebase-research-analyst | code-refactor-master | code-refactorer | code-reviewer |
|--------|--------------|---------------------------|---------------------|----------------|--------------|
| **Primary Goal** | Find code fast | Understand architecture | Reorganize structure | Improve code quality | Validate quality |
| **Scope** | Single query | Deep analysis | System-wide | Function-level | Comprehensive review |
| **Speed** | ⚡⚡⚡⚡⚡ Very fast | ⚡⚡⚡ Medium | ⚡⚡ Slow | ⚡⚡⚡ Medium | ⚡⚡⚡ Medium |
| **Depth** | 🔍 Shallow | 🔍🔍🔍🔍 Very deep | 🔍🔍🔍 Deep | 🔍🔍 Moderate | 🔍🔍🔍🔍 Very deep |
| **Changes Code** | ❌ No | ❌ No | ✅ Yes | ✅ Yes | ❌ No |
| **Moves Files** | ❌ No | ❌ No | ✅ Yes | ❌ No | ❌ No |
| **Security Check** | ❌ No | ❌ No | ❌ No | ❌ No | ✅ Yes |
| **When to use** | Quick lookups | Before big changes | Restructuring | Local improvements | Before merge |

---

## 🎯 Decision Tree

```
START: "I need help with code"
│
├─ "Where is X?" / "Find Y"
│  └─ ✅ code-searcher
│
├─ "How does X work?" / "Analyze dependencies"
│  └─ ✅ codebase-research-analyst
│
├─ "Reorganize project" / "Move files"
│  └─ ✅ code-refactor-master
│
├─ "Improve this function" / "Clean up code"
│  └─ ✅ code-refactorer
│
└─ "Review code" / "Check security"
   └─ ✅ code-reviewer
```

---

## 💡 Real-World Scenarios

### Scenario 1: New Feature Development

**Task**: Add payment processing feature

```
Step 1: code-searcher
→ "Find existing payment code"
→ Located: old-payments.ts (deprecated)

Step 2: codebase-research-analyst
→ "Analyze payment architecture"
→ Found: Stripe integration, webhook handlers

Step 3: code-refactor-master
→ "Reorganize to features/payments/"
→ Created new structure, updated imports

Step 4: code-refactorer
→ "Improve payment validation logic"
→ Extracted validatePayment(), reduced duplication

Step 5: code-reviewer
→ "Review payment feature before merge"
→ Found security issue: Missing input sanitization
→ Grade: B+ (after fix: A-)
```

---

### Scenario 2: Technical Debt Cleanup

**Task**: Clean up messy authentication code

```
Step 1: code-searcher
→ "Find all auth-related files"
→ Found: 8 files, mixed patterns

Step 2: codebase-research-analyst
→ "Map auth dependencies"
→ Complexity: High, 15 files depend on auth

Step 3: code-refactor-master
→ "Consolidate auth into auth/ module"
→ Moved 8 files, updated 47 imports

Step 4: code-refactorer
→ "Clean up auth logic"
→ Removed duplication, improved naming

Step 5: code-reviewer
→ "Security audit auth module"
→ Found: 2 vulnerabilities, fixed
→ Final grade: A
```

---

### Scenario 3: Bug Investigation

**Task**: Fix performance issue in user dashboard

```
Step 1: code-searcher
→ "Find UserDashboard rendering logic"
→ Located: Dashboard.tsx:145-289

Step 2: codebase-research-analyst
→ "Trace UserDashboard dependencies"
→ Found: Loads 5 services, potential N+1 queries

Step 3: code-refactor-master
→ "Split Dashboard into smaller components"
→ Extracted: UserProfile, UserActivity, UserSettings

Step 4: code-refactorer
→ "Optimize data fetching"
→ Combined queries, added caching

Step 5: code-reviewer
→ "Review performance fixes"
→ Performance improved 3x
→ Grade: A
```

---

## 📚 Cheat Sheet - Từng Agent

### 🔍 code-searcher
```yaml
Use when: "Where is...", "Find...", "Locate..."
Triggers: find, where, locate, search, tìm
Output: File paths + line numbers
Speed: ⚡⚡⚡⚡⚡ (fastest)
Specialty: CoD ultra-concise mode
```

### 🔬 codebase-research-analyst
```yaml
Use when: "How does...", "Analyze...", "Dependencies..."
Triggers: analyze, architecture, dependencies, phân tích
Output: Architecture diagrams, dependency maps
Speed: ⚡⚡⚡ (medium, thorough)
Specialty: Impact assessment
```

### 🏗️ code-refactor-master
```yaml
Use when: "Reorganize...", "Move...", "Restructure..."
Triggers: reorganize, restructure, move, tổ chức lại
Output: New structure + migration plan
Speed: ⚡⚡ (slower, comprehensive)
Specialty: System-wide refactoring
```

### 🧹 code-refactorer
```yaml
Use when: "Improve...", "Clean up...", "Simplify..."
Triggers: refactor, improve, clean-up, cải thiện
Output: Improved code + explanations
Speed: ⚡⚡⚡ (medium)
Specialty: Function-level quality
```

### ✅ code-reviewer
```yaml
Use when: "Review...", "Check security...", "Validate..."
Triggers: review, pr-review, security, validate
Output: Detailed review report with grades
Speed: ⚡⚡⚡ (medium, comprehensive)
Specialty: Security + quality gate
```

---

## 🎓 Key Takeaways

### 1. **Clear Separation**

- **Searcher** = Find (fast)
- **Analyst** = Understand (deep)
- **Refactor-Master** = Reorganize (system)
- **Refactorer** = Improve (local)
- **Reviewer** = Validate (quality)

### 2. **No Overlap** (after fixes)

Each agent có scope rõ ràng, không duplicate

### 3. **Complementary**

Agents work together trong typical workflows

### 4. **Specialized Tools**

- Searcher: CoD mode
- Analyst: Dependency mapping
- Refactor-Master: Import management
- Refactorer: Pattern recognition
- Reviewer: Security audit + Bash execution

---

## 📞 Quick Reference

**Câu hỏi nhanh**:

| Query | Agent |
|-------|-------|
| "Tìm function X" | code-searcher |
| "Hiểu architecture" | codebase-research-analyst |
| "Tổ chức lại files" | code-refactor-master |
| "Cải thiện function" | code-refactorer |
| "Review PR" | code-reviewer |
| "Find bug location" | code-searcher |
| "Impact nếu change X" | codebase-research-analyst |
| "Move module Y" | code-refactor-master |
| "Xóa duplicate code" | code-refactorer |
| "Check security" | code-reviewer |

---

**Status**: ✅ **COMPLETE**  
**Next**: Apply triggers differentiation để avoid conflicts
