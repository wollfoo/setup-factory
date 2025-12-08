---
priority: 8
command_name: delegate-debug
description: Cung cấp template để ủy thác nhiệm vụ debug phức tạp cho Ad-Hoc agent
---

# APM 0.5.3 - Hướng dẫn Ủy thác Debug
Hướng dẫn này định nghĩa cách Implementation Agent ủy thác công việc **debug** (gỡ lỗi) phức tạp cho **Ad-Hoc Debug agent** (Agent Debug Đặc biệt). Sử dụng hướng dẫn này khi gặp lỗi lớn (> 2 trao đổi HOẶC vấn đề phức tạp/hệ thống ngay lập tức) như định nghĩa trong Implementation Agent Initiation Prompt hoặc nếu được chỉ định rõ ràng trong Task Assignment Prompt.

---

## 1  Tổng quan Quy trình Ủy thác
Ad-Hoc Debug agent hoạt động trong **phiên chat riêng biệt** được quản lý bởi Implementation Agent ủy thác:

### Quản lý Nhánh
- **Hoạt động Độc lập**: Ad-Hoc agent làm việc trong các phiên nhánh cô lập mà không có quyền truy cập ngữ cảnh dự án chính
- **Phối hợp Người dùng**: Người dùng mở phiên chat mới, dán prompt ủy thác, trả về với giải pháp
- **Bảo toàn Ngữ cảnh**: Phiên ủy thác vẫn mở cho khả năng tái ủy thác cho đến khi lỗi được giải quyết hoặc escalated

### Quy trình Bàn giao
1. **Tạo Prompt**: Sử dụng template bên dưới với ngữ cảnh debug đầy đủ và chi tiết lỗi
2. **Người dùng Mở Phiên**: Người dùng khởi tạo phiên chat Ad-Hoc Debug mới và dán prompt
3. **Debugger Làm việc**: Ad-Hoc agent thực sự debug và giải quyết vấn đề, hợp tác với Người dùng khi cần
4. **Người dùng Trả về**: Người dùng mang giải pháp hoạt động về cho Implementation Agent để tiếp tục nhiệm vụ

---

## 2  Template Prompt Ủy thác
Trình bày prompt ủy thác **trong chat dưới dạng một khối mã markdown duy nhất với YAML frontmatter ở đầu** để Người dùng sao chép-dán sang phiên Ad-Hoc Debug mới

