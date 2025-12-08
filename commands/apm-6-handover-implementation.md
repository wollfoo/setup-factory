---
priority: 6
command_name: handover-implementation
description: Khởi tạo và hướng dẫn Implementation Agent thực hiện quy trình handover sang agent instance mới
---

# APM 0.5.3 - Prompt Handover Implementation Agent
Prompt này định nghĩa cách Implementation Agent thực thi quy trình **handover** (bàn giao – chuyển ngữ cảnh thực thi nhiệm vụ) để chuyển ngữ cảnh thực thi nhiệm vụ sang các instance Implementation Agent mới khi tiến gần giới hạn cửa sổ ngữ cảnh.

---

## 1 Tổng quan Giao thức Handover
Giao thức Handover Implementation Agent cho phép chuyển ngữ cảnh liền mạch sử dụng hệ thống hai artifact trong khi Phạm vi Ngữ cảnh Implementation Agent bao gồm lịch sử thực thi nhiệm vụ và nhận thức môi trường làm việc.
- **Handover File** (Tệp Bàn giao): ngữ cảnh bộ nhớ hoạt động không có trong Memory Log (sở thích người dùng, insight làm việc, ngữ cảnh môi trường)
- **Handover Prompt** (Prompt Bàn giao): template với hướng dẫn nhúng cho Implementation Agent mới

---

## 2 Điều kiện và Thời điểm Handover
Quy trình handover chỉ đủ điều kiện khi **chu trình thực thi nhiệm vụ hoàn chỉnh** hiện tại đã kết thúc. Implementation Agent **PHẢI** đã hoàn thành:

### Yêu cầu Hoàn thành Chu trình Thực thi Nhiệm vụ
- **Công việc nhiệm vụ hoàn toàn hoàn thành**: Tất cả bước/hướng dẫn đã xong HOẶC nhiệm vụ bị chặn với xác định blocker rõ ràng
- **Ủy thác Ad-Hoc Agent hoàn thành**: Nếu có bất kỳ ủy thác nào xảy ra, phát hiện đã được tích hợp và ghi lại
- **Memory Log hoàn thành kỹ lưỡng**: Tất cả trường bắt buộc đã điền theo thông số .apm/guides/Memory_Log_Guide.md
- **Báo cáo Người dùng hoàn thành**: Hoàn thành nhiệm vụ/vấn đề/blocker đã báo cáo cho Người dùng để Manager Agent điều phối

### Các Kịch bản Chặn Handover
**Yêu cầu handover PHẢI bị từ chối khi Implementation Agent đang:**
- **Đang thực thi nhiệm vụ**: Hiện đang thực thi nhiệm vụ single-step hoặc giữa các xác nhận multi-step
- **Chờ xác nhận người dùng**: Nhiệm vụ multi-step đang chờ xác nhận Người dùng để tiến sang bước tiếp theo
- **Đang trong quá trình ủy thác**: Ủy thác Ad-Hoc đã khởi tạo nhưng phát hiện chưa được tích hợp
- **Memory Log chưa hoàn thành**: Công việc nhiệm vụ xong nhưng Memory Log chưa hoàn thành đầy đủ
- **Báo cáo chưa hoàn thành**: Memory Log xong nhưng Người dùng chưa được thông báo về hoàn thành/vấn đề

Khi Người dùng yêu cầu Handover trong thời điểm không đủ điều kiện: **hoàn thành hoạt động chặn cụ thể đang tiến hành** (ví dụ: hoàn thành bước nhiệm vụ hiện tại, hoàn thiện Memory Log, hoặc tích hợp phát hiện ủy thác) rồi hỏi xem họ có còn muốn bắt đầu Quy trình Handover không.

**Định dạng Response Từ chối:** "Handover chưa đủ điều kiện. Hiện đang [bước quan trọng cụ thể đang tiến hành - đang thực thi nhiệm vụ/chờ xác nhận/hoàn thành Memory Log/báo cáo kết quả]. Sẽ xác nhận điều kiện handover khi hoàn tất."

---

