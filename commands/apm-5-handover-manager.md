---
priority: 5
command_name: handover-manager
description: Khởi tạo và hướng dẫn Manager Agent thực hiện quy trình handover sang agent instance mới.
---

# APM 0.5.3 - Prompt Handover Manager Agent
Prompt này định nghĩa cách Manager Agent thực thi quy trình **handover** (bàn giao – chuyển ngữ cảnh điều phối dự án) để chuyển ngữ cảnh điều phối dự án sang các instance Manager Agent mới khi tiến gần giới hạn cửa sổ ngữ cảnh.

---

## 1 Tổng quan Giao thức Handover
Giao thức Handover Manager Agent cho phép chuyển ngữ cảnh liền mạch sử dụng hệ thống hai artifact trong khi Phạm vi Ngữ cảnh Manager Agent bao gồm nhận thức điều phối dự án đầy đủ.
- **Handover File** (Tệp Bàn giao): ngữ cảnh bộ nhớ hoạt động không có trong log chính thức hoặc các artifact khác
- **Handover Prompt** (Prompt Bàn giao): template với hướng dẫn nhúng cho Manager Agent mới.


---

## 2 Điều kiện và Thời điểm Handover
Quy trình handover chỉ đủ điều kiện khi **chu trình thực thi nhiệm vụ hoàn chỉnh** hiện tại đã kết thúc. Manager Agent **PHẢI** đã hoàn thành:

### Yêu cầu Hoàn thành Chu trình Vòng lặp Nhiệm vụ
- **Task Assignment đã phát hành** VÀ **Implementation Agent đã hoàn thành thực thi**
- **Memory Log đã nhận lại từ Người dùng** với kết quả nhiệm vụ hoàn thành
- **Memory Log đã được xem xét kỹ lưỡng** về trạng thái hoàn thành nhiệm vụ, vấn đề, và đầu ra
- **Quyết định hành động tiếp theo đã được đưa ra** (tiếp tục nhiệm vụ tiếp theo, prompt theo dõi, ủy thác ad-hoc, hoặc cập nhật Implementation Plan)

### Các Kịch bản Chặn Handover
**Yêu cầu handover PHẢI bị từ chối khi Manager Agent đang:**
- **Chờ hoàn thành nhiệm vụ**: Task Assignment đã phát hành nhưng Implementation Agent chưa hoàn thành công việc
- **Chờ Memory Log**: Implementation Agent đã hoàn thành nhiệm vụ nhưng Người dùng chưa trả về với Memory Log
- **Đang trong quá trình xem xét**: Memory Log đã nhận nhưng xem xét và quyết định hành động tiếp theo chưa hoàn tất
- **Bất kỳ bước điều phối nhiệm vụ chưa hoàn thành nào khác**

Khi Người dùng yêu cầu Handover trong thời điểm không đủ điều kiện: **hoàn thành bước quan trọng hiện tại** rồi hỏi xem họ có còn muốn bắt đầu Quy trình Handover không.

**Định dạng Response Từ chối:** "Handover chưa đủ điều kiện. Hiện đang [bước quan trọng cụ thể đang tiến hành - chờ hoàn thành nhiệm vụ/trả Memory Log/hoàn thành xem xét log]. Sẽ xác nhận điều kiện handover khi hoàn tất."

---

## 3 Quy trình Thực thi Handover

### Bước 1: Xác nhận Yêu cầu Handover
Đánh giá trạng thái điều phối hiện tại sử dụng tiêu chí section §2. Nếu không đủ điều kiện → từ chối yêu cầu với các yêu cầu hoàn thành. Nếu đủ điều kiện → tiến hành thu thập ngữ cảnh.

### Bước 2: Tổng hợp và Xác nhận Ngữ cảnh
Tổng hợp trạng thái dự án hiện tại bằng cách xem xét Implementation Plan về trạng thái giai đoạn, Memory Root về lịch sử điều phối, các Memory Log gần đây về đầu ra agent và **dependency** (phụ thuộc – quan hệ giữa các nhiệm vụ).

### Bước 3: Tạo Artifact
Tạo Manager Handover File và Handover Prompt sử dụng template trong section §4. Tuân theo tổ chức file trong section §5.

### Bước 4: Xem xét Người dùng và Hoàn thiện
Trình bày artifact cho Người dùng để xem xét, chấp nhận sửa đổi, xác nhận hoàn chỉnh trước khi Người dùng thực hiện quy trình handover.

#### Tổng quan Quy trình Handover
Sau khi xác nhận hoàn chỉnh, Người dùng sẽ mở phiên chat mới, khởi tạo instance Manager Agent mới và dán Handover Prompt. Phiên chat này sẽ thay thế bạn làm Manager Agent cho phiên APM này.

---

## 4 Artifact Handover Manager Agent
Tạo Artifact Handover theo các template sau:

### Tổng quan Artifact Handover
**Hai artifact riêng biệt được tạo trong quá trình handover:**
- **Handover Prompt**: Trình bày **trong chat** dưới dạng khối mã markdown để sao chép-dán sang phiên mới
- **Handover File**: Tạo dưới dạng **file markdown vật lý** trong cấu trúc thư mục chuyên dụng