```markdown
---
bug_type: [crash|logic_error|performance|integration|environment|other]
complexity: [complex|systemic|unknown]
previous_attempts: [số lần trao đổi debug đã thử bởi Implementation Agent]
delegation_attempt: [1|2|3|...]
---

# Ủy thác Debug: [Mô tả Lỗi Ngắn gọn]

## Cách tiếp cận Thực thi Debug
**Mục tiêu Chính**: Thực sự giải quyết lỗi này để cho phép tiếp tục nhiệm vụ, không phải nghiên cứu thông tin về debug
**Giải pháp Hoạt động Bắt buộc**: Cung cấp bản sửa chức năng mà Implementation Agent có thể kết hợp ngay lập tức
**Debug Trực tiếp**: Làm việc với thông báo lỗi thực tế, môi trường thực, và hợp tác Người dùng để giải quyết vấn đề
**Giao thức Escalation**: Nếu lỗi chứng minh không thể giải quyết sau các lần thử debug kỹ lưỡng, ghi lại phát hiện để escalation

## Yêu cầu Thực thi Debug
**Thực thi Terminal Bắt buộc**: Thực thi các bước tái tạo được cung cấp sử dụng quyền truy cập terminal của bạn. Làm theo các bước được liệt kê để tự tái tạo lỗi.
**Giao thức Sử dụng Công cụ**: Bạn có quyền truy cập terminal và hệ thống file. Sử dụng các công cụ này để tái tạo vấn đề thay vì yêu cầu hợp tác Người dùng ngay lập tức.
**Debug Chủ động**: Sử dụng các công cụ và lệnh có sẵn để debug chủ động thay vì mặc định hợp tác người dùng
**Chủ động Dẫn dắt**: Sở hữu quy trình debug và làm việc hướng tới giải quyết sử dụng khả năng môi trường của bạn
**Hợp tác Khi Cần**: Yêu cầu hỗ trợ Người dùng chỉ khi các lần thử tái tạo thất bại do hạn chế môi trường hoặc thiếu quyền truy cập dữ liệu cụ thể

## Hợp tác Người dùng cho Debug Phức tạp
**Cách tiếp cận Phụ**: Sử dụng khi các lần thử tái tạo và debug ban đầu cần hỗ trợ thêm
**Khi nào Hợp tác**: Sau khi thử tái tạo, nếu lỗi chứng minh phức tạp và cần chẩn đoán môi trường trực tiếp hoặc hành động ngoài môi trường IDE của bạn
**Hành động Người dùng Có sẵn**: Yêu cầu đầu ra lệnh terminal, log lỗi, nội dung file, lệnh chẩn đoán, và kiểm tra môi trường
**Giải quyết Vấn đề Tương tác**: Hướng dẫn Người dùng qua quy trình debug từng bước, phân tích kết quả, và lặp lại cho đến khi giải quyết

## Ngữ cảnh Lỗi
[Mô tả code/hệ thống được cho là làm gì, lỗi xảy ra ở đâu, và thực thi nhiệm vụ nào bị chặn]

## Các bước Tái tạo
1. [Hướng dẫn từng bước để tái tạo lỗi]
2. [Bao gồm đầu vào cụ thể, điều kiện, hoặc trigger]
3. [Ghi chú bất kỳ dependency môi trường hoặc yêu cầu thiết lập nào]

## Hành vi Hiện tại vs Mong đợi
- **Hiện tại**: [Những gì thực sự xảy ra - bao gồm thông báo lỗi CHÍNH XÁC, stack trace, hoặc triệu chứng thất bại]
- **Mong đợi**: [Những gì nên xảy ra thay thế để nhiệm vụ có thể tiếp tục thành công]

## Các lần Thử Debug Thất bại
[Ghi lại các lần thử debug đã được thực hiện bởi Implementation Agent:]
- [Các lần thử giải pháp cụ thể và kết quả của chúng]
- [Mẫu lỗi quan sát được trong quá trình debug]
- [Insight thu được về nguyên nhân gốc tiềm năng]

## Ngữ cảnh Môi trường
[Ngôn ngữ lập trình, phiên bản framework, hệ điều hành, dependency, thay đổi gần đây, và bất kỳ yếu tố cụ thể môi trường nào]

## Ngữ cảnh Code/File
[Cung cấp đoạn code liên quan, đường dẫn file, file cấu hình, hoặc thành phần hệ thống liên quan đến lỗi]

## Phát hiện Ủy thác Trước đó
[Chỉ bao gồm nếu delegation_attempt > 1]
[Tóm tắt các lần thử debug trước: những gì đã thử, những gì đã phát hiện, tại sao lỗi vẫn chưa giải quyết]

## Ghi chú Thực thi Ủy thác
**Tuân theo quy trình prompt khởi tạo của bạn chính xác**: Hoàn thành Bước 1 (đánh giá/xác nhận phạm vi), Bước 2 (debug thực tế + giải pháp + yêu cầu xác nhận), và Bước 3 (giao giải pháp cuối cùng) như các response riêng biệt.
```

### Xác nhận Giao hàng
Sau khi trình bày prompt ủy thác trong chat, giải thích quy trình ad-hoc cho Người dùng:
1. Sao chép khối mã markdown hoàn chỉnh chứa prompt ủy thác
2. Mở phiên chat Ad-Hoc agent mới & khởi tạo với .claude/commands/apm-4-initiate-adhoc.md
3. Dán prompt ủy thác để bắt đầu công việc ad-hoc
4. Trả về với phát hiện để tích hợp

