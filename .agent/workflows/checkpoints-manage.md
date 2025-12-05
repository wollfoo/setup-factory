---
description: Manage checkpoints - list, view, clear, archive
auto_execution_mode: 3
---

# Checkpoints Management Workflow

## Commands Overview

```bash
/checkpoints list              # Liệt kê tất cả
/checkpoints view [file]       # Xem chi tiết
/checkpoints resume [file]     # Resume từ file
/checkpoints clear [options]   # Xoá có chọn lọc
/checkpoints archive [options] # Archive thay vì xoá
```

---

## `/checkpoints clear` - Xoá có chọn lọc

### Syntax

```bash
/checkpoints clear "<goal/task description>"
```

### Primary Usage

Argument chính là **goal/task description** - xoá tất cả sessions liên quan đến mục tiêu đó.

```bash
# Xoá tất cả sessions của goal này
/checkpoints clear "phát triển Handoff System cho Windsurf"

# Xoá sessions liên quan đến auth
/checkpoints clear "implement authentication"

# Xoá sessions về API design
/checkpoints clear "API design"
```

### Optional Filters

| Option | Description | Example |
|--------|-------------|----------|
| `--type` | Chỉ xoá loại cụ thể | `--type checkpoint` |
| `--before` | Chỉ xoá trước ngày | `--before 2025-12-01` |
| `--dry-run` | Preview không xoá thật | `--dry-run` |
| `--all` | Xoá TẤT CẢ (không cần goal) | `--all` |

### Examples

```bash
# Xoá tất cả sessions của một goal
/checkpoints clear "phát triển Handoff System"

# Chỉ xoá checkpoints (giữ handoffs)
/checkpoints clear "Handoff System" --type checkpoint

# Chỉ xoá handoffs cũ
/checkpoints clear "Handoff System" --type handoff --before 2025-12-01

# Preview trước khi xoá
/checkpoints clear "Handoff System" --dry-run

# Xoá TẤT CẢ mọi thứ (dangerous)
/checkpoints clear --all
```

---

## Workflow Steps

### Step 1: Parse Input

```yaml
input: /checkpoints clear "<goal>" [options]

parse:
  goal: string | null      # Primary - match against task/goal in files
  type: checkpoint | handoff | null
  before: YYYY-MM-DD | null
  all: boolean             # If true, ignore goal requirement
  dry_run: boolean
```

### Step 2: Find Matching Files

```
1. Scan .handoff/checkpoints/
2. Exclude _index.md
3. For each file:
   a. Read frontmatter (goal, task, type, created)
   b. Match goal against:
      - frontmatter.goal field
      - frontmatter.task field  
      - filename task segment
      - file content "# Handoff:" or "# Checkpoint:" title
   c. Apply optional filters (--type, --before)
4. Return list of matching files
```

### Matching Logic

```
Goal: "phát triển Handoff System"

Matches:
✅ goal: "Tiếp tục phát triển Handoff System"  (contains)
✅ task: "Handoff System Development"           (contains "Handoff System")
✅ filename: handoff-handoff-system-*.md        (contains)
✅ title: "# Handoff: Handoff System Testing"   (contains)

Not matches:
❌ goal: "implement authentication"             (no overlap)
```

### Step 3: Confirm (nếu không phải dry-run)

```markdown
## 🗑️ Files sẽ bị xoá:

| File | Type | Date | Status |
|------|------|------|--------|
| checkpoint-auth-impl-2025-12-01-1430.md | checkpoint | 2025-12-01 | in_progress |
| handoff-auth-impl-2025-12-02-0900.md | handoff | 2025-12-02 | transferred |

**Total: 2 files**

⚠️ Confirm xoá? (yes/no)
```

### Step 4: Execute Delete

```
1. Delete matching files
2. Update _index.md:
   - Remove entries for deleted files
   - Keep remaining entries
3. Report results
```

### Step 5: Report

```markdown
✅ Cleared 2 files:
- checkpoint-auth-impl-2025-12-01-1430.md
- handoff-auth-impl-2025-12-02-0900.md

📍 Index updated: _index.md
💡 Remaining: 5 checkpoints, 3 handoffs
```

---

## `/checkpoints archive` - Archive thay vì xoá

### Khi nào dùng
- Muốn giữ lại để reference
- Không muốn xoá vĩnh viễn

### Workflow
```
1. Move files to .handoff/checkpoints/archive/
2. Update _index.md
3. Archived files không hiện trong list mặc định
```

### Command
```bash
/checkpoints archive --task "old-project"
/checkpoints archive --before 2025-11-01
```

---

## `/checkpoints list` - Enhanced

### Options

```bash
/checkpoints list                    # List active only
/checkpoints list --all              # Include archived
/checkpoints list --type handoff     # Filter by type
/checkpoints list --task "auth"      # Filter by task
```

### Output Format

```markdown
## 📋 Checkpoints & Handoffs

### Active (3)
| Type | Task | Date | Status | File |
|------|------|------|--------|------|
| 🔄 checkpoint | Auth Impl | 2025-12-03 | in_progress | checkpoint-auth-*.md |
| 📤 handoff | API Design | 2025-12-02 | ready | handoff-api-*.md |

### Archived (2)
| Type | Task | Date | File |
|------|------|------|------|
| 📦 checkpoint | Old Task | 2025-11-15 | archive/checkpoint-old-*.md |
```

---

## Safety Rules

### Protected Actions
- `--all` luôn yêu cầu confirm
- Không cho xoá `_index.md`
- `--dry-run` mặc định cho lần đầu

### Confirmation Required
```yaml
require_confirm:
  - --all flag used
  - >5 files affected
  - files with status: in_progress
```

### No Confirm Needed
```yaml
auto_execute:
  - --dry-run (preview only)
  - status: transferred (đã hoàn thành)
  - 1-2 files với explicit --task
```

---

## Integration

### Với _index.md
- Mỗi thao tác clear/archive đều update index
- Index là source of truth cho list command

### Với Handoff Workflow
- Sau khi resume thành công, có thể auto-suggest clear
- Transferred handoffs là candidates cho cleanup

### Storage Structure
```
.handoff/checkpoints/
├── _index.md
├── checkpoint-*.md
├── handoff-*.md
└── archive/
    ├── checkpoint-*.md
    └── handoff-*.md
```