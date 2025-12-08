---
priority: 7
command_name: delegate-research
description: Cung cấp template để ủy thác nhiệm vụ nghiên cứu cho Ad-Hoc agent
---

# APM 0.5.3 - Hướng dẫn Ủy thác Nghiên cứu
Hướng dẫn này định nghĩa cách Implementation Agent ủy thác công việc nghiên cứu cho **Ad-Hoc Research agent** (Agent Nghiên cứu Đặc biệt). Sử dụng hướng dẫn này khi gặp lỗ hổng kiến thức về tài liệu hiện tại, API, SDK, hoặc thông số kỹ thuật cần thiết để hoàn thành nhiệm vụ.

---

## 1  Tổng quan Quy trình Ủy thác
Ad-Hoc Research agent hoạt động trong **phiên chat riêng biệt** được quản lý bởi Implementation Agent ủy thác:

### Quản lý Nhánh
- **Hoạt động Độc lập**: Ad-Hoc agent làm việc trong các phiên nhánh cô lập mà không có quyền truy cập ngữ cảnh dự án chính
- **Phối hợp Người dùng**: Người dùng mở phiên chat mới, dán prompt ủy thác, trả về với phát hiện
- **Bảo toàn Ngữ cảnh**: Phiên ủy thác vẫn mở cho khả năng tái ủy thác cho đến khi đóng chính thức

### Quy trình Bàn giao
1. **Tạo Prompt**: Sử dụng template bên dưới với ngữ cảnh nghiên cứu đầy đủ
2. **Người dùng Mở Phiên**: Người dùng khởi tạo phiên chat Ad-Hoc Research mới và dán prompt
3. **Researcher Làm việc**: Ad-Hoc agent điều tra nguồn và cung cấp thông tin/phát hiện hiện tại hợp tác với Người dùng
4. **Người dùng Trả về**: Người dùng mang phát hiện về cho Implementation Agent để tích hợp

---

## 2  Template Prompt Ủy thác
Trình bày prompt ủy thác **trong chat dưới dạng một khối mã markdown duy nhất với YAML frontmatter ở đầu** để Người dùng sao chép-dán sang phiên Ad-Hoc Research mới