---

## 3  Giao thức Tích hợp & Tái Ủy thác
Khi Người dùng trả về với phát hiện của Ad-Hoc Agent, tuân theo các bước sau:

### Tích hợp Giải pháp
- **Áp dụng Giải pháp Hoạt động**: Triển khai bản sửa được cung cấp và xác minh giải quyết lỗi trong ngữ cảnh nhiệm vụ
- **Tiếp tục Thực thi Nhiệm vụ**: Tiếp tục nhiệm vụ từ điểm mà lỗi đã chặn tiến độ
- **Ghi lại Giải quyết**: Ghi lại quy trình debug và giải pháp trong **Memory Log** (Nhật ký Bộ nhớ) nhiệm vụ

### Khung Quyết định Tái Ủy thác
**Lỗi Đã Giải quyết**: Đóng phiên ủy thác, tiếp tục hoàn thành nhiệm vụ sử dụng giải pháp được cung cấp
**Lỗi Giải quyết Một phần**: Nếu bản sửa chưa hoàn chỉnh, tinh chỉnh prompt với phát hiện mới và tái ủy thác:
- **Kết hợp Tiến bộ Debug**: Cập nhật "Phát hiện Ủy thác Trước đó" với các khám phá cụ thể và giải pháp một phần
- **Tinh chỉnh Ngữ cảnh Vấn đề**: Thêm chi tiết được phát hiện trong các lần thử debug
- **Tăng Bộ đếm**: Cập nhật trường `delegation_attempt` trong YAML

**Lỗi Không thể Giải quyết**: Nếu ủy thác trả về phát hiện escalation, dừng thực thi nhiệm vụ và escalate lên Manager Agent

### Tiêu chí Đóng Phiên
- **Thành công**: Lỗi được giải quyết với giải pháp hoạt động, thực thi nhiệm vụ có thể tiếp tục
- **Giới hạn Tài nguyên**: Sau 3-4 lần thử ủy thác mà không có giải quyết
- **Escalation**: Ad-Hoc agent xác định lỗi không thể giải quyết và cung cấp tài liệu escalation

### Giao thức Escalation
Khi Ad-Hoc Debug agent trả về phát hiện cho thấy lỗi không thể giải quyết:
- **Dừng thực thi nhiệm vụ ngay lập tức**
- **Bảo toàn ngữ cảnh debug** cho các lần thử giải quyết tiềm năng trong tương lai
- **Ghi log blocker kỹ thuật và ngữ cảnh** trong Memory Log với tham chiếu phiên ủy thác và phân tích nguyên nhân gốc
- **Người dùng báo cáo cho Manager Agent** để tái phân công nhiệm vụ, sửa đổi kế hoạch, hoặc escalation kỹ thuật

### Yêu cầu Ghi Log Memory
Ghi lại trong Memory Log nhiệm vụ:
- **Mô tả Lỗi**: Vấn đề gốc đã chặn thực thi nhiệm vụ
- **Tóm tắt Phiên Debug**: Số lần thử, cách tiếp cận hợp tác, và phát hiện kỹ thuật
- **Giải pháp Áp dụng**: Bản sửa hoạt động được cung cấp và cách nó cho phép tiếp tục nhiệm vụ
- **Trạng thái Phiên**: Đã giải quyết với giải pháp HOẶC escalated với chi tiết kỹ thuật

---

## 4 Quy tắc Ngôn ngữ – BẮT BUỘC

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
- **Debug Delegation** (Ủy thác Debug – giao nhiệm vụ gỡ lỗi phức tạp)
- **Bug Context** (Ngữ cảnh Lỗi – mô tả vấn đề và môi trường)
- **Escalation Protocol** (Quy trình Leo thang – báo cáo lỗi không giải quyết được)

---

**Kết thúc Hướng dẫn**