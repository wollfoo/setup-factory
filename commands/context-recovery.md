---
description: Khôi phục ngữ cảnh làm việc từ phiên trước bằng cách phân tích git history và cấu trúc dự án
auto_execution_mode: 3
---

# Context Recovery Prompt

Workflow này giúp khôi phục trạng thái làm việc khi bạn đã mất ngữ cảnh từ phiên trước.

## Điều kiện kích hoạt
- Bắt đầu phiên làm việc mới sau thời gian dài
- Mất context do IDE restart hoặc conversation reset
- Cần nhanh chóng nắm bắt lại tiến độ công việc

---

## Các bước thực hiện

### 1. Kiểm tra lịch sử commit gần đây
// turbo
```bash
git log -n 3 --stat
```
- Xem 3 commit gần nhất và các file đã thay đổi
- Ghi nhận: commit message, author, thời gian, danh sách files

### 2. Phân tích thay đổi trong commit cuối cùng
// turbo
```bash
git show HEAD --stat
```
- Đọc chi tiết diff của commit cuối
- Nếu cần xem nội dung đầy đủ: `git show HEAD` (không có --stat)
- Đọc trực tiếp các file quan trọng vừa được sửa đổi

### 3. Quét cấu trúc dự án hiện tại
// turbo
```bash
ls -la
```
- Liệt kê files trong thư mục gốc
- Kiểm tra các thư mục quan trọng: `src/`, `config/`, `tests/`
- Xác định entry points và configuration files

### 4. Kiểm tra trạng thái working directory
// turbo
```bash
git status
```
- Xem có uncommitted changes không
- Kiểm tra staged files
- Phát hiện untracked files mới

### 5. Tổng hợp và đề xuất

Dựa trên thông tin thu thập, tóm tắt:

| Mục | Nội dung |
|-----|----------|
| **Tính năng vừa hoàn thành** | [Tóm tắt từ commit messages] |
| **Files trọng tâm** | [Danh sách files được sửa đổi nhiều nhất] |
| **Trạng thái hiện tại** | [Clean/Dirty/In-progress] |
| **Bước tiếp theo dự đoán** | [Fix bug / Refactor / Add feature / Testing] |

---

## Output mong đợi

```markdown
## 📋 Context Recovery Report

### Tóm tắt 3 commits gần nhất
1. `abc1234` - [message] - [time]
2. `def5678` - [message] - [time]  
3. `ghi9012` - [message] - [time]

### Phân tích commit cuối
- **Mục đích**: [Mô tả ngắn]
- **Files changed**: [Danh sách]
- **Thay đổi chính**: [Bullet points]

### Cấu trúc dự án hiện tại
[Tree hoặc list các thư mục/files quan trọng]

### Đề xuất bước tiếp theo
1. [Action item 1]
2. [Action item 2]
3. [Action item 3]
```

---

## Lưu ý
- Nếu project không dùng Git, thay thế bằng việc đọc `CHANGELOG.md` hoặc `progress.txt`
- Có thể kết hợp với `/handoff` workflow nếu cần chuyển giao context chi tiết hơn
- Ưu tiên đọc files có timestamp gần nhất