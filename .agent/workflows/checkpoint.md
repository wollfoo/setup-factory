---
description: Save current context checkpoint without switching sessions
auto_execution_mode: 3
---

# Checkpoint Workflow

## Mục Đích

**Checkpoint** = Lưu trạng thái hiện tại để resume sau, KHÔNG chuyển session.

---

## Step 1: Capture State

- [ ] **Goal**: Mục tiêu đang làm
- [ ] **Progress**: Đã làm được gì
- [ ] **Pending**: Còn gì chưa làm
- [ ] **Files**: Danh sách files đã modify
- [ ] **Decisions**: Các quyết định quan trọng

---

## Step 2: Create Checkpoint

### File: `.handoff/checkpoints/checkpoint-[task]-[timestamp].md`

```markdown
---
type: checkpoint
created: YYYY-MM-DD HH:MM
task: [task name]
status: in_progress
---

# Checkpoint: [Task Name]

## Current Goal
[Mục tiêu chính]

## Progress
- [x] Done item
- [ ] In progress item

## Modified Files
- `path/file.ts` – [description]

## Key Notes
- [Important note]

## Next Steps
1. [What to do next]
```

---

## Step 3: Confirm

```
✅ Checkpoint saved: checkpoint-[task]-[timestamp].md
📍 Location: .handoff/checkpoints/
💡 Resume: /checkpoints resume [filename]
```

---

## Commands

```bash
/checkpoint                      # Save current state
/checkpoints list                # List all checkpoints
/checkpoints view [file]         # View specific checkpoint
/checkpoints resume [file]       # Resume from checkpoint
/checkpoints clear [options]     # Xoá có chọn lọc
/checkpoints archive [options]   # Archive thay vì xoá
```

### Clear Options
```bash
/checkpoints clear "goal description"  # Xoá theo goal/task
/checkpoints clear "Handoff System"    # Xoá tất cả sessions liên quan
/checkpoints clear "auth" --type checkpoint  # Chỉ xoá checkpoints
/checkpoints clear "API" --dry-run     # Preview trước
/checkpoints clear --all               # Xoá tất cả (confirm)
```

📖 Chi tiết: Xem `/checkpoints-manage` workflow

---

## Checkpoint vs Handoff

| Aspect | Checkpoint | Handoff |
|--------|------------|---------|
| Mục đích | Lưu để tiếp tục sau | Chuyển sang session mới |
| Session | Giữ nguyên | Tạo mới |
| Use case | Tạm dừng | Kết thúc phase |