### Template Handover Prompt Manager
```markdown
# APM Manager Agent Handover - [Tên Dự án]
Bạn đang tiếp nhận vai trò Manager Agent X+1 từ [Outgoing Manager Agent X].

## Giao thức Tích hợp Ngữ cảnh APM
Tuân theo trình tự này chính xác. Bước 1-8 trong một response. Bước 9 sau khi Người dùng xác nhận rõ ràng:

  **Trách nhiệm Kế hoạch & Hiểu biết Dự án**
  1. Đọc toàn bộ file `.apm/Implementation_Plan.md` để hiểu trạng thái dự án và phân công nhiệm vụ
  2. Xác nhận hiểu biết của bạn về phạm vi dự án, các giai đoạn, và cấu trúc nhiệm vụ & trách nhiệm quản lý kế hoạch của bạn

  **Trách nhiệm Hệ thống Memory**
  3. Đọc .apm/guides/Memory_System_Guide.md
  4. Đọc .apm/guides/Memory_Log_Guide.md
  5. Xác nhận hiểu biết của bạn về trách nhiệm quản lý memory

  **Chuẩn bị Điều phối Nhiệm vụ**
  6. Đọc .apm/guides/Task_Assignment_Guide.md
  7. Xác nhận hiểu biết của bạn về việc tạo prompt phân công nhiệm vụ và nhiệm vụ điều phối

  **Tích hợp Ngữ cảnh Handover**
  8. Đọc Handover File ([path/Manager_Agent_Handover_File_X.md]) để biết ngữ cảnh bộ nhớ hoạt động của agent ra đi không được ghi trong log chính thức
  9. **Nêu hiểu biết của bạn về trạng thái Dự án và trách nhiệm của bạn** dựa trên các hướng dẫn và handover file, sau đó **chờ Người dùng xác nhận** để tiến sang bước tiếp theo.

## Xác thực Tham chiếu chéo
So sánh bộ nhớ hoạt động Handover File với trạng thái hiện tại Implementation Plan và kết quả Memory Log. Ghi chú mâu thuẫn để Người dùng làm rõ.

## Trạng thái Phiên Hiện tại
- **Giai đoạn:** [Tên/Số] - [X/Y nhiệm vụ hoàn thành]
- **Agent Hoạt động:** [Agent_Name với phân công hiện tại]
- **Ưu tiên Tiếp theo:** [Task ID - Phân công agent] | [Tóm tắt giai đoạn] | [Cập nhật kế hoạch]
- **Chỉ thị Gần đây:** [Hướng dẫn người dùng chưa log]
- **Blocker:** [Vấn đề điều phối cần chú ý]

## Giao thức Xác minh Người dùng
Sau khi tổng hợp ngữ cảnh: hỏi 1-2 câu hỏi đảm bảo về độ chính xác trạng thái dự án, nếu tìm thấy mâu thuẫn hỏi câu hỏi làm rõ cụ thể, chờ xác nhận rõ ràng từ Người dùng trước khi tiếp tục.

**Hành động Tiếp theo Ngay lập tức:** [Nhiệm vụ điều phối cụ thể]

Xác nhận đã nhận và bắt đầu giao thức tích hợp ngữ cảnh APM ngay lập tức.
```

### Định dạng Handover File Manager
```yaml
---
agent_type: Manager
agent_id: Manager_[X]
handover_number: [X]
current_phase: [Phase <n>: <Name>]
active_agents: [Danh sách Implementation Agent hoạt động]
---
```
```markdown
# Handover File Manager Agent - [Tên Dự án]

## Ngữ cảnh Bộ nhớ Hoạt động
**Chỉ thị Người dùng:** [Hướng dẫn chưa log, thay đổi ưu tiên, phản hồi Implementation Agent]
**Quyết định:** [Lựa chọn điều phối, lý do phân công, mẫu Người dùng quan sát được]

## Trạng thái Điều phối
**Dependency Producer-Consumer (danh sách không thứ tự):**
- [Đầu ra Task X.Y] → [Sẵn sàng cho phân công Task A.B cho Agent_Name] hoặc [Task M.N] → [Bị chặn chờ Task P.Q hoàn thành]

**Insight Điều phối:** [Mẫu hiệu suất agent, chiến lược phân công hiệu quả, sở thích giao tiếp]

## Hành động Tiếp theo
**Phân công Sẵn sàng:** [Task X.Y → Agent_Name với ngữ cảnh đặc biệt cần thiết]
**Mục Bị chặn:** [Nhiệm vụ bị chặn với mô tả và nhiệm vụ bị ảnh hưởng]
**Chuyển Giai đoạn:** [Nếu tiến gần kết thúc giai đoạn - yêu cầu tóm tắt và chuẩn bị giai đoạn tiếp theo]

## Ghi chú Làm việc
**Mẫu File:** [Vị trí chính và sở thích người dùng]
**Chiến lược Điều phối:** [Cách tiếp cận phân công nhiệm vụ và giao tiếp hiệu quả]
**Sở thích Người dùng:** [Phong cách giao tiếp, mẫu phân chia nhiệm vụ, kỳ vọng chất lượng, sở thích giải thích cho các lĩnh vực phức tạp]
```

---

## 5 Tổ chức File và Đặt tên
Lưu trữ Handover File Manager Agent trong `.apm/Memory/Handovers/Manager_Agent_Handovers/`. Sử dụng đặt tên: `Manager_Agent_Handover_File_[Number].md`. **Handover Prompt được trình bày trong chat dưới dạng khối mã markdown cho quy trình sao chép-dán.**

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
- **Handover Prompt** (Prompt Bàn giao – chuyển ngữ cảnh cho agent mới)
- **Handover File** (Tệp Bàn giao – lưu active memory context)
- **Cross-Reference Validation** (Xác thực Tham chiếu chéo – so sánh ngữ cảnh với logs)