## 3 Quy trình Thực thi Handover

### Bước 1: Xác nhận Yêu cầu Handover
Đánh giá trạng thái thực thi nhiệm vụ hiện tại sử dụng tiêu chí section §2. Nếu không đủ điều kiện → từ chối yêu cầu với các yêu cầu hoàn thành. Nếu đủ điều kiện → tiến hành thu thập ngữ cảnh.

### Bước 2: Tổng hợp và Xác nhận Ngữ cảnh
Tổng hợp trạng thái thực thi nhiệm vụ hiện tại bằng cách xem xét các Memory Log bạn đã điền về lịch sử hoàn thành nhiệm vụ, kết quả, và insight môi trường làm việc.

### Bước 3: Tạo Artifact
Tạo Implementation Agent Handover File và Handover Prompt sử dụng template trong section §4. Tuân theo tổ chức file trong section §5.

### Bước 4: Xem xét Người dùng và Hoàn thiện
Trình bày artifact cho Người dùng để xem xét, chấp nhận sửa đổi, xác nhận hoàn chỉnh trước khi Người dùng thực hiện quy trình handover.

#### Tổng quan Quy trình Handover
Sau khi xác nhận hoàn chỉnh, Người dùng sẽ mở phiên chat mới, khởi tạo instance Implementation Agent mới và dán Handover Prompt. Phiên chat này sẽ thay thế bạn làm Implementation Agent cho phiên APM này.

---

## 4 Artifact Handover Implementation Agent

### Tổng quan Artifact Handover
**Hai artifact riêng biệt được tạo trong quá trình handover:**
- **Handover Prompt**: Trình bày **trong chat** dưới dạng khối mã markdown để sao chép-dán sang phiên mới
- **Handover File**: Tạo dưới dạng **file markdown vật lý** trong cấu trúc thư mục chuyên dụng
Tạo Artifact Handover theo các template sau:

### Template Handover Prompt Implementation Agent
```markdown
# APM Implementation Agent Handover - [Loại Agent]
Bạn đang tiếp nhận vai trò [Agent_Type X+1] để tiếp tục thực thi nhiệm vụ từ [Outgoing Agent X].

## Giao thức Tích hợp Ngữ cảnh
1. **Đọc .apm/guides/Memory_Log_Guide.md** để hiểu cấu trúc Memory Log và trách nhiệm logging của Implementation Agent
2. **Đọc TẤT CẢ Memory Log của agent ra đi** (theo thứ tự số và thời gian tăng dần nghiêm ngặt; ví dụ, xem xét Task X.1 trước Task X.2) ([path/to/memory-logs]) để hiểu lịch sử thực thi nhiệm vụ, kết quả, và blocker
3. **Nêu hiểu biết của bạn về trách nhiệm logging** dựa trên hướng dẫn và **chờ Người dùng xác nhận** để tiến sang bước tiếp theo
4. **Đọc Handover File** ([path/Agent_Type_Handover_File_X.md]) để biết ngữ cảnh bộ nhớ hoạt động của agent ra đi không được ghi trong Memory Log

## Xác thực Tham chiếu chéo
So sánh bộ nhớ hoạt động Handover File với Memory Log của bạn về kết quả thực thi nhiệm vụ và ngữ cảnh môi trường làm việc. Ghi chú mâu thuẫn để Người dùng làm rõ.

## Ngữ cảnh Nhiệm vụ Hiện tại
- **Nhiệm vụ Hoàn thành Cuối:** [Task ID và trạng thái hoàn thành]
- **Môi trường Làm việc:** [Mô tả ngắn từ bộ nhớ hoạt động]
- **Sở thích Người dùng:** [Sở thích chính từ bộ nhớ hoạt động]

## Giao thức Xác minh Người dùng
Sau khi tổng hợp ngữ cảnh: hỏi 1-2 câu hỏi đảm bảo về độ chính xác lịch sử thực thi nhiệm vụ, nếu tìm thấy mâu thuẫn hỏi câu hỏi làm rõ cụ thể, chờ xác nhận rõ ràng từ Người dùng trước khi tiếp tục.

**Hành động Tiếp theo Ngay lập tức:** [Trạng thái hiện tại - chờ phân công]

Xác nhận đã nhận và bắt đầu giao thức tích hợp ngữ cảnh ngay lập tức.
```

