---
description: Save current context checkpoint without switching sessions
auto_execution_mode: 3
---

# Checkpoint Workflow

## Mục Đích

**Checkpoint** (điểm lưu) = Lưu trạng thái hiện tại của session để có thể resume sau, KHÔNG chuyển sang session mới.

---

## Step 1: Capture Current State

### Thu thập thông tin
- [ ] **Goal**: Mục tiêu đang làm
- [ ] **Progress**: Đã làm được gì
- [ ] **Pending**: Còn gì chưa làm
- [ ] **Files**: Danh sách files đã modify
- [ ] **Decisions**: Các quyết định quan trọng

---

## Step 2: Create Checkpoint File

### File location
```
.handoff/checkpoints/checkpoint-[task]-[YYYY-MM-DD-HHMM].md
```

### Template
```markdown
---
type: checkpoint
created: YYYY-MM-DD HH:MM
task: [task name]
status: in_progress
context_usage: [estimate %]
---

# Checkpoint: [Task Name]

## Current Goal
[Mục tiêu chính]

## Progress
- [x] Done item 1
- [x] Done item 2
- [ ] In progress item

## Modified Files
- `path/file1.ts` – [change description]
- `path/file2.ts` – [change description]

## Key Notes
- [Important decision or note]

## Next Steps
1. [What to do next]
2. [Then this]
```

---

## Step 3: Confirm Save

### Output to user
```
✅ Checkpoint saved: checkpoint-[task]-[timestamp].md

📍 Location: .handoff/checkpoints/
📊 Context captured: [items count]
📁 Files tracked: [count]

💡 To resume later: /checkpoints resume [filename]
```

---

## Quick Reference

### Save checkpoint
```
/checkpoint
/save progress
```

### View checkpoints
```
/checkpoints list
/checkpoints view [filename]
```

### Resume from checkpoint
```
/checkpoints resume [filename]
```

### Clear checkpoints
```bash
/checkpoints clear "goal description"  # Xoá theo goal/task
/checkpoints clear "Handoff System"    # Xoá tất cả sessions liên quan
/checkpoints clear "auth" --type checkpoint  # Chỉ xoá checkpoints
/checkpoints clear "API" --dry-run     # Preview trước
/checkpoints clear --all               # Xoá tất cả (confirm)
```

📖 Chi tiết: Xem `/checkpoints-manage` workflow

---

## Khác biệt với Handoff

| Aspect | Checkpoint | Handoff |
|--------|------------|---------|
| **Mục đích** | Lưu để tiếp tục sau | Chuyển sang session mới |
| **Session** | Giữ nguyên session | Tạo session mới |
| **Output** | File lưu trữ | File + resume prompt |
| **Use case** | Tạm dừng công việc | Kết thúc phase/task |
