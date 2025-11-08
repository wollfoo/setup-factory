#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Maximum Triggers Generator cho Factory.ai Custom Droids
Tự động áp dụng maximum triggers configuration cho các droids

Usage:
    python apply-maximum-triggers.py --droid <droid-name>          # Apply cho 1 droid
    python apply-maximum-triggers.py --all                         # Apply cho tất cả droids
    python apply-maximum-triggers.py --preview <droid-name>        # Preview changes
"""

import os
import re
import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Any

# ============================================================================
# CONFIGURATION
# ============================================================================

DROIDS_DIR = Path(__file__).parent.parent.parent / "droids"
TEMPLATE_FILE = Path(__file__).parent.parent / "triggers-templates" / "maximum-triggers-template.yaml"

# Domain-specific trigger mappings
DOMAIN_TRIGGERS = {
    "frontend": {
        "keywords": [
            "frontend", "ui", "ux", "component", "components", "react", "vue", "angular",
            "svelte", "css", "html", "javascript", "typescript", "jsx", "tsx",
            "responsive", "mobile", "desktop", "layout", "design", "theme",
            "style", "styling", "animation", "interaction", "accessibility", "a11y"
        ],
        "file_patterns": [
            "**/components/**/*", "**/src/components/**/*",
            "**/pages/**/*", "**/views/**/*",
            "*.jsx", "*.tsx", "*.vue", "*.svelte",
            "*.css", "*.scss", "*.sass", "*.less",
            "**/styles/**/*", "**/assets/**/*"
        ],
        "domains": [
            "frontend", "ui", "ux", "web", "react", "vue", "angular",
            "css", "javascript", "typescript", "design"
        ]
    },
    
    "backend": {
        "keywords": [
            "api", "endpoint", "backend", "server", "service", "route", "controller",
            "middleware", "database", "db", "rest", "graphql", "authentication",
            "authorization", "jwt", "oauth", "session", "crud", "orm"
        ],
        "file_patterns": [
            "**/api/**/*", "**/routes/**/*", "**/controllers/**/*",
            "**/services/**/*", "**/handlers/**/*", "**/middleware/**/*",
            "*.route.*", "*.controller.*", "*.service.*", "*.api.*"
        ],
        "domains": [
            "backend", "api", "server", "rest", "graphql", "database",
            "authentication", "microservices"
        ]
    },
    
    "devops": {
        "keywords": [
            "deploy", "deployment", "ci", "cd", "pipeline", "docker", "kubernetes",
            "k8s", "container", "infrastructure", "cloud", "aws", "azure", "gcp",
            "terraform", "ansible", "jenkins", "github-actions", "gitlab-ci"
        ],
        "file_patterns": [
            "**/docker/**/*", "Dockerfile*", "docker-compose*",
            "*.yaml", "*.yml", "**/k8s/**/*", "**/infrastructure/**/*",
            ".github/workflows/*", ".gitlab-ci.yml"
        ],
        "domains": [
            "devops", "deployment", "infrastructure", "cloud", "ci-cd",
            "docker", "kubernetes", "automation"
        ]
    },
    
    "testing": {
        "keywords": [
            "test", "testing", "unit-test", "integration-test", "e2e", "spec",
            "jest", "mocha", "pytest", "vitest", "cypress", "playwright",
            "mock", "stub", "assertion", "coverage"
        ],
        "file_patterns": [
            "**/*.test.*", "**/*.spec.*", "**/tests/**/*", "**/test/**/*",
            "**/__tests__/**/*", "**/e2e/**/*"
        ],
        "domains": [
            "testing", "quality-assurance", "test-automation", "e2e-testing"
        ]
    },
    
    "security": {
        "keywords": [
            "security", "vulnerability", "audit", "pentest", "owasp",
            "authentication", "authorization", "encryption", "xss", "csrf",
            "sql-injection", "sanitization", "validation", "secure"
        ],
        "file_patterns": [
            "**/security/**/*", "**/auth/**/*", "**/middleware/**/*"
        ],
        "domains": [
            "security", "cybersecurity", "authentication", "authorization"
        ]
    },
    
    "database": {
        "keywords": [
            "database", "db", "sql", "nosql", "postgres", "mysql", "mongodb",
            "redis", "orm", "migration", "schema", "query", "index", "transaction"
        ],
        "file_patterns": [
            "**/models/**/*", "**/schemas/**/*", "**/migrations/**/*",
            "**/db/**/*", "**/database/**/*"
        ],
        "domains": [
            "database", "data", "sql", "nosql", "orm"
        ]
    },
    
    "documentation": {
        "keywords": [
            "documentation", "docs", "readme", "guide", "tutorial",
            "api-docs", "swagger", "openapi", "markdown", "docstring"
        ],
        "file_patterns": [
            "**/*.md", "**/docs/**/*", "**/documentation/**/*",
            "README*", "CHANGELOG*", "**/swagger.*", "**/openapi.*"
        ],
        "domains": [
            "documentation", "technical-writing", "api-documentation"
        ]
    }
}

# Common action verbs cho task patterns (English)
ACTION_VERBS = [
    "create", "build", "implement", "develop", "add", "make", "write", "generate",
    "update", "modify", "change", "refactor", "improve", "optimize", "enhance",
    "fix", "debug", "solve", "resolve", "repair", "patch",
    "deploy", "test", "document", "integrate", "connect"
]

# Vietnamese action verbs (động từ tiếng Việt)
VIETNAMESE_VERBS = [
    # Create
    "tạo", "tạo mới", "thêm", "xây dựng", "làm", "viết",
    # Implement
    "triển khai", "cài đặt", "thiết lập", "cấu hình",
    # Update
    "cập nhật", "sửa đổi", "chỉnh sửa", "thay đổi", "đổi",
    # Fix
    "sửa", "sửa lỗi", "chữa", "khắc phục",
    # Optimize
    "tối ưu", "tối ưu hóa", "cải thiện", "nâng cao",
    # Delete
    "xóa", "xóa bỏ", "loại bỏ", "gỡ",
    # Test
    "kiểm tra", "thử", "chạy thử",
    # Analyze
    "phân tích", "analyze", "analysis", "đánh giá", "xem xét", "nghiên cứu",
    # Question words
    "làm sao", "làm thế nào", "cách", "ở đâu"
]

# Combined verbs for generation
ALL_VERBS = ACTION_VERBS + VIETNAMESE_VERBS

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def detect_droid_domain(droid_name: str, description: str) -> str:
    """Detect domain của droid từ name và description"""
    name_lower = droid_name.lower()
    desc_lower = description.lower() if description else ""
    
    # Check exact matches
    for domain in DOMAIN_TRIGGERS.keys():
        if domain in name_lower or domain in desc_lower:
            return domain
    
    # Fallback heuristics
    if any(x in name_lower for x in ["api", "server", "route", "controller"]):
        return "backend"
    if any(x in name_lower for x in ["ui", "component", "react", "vue"]):
        return "frontend"
    if any(x in name_lower for x in ["deploy", "infra", "docker", "k8s"]):
        return "devops"
    if any(x in name_lower for x in ["test", "spec", "e2e"]):
        return "testing"
    if any(x in name_lower for x in ["security", "auth", "audit"]):
        return "security"
    if any(x in name_lower for x in ["database", "db", "sql", "orm"]):
        return "database"
    if any(x in name_lower for x in ["doc", "readme", "guide"]):
        return "documentation"
    
    return "backend"  # Default fallback

def generate_task_patterns(domain: str, keywords: List[str]) -> List[str]:
    """Generate comprehensive task patterns"""
    patterns = []
    
    # Ultra-broad wildcards
    for kw in keywords[:10]:  # Top 10 keywords
        patterns.extend([
            f"* {kw} *",
            f"{kw} * *",
            f"* * {kw}"
        ])
    
    # Action verb patterns
    for verb in ACTION_VERBS[:15]:  # Top 15 verbs
        patterns.extend([
            f"{verb} *",
            f"{verb} * {keywords[0]}",
            f"{verb} {keywords[0]} *"
        ])
    
    # Multi-word patterns
    for kw in keywords[:5]:
        patterns.extend([
            f"create * for {kw}",
            f"implement * using {kw}",
            f"add * to {kw}",
            f"build * with {kw}"
        ])
    
    # Question patterns
    for kw in keywords[:5]:
        patterns.extend([
            f"how to * {kw}",
            f"where is * {kw}",
            f"find * {kw}"
        ])
    
    return list(set(patterns))  # Remove duplicates

def generate_maximum_triggers(droid_name: str, current_metadata: Dict[str, Any]) -> Dict[str, Any]:
    """Generate maximum triggers configuration cho droid"""
    
    # Detect domain
    description = current_metadata.get("metadata", {}).get("description", "")
    domain = detect_droid_domain(droid_name, description)
    
    print(f"  → Detected domain: {domain}")
    
    # Get base triggers cho domain
    base_triggers = DOMAIN_TRIGGERS.get(domain, DOMAIN_TRIGGERS["backend"])
    
    # Expand keywords with both English and Vietnamese
    keywords = base_triggers["keywords"].copy()
    keywords.extend(ACTION_VERBS)
    keywords.extend(VIETNAMESE_VERBS)  # Add Vietnamese verbs
    keywords = list(set(keywords))  # Remove duplicates
    
    # Expand file patterns
    file_patterns = base_triggers["file_patterns"].copy()
    
    # Generate task patterns
    task_patterns = generate_task_patterns(domain, base_triggers["keywords"])
    
    # Expand domains
    domains = base_triggers["domains"].copy()
    domains.append("software-development")
    domains.append("engineering")
    
    # Build triggers dict
    triggers = {
        "keywords": sorted(keywords),
        "file_patterns": sorted(file_patterns),
        "task_patterns": sorted(task_patterns),
        "domains": sorted(domains)
    }
    
    return triggers

def parse_droid_file(file_path: Path) -> Dict[str, Any]:
    """Parse droid markdown file và extract YAML frontmatter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid droid file format: {file_path}")
    
    yaml_content = match.group(1)
    markdown_content = match.group(2)
    
    # Parse YAML
    metadata = yaml.safe_load(yaml_content)
    
    return {
        "metadata": metadata,
        "markdown": markdown_content,
        "raw_yaml": yaml_content
    }