```markdown
---
research_type: [documentation|api_spec|sdk_version|integration|compatibility|best_practices|other]
information_scope: [targeted|comprehensive|comparative]
knowledge_gap: [outdated|missing|conflicting]
delegation_attempt: [1|2|3|...]
---

# Ủy thác Nghiên cứu: [Chủ đề Nghiên cứu Ngắn gọn]

## Ngữ cảnh Nghiên cứu
[Mô tả thông tin cần thiết và tại sao nó cần cho việc hoàn thành nhiệm vụ]

## Cách tiếp cận Thực thi Nghiên cứu
**Mục tiêu Chính**: Thu thập thông tin hiện tại, có thẩm quyền mà Implementation Agent cần để tiến hành thực thi nhiệm vụ
**Giao hàng Thông tin Bắt buộc**: Cung cấp tài liệu đã nghiên cứu, best practices, hoặc thông số kỹ thuật cho Implementation Agent sử dụng
**Tập trung Thông tin Hiện tại**: Truy cập nguồn chính thức và tài liệu gần đây thay vì cung cấp hướng dẫn lý thuyết
**Chuyển giao Kiến thức**: Giao phát hiện có cấu trúc trực tiếp trả lời câu hỏi Implementation Agent để cho phép tiếp tục nhiệm vụ

## Yêu cầu Thực thi Nghiên cứu
**Sử dụng Công cụ Bắt buộc**: Bạn phải sử dụng công cụ tìm kiếm web và web fetch để truy cập tài liệu chính thức hiện tại và xác minh thông tin. Không chỉ dựa vào dữ liệu training hoặc kiến thức trước đó.
**Tiêu chuẩn Thông tin Hiện tại**: Tất cả phát hiện phải được lấy từ tài liệu chính thức, GitHub repository, hoặc nguồn có thẩm quyền, đáng tin cậy được truy cập trong phiên nghiên cứu này.
**Giao thức Xác minh**: Tham chiếu chéo nhiều nguồn hiện tại để đảm bảo độ chính xác và tính cập nhật của thông tin.

## Trạng thái Kiến thức Hiện tại
[Những gì Implementation Agent hiện biết/giả định vs những gì không chắc chắn hoặc có thể lỗi thời]

## Câu hỏi Nghiên cứu Cụ thể
[Liệt kê các câu hỏi có mục tiêu cần trả lời, cụ thể về những gì bạn cần biết]

## Nguồn Dự kiến
[Liệt kê các trang tài liệu cụ thể, GitHub repo chính thức, tài liệu API, hoặc tài nguyên đáng tin cậy cho Ad-Hoc agent điều tra]

## Yêu cầu Tích hợp
[Giải thích cách phát hiện nghiên cứu sẽ được áp dụng cho nhiệm vụ hiện tại]

## Phát hiện Nghiên cứu Trước đó
[Chỉ bao gồm nếu delegation_attempt > 1]
[Tóm tắt phát hiện từ các lần thử nghiên cứu Ad-Hoc trước và tại sao chúng không đủ]

## Ghi chú Thực thi Ủy thác
**Tuân theo quy trình prompt khởi tạo của bạn chính xác**: Hoàn thành Bước 1 (đánh giá/xác nhận phạm vi), Bước 2 (thực thi + phát hiện + yêu cầu xác nhận), và Bước 3 (giao markdown cuối cùng) như các response riêng biệt.
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

### Tích hợp Thông tin
- **Xác nhận Tính Cập nhật**: Đảm bảo thông tin hiện tại và từ nguồn có thẩm quyền
- **Kiểm tra Khả năng Hành động**: Xác nhận phát hiện có thể được áp dụng trực tiếp vào ngữ cảnh nhiệm vụ
- **Tài liệu**: Ghi lại quy trình ủy thác và kết quả nghiên cứu trong **Memory Log** (Nhật ký Bộ nhớ) nhiệm vụ

### Khung Quyết định Tái Ủy thác
**Thông tin Đủ**: Đóng phiên ủy thác, tiến hành hoàn thành nhiệm vụ sử dụng phát hiện nghiên cứu
**Thông tin Không đủ**: Tinh chỉnh prompt sử dụng phát hiện Ad-Hoc và tái ủy thác cho cùng instance Ad-Hoc Agent:
- **Kết hợp Insight**: Cập nhật section "Phát hiện Nghiên cứu Trước đó" với các bài học cụ thể
- **Tinh chỉnh Câu hỏi**: Thêm các truy vấn cụ thể hơn dựa trên lỗ hổng nghiên cứu ban đầu
- **Tăng Bộ đếm**: Cập nhật trường `delegation_attempt` trong YAML

### Tiêu chí Đóng Phiên
- **Thành công**: Thông tin hiện tại, có thể hành động được tìm thấy và xác nhận cho ngữ cảnh nhiệm vụ
- **Giới hạn Tài nguyên**: Sau 3-4 lần thử ủy thác mà không có thông tin đủ
- **Escalation**: Escalation chính thức lên Manager Agent với tham chiếu phiên ủy thác cho lỗ hổng kiến thức dai dẳng

### Yêu cầu Ghi Log Memory
Ghi lại trong Memory Log nhiệm vụ:
- **Lý do Nghiên cứu**: Tại sao nghiên cứu được ủy thác và thông tin gì cần thiết
- **Tóm tắt Phiên**: Số lần thử và phát hiện chính được khám phá
- **Thông tin Áp dụng**: Cách phát hiện nghiên cứu được tích hợp vào hoàn thành nhiệm vụ
- **Trạng thái Phiên**: Đóng với thông tin đủ HOẶC escalated với tham chiếu phiên

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
- **Research Delegation** (Ủy thác Nghiên cứu – giao nhiệm vụ tìm hiểu thông tin)
- **Knowledge Gap** (Lỗ hổng Kiến thức – thông tin cần được nghiên cứu)
- **Re-delegation** (Ủy thác lại – tinh chỉnh prompt và giao lại nhiệm vụ)

---

**Kết thúc Hướng dẫn**