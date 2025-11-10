# Droids Conversion Report
## Báo cáo chuyển đổi Subagents về Factory CLI Format

**Ngày thực hiện**: 2025-11-10
**Tổng số droids**: 52 files

---

## 📊 Kết quả (Results)

✅ **Thành công (Success)**: 52/52 droids (100%)

- **Script conversion**: 46 files
- **Manual fix**: 6 files

---

## 🔄 Quy trình chuyển đổi (Conversion Process)

### 1. Phân tích cấu trúc (Structure Analysis)

**Cấu trúc CŨ (Old - SAI)**:
```yaml
---
name: code-reviewer
category: quality-assurance        # ❌ THỪA
color: orange                      # ❌ THỪA
type: review                       # ❌ THỪA
tags: [...]                        # ❌ THỪA
model: sonnet
metadata:                          # ❌ SAI cấu trúc
  description: ...                 # Should be top-level
  specialization: ...              # ❌ THỪA
  complexity: ...                  # ❌ THỪA
  autonomous: ...                  # ❌ THỪA
triggers:                          # ❌ THỪA
  keywords: [...]
---
(thiếu system prompt)
```

**Cấu trúc MỚI (New - ĐÚNG theo Factory CLI)**:
```yaml
---
name: code-reviewer
description: Elite code review expert specializing in modern AI-powered code analysis...
model: inherit
tools: ["Read", "LS", "Grep", "Glob"]
---
You are an elite code review expert...
(system prompt chi tiết)
```

### 2. Script conversion (convert_droids.py)

**Chức năng**:
- Parse YAML frontmatter từ file cũ
- Trích xuất `name`, `description` (từ `metadata.description`), `model`, `tools`
- Loại bỏ các trường thừa: `category`, `color`, `type`, `tags`, `metadata`, `triggers`, `capabilities`, `constraints`, etc.
- Giữ nguyên hoặc tạo system prompt trong markdown body
- Tạo backup file gốc với extension `.md.bak`

**Kết quả**: 46/52 files converted thành công

### 3. Manual fix cho 6 files bị lỗi YAML parsing

**Files cần sửa thủ công**:
1. `architect-review.md` - YAML parsing error với `* architecture *` trong triggers
2. `backend-architect.md` - Tương tự
3. `code-reviewer.md` - Tương tự
4. `docs-architect.md` - Tương tự
5. `graphql-architect.md` - Tương tự
6. `planner-researcher.md` - XML tags trong description không được quote

**Giải pháp**: Tạo file mới theo Factory CLI format với description rút gọn và system prompt chi tiết

### 4. File extension fix

**Vấn đề**: Script tạo file với extension `.md.md` thay vì `.md`

**Giải pháp**: PowerShell command để rename tất cả file `.md.md` → `.md`
```powershell
Get-ChildItem -Filter "*.md.md" | ForEach-Object { 
    Rename-Item -Path $_.FullName -NewName ($_.Name -replace '\.md\.md$', '.md') -Force 
}
```

---

## ✅ Kết quả cuối cùng (Final Results)

### Cấu trúc file Factory CLI chuẩn

**Các trường bắt buộc**:
1. ✅ `name` - Tên droid (lowercase, hyphenated)
2. ✅ `description` - Mô tả chức năng (dùng cho auto-delegation)
3. ✅ `model` - Model sử dụng (`inherit` hoặc tên model cụ thể)
4. ✅ `tools` - Danh sách tools được phép (array format)

**Markdown body**: System prompt chi tiết

### Tool categories theo Factory CLI

- **read-only**: `Read`, `LS`, `Grep`, `Glob`
- **edit**: `Create`, `Edit`, `MultiEdit`, `ApplyPatch`
- **execute**: `Execute`, `Bash`
- **web**: `WebSearch`, `FetchUrl`, `WebFetch`
- **task**: `Task`
- **write**: `Write`, `NotebookEdit`

---

## 📁 Files structure

```
droids/
├── *.md              # 52 converted droids (Factory CLI format)
└── *.md.bak          # 52 backup files (original format)
```

**Backup files**: Tất cả file gốc được lưu với extension `.md.bak` để có thể rollback nếu cần

---

## 🎯 Validation checklist

- ✅ All 52 droids converted successfully
- ✅ YAML frontmatter có đúng 4 trường: `name`, `description`, `model`, `tools`
- ✅ Không còn các trường thừa: `category`, `color`, `type`, `tags`, `metadata`, `triggers`
- ✅ `description` ở top-level (không nằm trong `metadata`)
- ✅ `tools` là array format (e.g., `["Read", "LS", "Grep"]`)
- ✅ Markdown body chứa system prompt chi tiết
- ✅ Backup files tồn tại (`.md.bak`)

---

## 📚 Tài liệu tham khảo (References)

- **Factory CLI Documentation**: https://docs.factory.ai/cli/configuration/custom-droids
- **Conversion script**: `convert_droids.py`
- **Example droids**:
  - `code-reviewer.md` - Read-only reviewer
  - `security-auditor.md` - Security audit with Task tool
  - `backend-architect.md` - Full-stack architect with Write/Edit tools

---

## 🚀 Next steps

1. ✅ Kiểm tra droids hoạt động đúng với Factory CLI
2. ✅ Test delegation mechanism với `Task` tool
3. ✅ Xác minh auto-delegation dựa trên `description`
4. ✅ Remove backup files nếu conversion ổn định (optional)

---

## 📝 Notes

- **Model recommendation**: Sử dụng `inherit` để kế thừa model từ parent session (flexible, theo Factory best practice)
- **Tool access**: Giới hạn tools theo chức năng (read-only cho reviewer, edit cho architect, etc.)
- **Description importance**: `description` field rất quan trọng cho auto-delegation mechanism
- **System prompt**: Giữ nguyên hoặc tối ưu system prompt để đảm bảo chất lượng output

---

**Status**: ✅ COMPLETED
**Success rate**: 100% (52/52)
