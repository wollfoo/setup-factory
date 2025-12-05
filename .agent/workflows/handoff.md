---
description: Context handoff - chuyển giao ngữ cảnh giữa các sessions/threads
auto_execution_mode: 3
---

# Handoff Workflow

## Mục Đích

**Handoff** (chuyển giao ngữ cảnh) giúp:
- Chuyển công việc từ session hiện tại sang session mới với ngữ cảnh liên quan
- Quản lý context window hiệu quả (tránh overflow)
- Đảm bảo tính liên tục khi làm việc với tasks phức tạp

---

## Step 1: Trigger Analysis

### Xác định thời điểm cần Handoff

| Trigger | Điều kiện | Hành động |
|---------|-----------|-----------|
| **Context Overflow** | >80% context window | Bắt buộc handoff |
| **Phase Transition** | Chuyển từ planning → implementation | Khuyến nghị handoff |
| **Task Completion** | Xong 1 task, bắt đầu task mới | Khuyến nghị handoff |
| **Long Session** | >30 turns trong 1 conversation | Cảnh báo + gợi ý |
| **Manual** | User yêu cầu `/handoff` | Thực hiện ngay |

---

## Step 2: Context Extraction

### Thu thập ngữ cảnh quan trọng

**Ưu tiên cao (PHẢI giữ):**
- [ ] **Decisions** – Các quyết định kiến trúc/thiết kế
- [ ] **Current State** – Trạng thái hiện tại của task
- [ ] **Modified Files** – Danh sách files đã thay đổi
- [ ] **Pending Tasks** – Tasks còn chưa hoàn thành
- [ ] **Blockers** – Vấn đề đang gặp phải

**Ưu tiên trung (NÊN giữ):**
- [ ] **Relevant Code** – Code snippets quan trọng
- [ ] **Dependencies** – Thư viện/services liên quan

---

## Step 3: Create Handoff Document

### Tạo file trong `.handoff/checkpoints/`

```markdown
---
type: handoff
created: YYYY-MM-DD HH:MM
goal: [mục tiêu cho session mới]
---

# Handoff: [Task Name]

## Context Summary

### 🎯 Goal
[Mục tiêu chính]

### ✅ Completed
- [x] Task đã hoàn thành

### 🔄 In Progress  
- [ ] Task đang làm dở

### 📁 Modified Files
- `path/to/file.ts` – [mô tả]

### 💡 Key Decisions
1. **[Decision]**: [Lý do]

## Resume Prompt
[Prompt để bắt đầu session mới]
```

---

## Step 4: Generate Resume Prompt

Tạo prompt sẵn cho session mới:

```markdown
## 📋 Resume Prompt

Tiếp tục task: **[Task Name]**

### Context
[2-3 câu tóm tắt]

### Files cần xem
@file1.ts @file2.ts

### Next action
[Hành động cần làm tiếp]

### Reference
`.handoff/checkpoints/[filename].md`
```

---

## Step 5: Verify & Complete

- [ ] File handoff đã được lưu
- [ ] Resume prompt đã generate
- [ ] Files quan trọng đã được list
- [ ] Next steps rõ ràng

---

## Quick Commands

```
/handoff [goal]              # Full handoff
/handoff implement the API   # Với goal cụ thể
/checkpoint                  # Chỉ save, không switch
```

---

## Best Practices

### ✅ DO
- Handoff khi chuyển phase
- Giữ sessions 15-20 turns
- Ghi rõ decisions và lý do

### ❌ DON'T
- Đợi đến overflow mới handoff
- Bỏ qua pending tasks
- Handoff không có next steps