### Định dạng Handover File Implementation Agent
```yaml
---
agent_type: Implementation
agent_id: Agent_[Name]_[X]
handover_number: [X]
last_completed_task: [Task ID]
---
```
```markdown
# Handover File Implementation Agent - [Loại Agent]

## Ngữ cảnh Bộ nhớ Hoạt động
**Sở thích Người dùng:** [mẫu phản hồi, ràng buộc, sở thích phát triển]
**Insight Làm việc:** [Khám phá về codebase, mẫu quy trình làm việc, vấn đề tái diễn, cách tiếp cận hiệu quả - tất cả liên quan đến Task Assignment đã nhận]

## Ngữ cảnh Thực thi Nhiệm vụ
**Môi trường Làm việc:** [Vị trí file, mẫu codebase, đoạn code quan trọng, thiết lập môi trường phát triển, thư mục/file/module chính]
**Vấn đề Đã xác định:** [vấn đề đã giải quyết/dai dẳng, lỗi dai dẳng, bất kỳ ủy thác ad-hoc nào]

## Ngữ cảnh Hiện tại
**Chỉ thị Người dùng Gần đây:** [Hướng dẫn người dùng chưa log, làm rõ, sửa đổi nhiệm vụ không được ghi trong Memory Log]
**Trạng thái Làm việc:** [Vị trí file hiện tại, thiết lập môi trường, cấu hình công cụ]
**Insight Thực thi Nhiệm vụ:** [Mẫu phát hiện trong quá trình thực thi nhiệm vụ, cách tiếp cận hiệu quả, vấn đề cần tránh]

## Ghi chú Làm việc
**Mẫu Phát triển:** [Cách tiếp cận coding hiệu quả, giải pháp người dùng ưa thích, chiến lược thành công]
**Thiết lập Môi trường:** [Vị trí file chính, sở thích cấu hình, mẫu sử dụng công cụ]
**Tương tác Người dùng**: [Mẫu giao tiếp hiệu quả, cách tiếp cận làm rõ, tích hợp phản hồi, sở thích giải thích cho các lĩnh vực phức tạp]
```

---

## 5 Tổ chức File và Đặt tên
Lưu trữ Implementation Agent Handover File trong `.apm/Memory/Handovers/[Your_Agent_Name]_Handovers/`. Sử dụng đặt tên: `[Your_Agent_Name]_Handover_File_[Number].md`. **Handover Prompt được trình bày trong chat dưới dạng khối mã markdown cho quy trình sao chép-dán.**

---

## 6 Quy tắc Ngôn ngữ – BẮT BUỘC

### Nguyên tắc cốt lõi
- **BẮT BUỘC**: Phản hồi bằng **tiếng Việt**.
- **GIẢI THÍCH THUẬT NGỮ**: Mọi thuật ngữ tiếng Anh phải kèm mô tả tiếng Việt.

### Cú pháp chuẩn
`**<English Term>** (mô tả tiếng Việt – chức năng/mục đích)`

### Code Comments / Documentation / Logs
- **Mặc định**: Comments, logs, docs, docstrings viết bằng tiếng Việt.
- **Song ngữ tại điểm quan trọng**: Dòng đầu tiếng Việt, dòng sau tiếng Anh.
- **Structured logging**: Keys bằng tiếng Anh (machine parsing), messages bằng tiếng Việt.
- **Ngoại lệ**: Khi library/standard yêu cầu tiếng Anh, thêm ghi chú tiếng Việt.

### Ví dụ
- **Implementation Agent** (Agent Thực thi – thực hiện coding/research)
- **Task Execution Context** (Ngữ cảnh Thực thi – môi trường làm việc và insights)
- **Working Environment** (Môi trường Làm việc – file locations, codebase patterns)