def update_droid_triggers(file_path: Path, new_triggers: Dict[str, Any], preview: bool = False) -> bool:
    """Update triggers trong droid file"""
    
    # Parse current file
    droid_data = parse_droid_file(file_path)
    metadata = droid_data["metadata"]
    
    # Update triggers
    metadata["triggers"] = new_triggers
    
    # Ensure autonomous flag
    if "metadata" not in metadata:
        metadata["metadata"] = {}
    metadata["metadata"]["autonomous"] = True
    
    # Convert back to YAML
    new_yaml = yaml.dump(metadata, sort_keys=False, allow_unicode=True, default_flow_style=False)
    
    # Reconstruct file
    new_content = f"---\n{new_yaml}---\n{droid_data['markdown']}"
    
    if preview:
        print("\n" + "="*80)
        print(f"PREVIEW: {file_path.name}")
        print("="*80)
        print(new_content[:1000])  # First 1000 chars
        print("...\n")
        return True
    
    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

# ============================================================================
# MAIN FUNCTIONS
# ============================================================================

def apply_to_droid(droid_name: str, preview: bool = False) -> bool:
    """Apply maximum triggers to một droid"""
    
    droid_file = DROIDS_DIR / f"{droid_name}.md"
    
    if not droid_file.exists():
        print(f"❌ Droid not found: {droid_name}")
        return False
    
    print(f"\n{'[PREVIEW]' if preview else '[APPLYING]'} {droid_name}.md")
    
    try:
        # Parse current droid
        droid_data = parse_droid_file(droid_file)
        
        # Generate maximum triggers
        new_triggers = generate_maximum_triggers(droid_name, droid_data["metadata"])
        
        print(f"  → Generated {len(new_triggers['keywords'])} keywords")
        print(f"  → Generated {len(new_triggers['file_patterns'])} file patterns")
        print(f"  → Generated {len(new_triggers['task_patterns'])} task patterns")
        print(f"  → Generated {len(new_triggers['domains'])} domains")
        
        # Update file
        success = update_droid_triggers(droid_file, new_triggers, preview=preview)
        
        if success and not preview:
            print(f"  ✅ Updated successfully")
        
        return success
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def apply_to_all_droids(preview: bool = False) -> Dict[str, bool]:
    """Apply maximum triggers to tất cả droids"""
    
    results = {}
    droid_files = sorted(DROIDS_DIR.glob("*.md"))
    
    print(f"\nFound {len(droid_files)} droids")
    print("="*80)
    
    for droid_file in droid_files:
        droid_name = droid_file.stem
        success = apply_to_droid(droid_name, preview=preview)
        results[droid_name] = success
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    successful = sum(1 for v in results.values() if v)
    failed = len(results) - successful
    
    print(f"Total: {len(results)} droids")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    
    if failed > 0:
        print("\nFailed droids:")
        for name, success in results.items():
            if not success:
                print(f"  - {name}")
    
    return results

# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Apply maximum triggers configuration to Factory.ai droids"
    )
    
    parser.add_argument(
        "--droid",
        type=str,
        help="Apply to specific droid (e.g., backend-developer)"
    )
    
    parser.add_argument(
        "--all",
        action="store_true",
        help="Apply to all droids"
    )
    
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview changes without applying"
    )
    
    args = parser.parse_args()
    
    # Validation
    if not args.droid and not args.all:
        parser.error("Either --droid or --all must be specified")
    
    if args.droid and args.all:
        parser.error("Cannot specify both --droid and --all")
    
    # Execute
    print("="*80)
    print("Factory.ai Maximum Triggers Generator")
    print("="*80)
    
    if args.droid:
        apply_to_droid(args.droid, preview=args.preview)
    elif args.all:
        apply_to_all_droids(preview=args.preview)

if __name__ == "__main__":
    main()
