# Factory.ai Maximum Triggers Configuration

Hệ thống tối ưu hóa auto-trigger cho Factory.ai Custom Droids

## 📁 Cấu Trúc Thư Mục

```
.factory/
├── README.md                          # File này
├── docs/
│   └── maximum-triggers-guide.md      # Hướng dẫn chi tiết
├── scripts/
│   └── apply-maximum-triggers.py      # Script automation
└── triggers-templates/
    └── maximum-triggers-template.yaml # Template mẫu
```

## 🚀 Quick Start

### Bước 1: Preview Changes

```bash
# Preview changes cho 1 droid
python .factory/scripts/apply-maximum-triggers.py --droid frontend-developer --preview

# Preview changes cho tất cả droids
python .factory/scripts/apply-maximum-triggers.py --all --preview
```

### Bước 2: Apply Configuration

```bash
# Apply cho 1 droid
python .factory/scripts/apply-maximum-triggers.py --droid frontend-developer

# Apply cho tất cả droids (66 droids)
python .factory/scripts/apply-maximum-triggers.py --all
```

### Bước 3: Configure Factory.ai Settings

```bash
# Edit settings
nano ~/.factory/settings.json

# Set recommended values:
# - enableCustomDroids: true
# - autonomyLevel: "auto-high"
# - triggerThreshold: 50
```

## 📊 What's Included

### ✅ Backend Developer (COMPLETED)

- **Keywords**: 100+ items (từ 20 items)
- **File Patterns**: 60+ items (từ 4 items)  
- **Task Patterns**: 80+ items (từ 3 items)
- **Domains**: 25+ items (từ 2 items)
- **Expected Impact**: Auto-trigger rate >85%

### 🔄 Remaining Droids (READY TO APPLY)

65 droids sẵn sàng apply với script:
- frontend-developer
- devops-engineer
- security-auditor
- database-specialist
- ... và 61 droids khác

## 🎯 Expected Results

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Keywords** | ~10 | ~100 | **10x** |
| **File Patterns** | ~5 | ~50 | **10x** |
| **Task Patterns** | ~5 | ~80 | **16x** |
| **Auto-Trigger Rate** | ~30% | **>85%** | **3x** |

## 📚 Documentation

- **Full Guide**: `.factory/docs/maximum-triggers-guide.md`
- **Template**: `.factory/triggers-templates/maximum-triggers-template.yaml`
- **Factory.ai Docs**: https://docs.factory.ai/cli/configuration/custom-droids

## 🛠️ Requirements

```bash
# Python 3.7+
python --version

# Install PyYAML
pip install pyyaml
```

## 💡 Usage Examples

### Example 1: Apply to Frontend Developer

```bash
python .factory/scripts/apply-maximum-triggers.py --droid frontend-developer
```

**Output**:
```
================================================================================
Factory.ai Maximum Triggers Generator
================================================================================

[APPLYING] frontend-developer.md
  → Detected domain: frontend
  → Generated 95 keywords
  → Generated 48 file patterns
  → Generated 156 task patterns
  → Generated 12 domains
  ✅ Updated successfully
```

### Example 2: Batch Apply to All

```bash
python .factory/scripts/apply-maximum-triggers.py --all
```

**Output**:
```
Found 66 droids
================================================================================
[APPLYING] backend-developer.md
  → Detected domain: backend
  ✅ Updated successfully

[APPLYING] frontend-developer.md
  → Detected domain: frontend
  ✅ Updated successfully

... (64 more)

================================================================================
SUMMARY
================================================================================
Total: 66 droids
✅ Successful: 66
❌ Failed: 0
```

## 🔍 Verification

### Check YAML Syntax

```bash
# Install yamllint
pip install yamllint

# Validate all droids
yamllint droids/*.md
```

### Count Triggers

```bash
# Count keywords in backend-developer
grep -c '^\s*-\s*"' droids/backend-developer.md

# Count all triggers
grep -c '^\s*-' droids/backend-developer.md
```

## 🚨 Safety Notes

1. **Backup First** - Script modifies files in-place
2. **Preview Mode** - Always use `--preview` first
3. **Git Commit** - Commit changes incrementally
4. **Test One** - Test with 1 droid before `--all`
5. **Validate YAML** - Run yamllint after changes

## 📈 Monitoring

### Track Auto-Trigger Rate

```bash
# Factory.ai CLI (future feature)
factory stats --metric=auto-triggers --period=7d
```

### Manual Tracking

```bash
# Create tracking log
echo "Date,Droid,Task,Triggered,Score" > trigger-log.csv

# Log each interaction
echo "2025-01-08,backend-developer,create api,true,72" >> trigger-log.csv
```

## 🎓 Best Practices

1. **Start Small** - Apply to 1-2 droids first
2. **Monitor Metrics** - Track auto-trigger rate
3. **Iterate** - Adjust based on false positives/negatives
4. **Document** - Note what works for your workflow
5. **Share** - Commit working configs to Git

## 🤝 Contributing

### Add New Domain Templates

Edit `.factory/scripts/apply-maximum-triggers.py`:

```python
DOMAIN_TRIGGERS = {
    # ... existing domains
    
    "your-domain": {
        "keywords": [...],
        "file_patterns": [...],
        "domains": [...]
    }
}
```

### Improve Detection Logic

Update `detect_droid_domain()` function with better heuristics.

## 📞 Support

- **Factory.ai Discord**: https://discord.gg/zuudFXxg69
- **GitHub Issues**: https://github.com/factory-ai/factory
- **Documentation**: https://docs.factory.ai/

## 📄 License

MIT License - Use freely for your Factory.ai droids!

---

**Created**: 2025-01-08  
**Status**: ✅ Production Ready  
**Version**: 1.0.0
