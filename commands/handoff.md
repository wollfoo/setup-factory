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

### Tự động phát hiện
```
Nếu phát hiện các dấu hiệu sau, gợi ý handoff:
- Lặp lại context đã đề cập trước đó
- Response bị cắt ngắn do limit
- User phải re-explain các quyết định cũ
```

---

## Step 2: Context Extraction

### 2.1 Thu thập ngữ cảnh quan trọng

**Danh mục ưu tiên cao (PHẢI giữ):**
- [ ] **Decisions** – Các quyết định kiến trúc/thiết kế
- [ ] **Current State** – Trạng thái hiện tại của task
- [ ] **Modified Files** – Danh sách files đã thay đổi
- [ ] **Pending Tasks** – Tasks còn chưa hoàn thành
- [ ] **Blockers** – Vấn đề đang gặp phải

**Danh mục ưu tiên trung (NÊN giữ):**
- [ ] **Relevant Code** – Code snippets quan trọng
- [ ] **Dependencies** – Thư viện/services liên quan
- [ ] **User Preferences** – Yêu cầu đặc biệt của user

**Danh mục ưu tiên thấp (CÓ THỂ bỏ):**
- Discussion chi tiết
- Attempts thất bại
- Debug logs đã xử lý

### 2.2 Template trích xuất

```markdown
## Context Summary

### 🎯 Goal
[Mục tiêu chính của task hiện tại]

### ✅ Completed
- [x] Task đã hoàn thành 1
- [x] Task đã hoàn thành 2

### 🔄 In Progress  
- [ ] Task đang làm dở
- [ ] Task cần tiếp tục

### 📁 Modified Files
- `path/to/file1.ts` – [mô tả thay đổi]
- `path/to/file2.ts` – [mô tả thay đổi]

### 💡 Key Decisions
1. **[Decision]**: [Lý do]
2. **[Decision]**: [Lý do]

### ⚠️ Notes
- [Lưu ý quan trọng]
- [Blockers nếu có]
```

---

## Step 3: Create Handoff Document

### 3.1 Tạo file checkpoint

Tạo file trong `.handoff/checkpoints/`:

```
.handoff/checkpoints/
└── handoff-[task-name]-[YYYY-MM-DD-HHMM].md
```

### 3.2 Cấu trúc file handoff

```markdown
---
type: handoff
created: YYYY-MM-DD HH:MM
from_session: [session_id hoặc mô tả]
goal: [mục tiêu cho session mới]
status: draft | ready | transferred
---

# Handoff: [Task Name]

## Origin Context
[Tóm tắt ngắn gọn session trước]

## Extracted Context
[Nội dung từ Step 2.2]

## Next Steps
1. [Bước tiếp theo cần làm]
2. [Bước tiếp theo]
3. [...]

## Relevant Files
@path/to/file1.ts
@path/to/file2.ts
@path/to/file3.ts

## Resume Prompt
[Prompt gợi ý để bắt đầu session mới]
```

---

## Step 4: Execute Handoff

### 4.1 Lưu checkpoint
```bash
# AI tự động tạo file handoff
.handoff/checkpoints/handoff-[name]-[timestamp].md
```

### 4.2 Generate resume prompt

Tạo prompt sẵn để user copy vào session mới:

```markdown
## 📋 Resume Prompt (Copy này vào session mới)

---
Tiếp tục task: **[Task Name]**

### Context
[2-3 câu tóm tắt]

### Files cần xem
@file1.ts @file2.ts @file3.ts

### Next action
[Hành động cụ thể cần làm tiếp]

### Reference
Xem chi tiết: `.handoff/checkpoints/[filename].md`
---
```

### 4.3 Verify trước khi hoàn tất

- [ ] File handoff đã được lưu
- [ ] Resume prompt đã generate
- [ ] Files quan trọng đã được list
- [ ] Next steps rõ ràng

---

## Step 5: Resume in New Session

### 5.1 Load context

Khi bắt đầu session mới:
1. User paste resume prompt
2. AI đọc handoff file từ checkpoint
3. AI đọc các files được mention
4. Tiếp tục từ điểm dừng

### 5.2 Verify continuity

AI kiểm tra:
- [ ] Hiểu đúng goal
- [ ] Biết trạng thái hiện tại
- [ ] Có danh sách next steps
- [ ] Files relevant đã được load

---

## Quick Commands

### Manual Handoff
```
/handoff [goal cho session mới]
```

**Ví dụ:**
```
/handoff implement the API endpoints we just designed
/handoff fix the remaining test failures
/handoff deploy to staging environment
```

### View Checkpoints
```
/checkpoints list
/checkpoints view [filename]
/checkpoints resume [filename]
```

---

## Best Practices

### ✅ DO
- Handoff khi chuyển phase (design → implement → test)
- Giữ sessions focused (~15-20 turns)
- Ghi rõ decisions và lý do
- List đầy đủ files đã modify

### ❌ DON'T
- Đợi đến khi context overflow mới handoff
- Bỏ qua pending tasks khi handoff
- Handoff không có clear next steps
- Quên verify trước khi kết thúc

---

## Automation Hooks

### Auto-suggest handoff
```yaml
triggers:
  - context_usage > 0.8
  - turn_count > 30
  - phase_keyword_detected: ["done with", "now let's", "next phase"]
  
action: suggest_handoff
message: "💡 Gợi ý: Session khá dài. Bạn có muốn handoff sang session mới không?"
```

### Auto-save checkpoint
```yaml
triggers:
  - significant_decision_made
  - file_batch_modified > 3
  - user_request: "save progress"

action: auto_checkpoint
```

---

## Integration với Context System

Handoff workflow tích hợp với:
- **03-context-system.md**: Sử dụng 3-Tier context coordination
- **03b-local-memory.md**: Lưu checkpoints vào `.handoff/checkpoints/`
- **02-quality-operations.md**: Persistence standards

### Context Budget sau Handoff
| Tier | Usage | Action |
|------|-------|--------|
| Fresh Start | <30% | System A - Tactical |
| With Context | 30-50% | System A/B - Normal ops |
| Heavy Context | 50-80% | System B - Monitor |
| Near Limit | >80% | Suggest next handoff |
