#!/usr/bin/env python3
"""
Convert Droids Script (Chuyển đổi các file Droids về cấu trúc Factory CLI chuẩn)

Chuyển đổi các file subagents từ cấu trúc cũ sang cấu trúc Factory CLI chính thức:
- Loại bỏ các trường không cần thiết: category, color, type, tags, metadata, triggers
- Đưa description lên top-level (từ metadata.description)
- Đảm bảo có trường tools với danh sách công cụ hợp lệ
- Giữ nguyên hoặc tạo system prompt trong markdown body
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, Any, List

# Tool categories mapping theo Factory CLI spec
TOOL_CATEGORIES = {
    'read-only': ['Read', 'LS', 'Grep', 'Glob'],
    'edit': ['Create', 'Edit', 'MultiEdit', 'ApplyPatch'],
    'execute': ['Execute', 'Bash'],
    'web': ['WebSearch', 'FetchUrl', 'WebFetch'],
    'task': ['Task'],
    'write': ['Write', 'NotebookEdit']
}

# Default tools for different droid types
DEFAULT_TOOLS_BY_TYPE = {
    'review': ['Read', 'LS', 'Grep', 'Glob'],
    'orchestration': ['Read', 'LS', 'Grep', 'Task', 'TodoWrite'],
    'design': ['Read', 'LS', 'Grep', 'Glob', 'Write'],
    'default': ['Read', 'LS', 'Grep', 'Glob', 'Edit', 'Write']
}


def parse_droid_file(filepath: Path) -> tuple[Dict[str, Any], str]:
    """Parse droid file - tách YAML frontmatter và markdown body"""
    content = filepath.read_text(encoding='utf-8')
    
    # Extract YAML frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid droid file format: {filepath}")
    
    yaml_content = match.group(1)
    markdown_body = match.group(2).strip()
    
    # Parse YAML
    try:
        frontmatter = yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        raise ValueError(f"YAML parsing error in {filepath}: {e}")
    
    return frontmatter, markdown_body


def extract_description(frontmatter: Dict[str, Any]) -> str:
    """Trích xuất description từ metadata hoặc top-level"""
    # Ưu tiên metadata.description
    if 'metadata' in frontmatter and 'description' in frontmatter['metadata']:
        desc = frontmatter['metadata']['description']
    elif 'description' in frontmatter:
        desc = frontmatter['description']
    else:
        # Fallback: dùng name
        desc = f"Specialized agent for {frontmatter.get('name', 'unknown')} tasks"
    
    # Clean up description - loại bỏ markdown và chỉ lấy phần đầu
    if isinstance(desc, str):
        # Remove excessive whitespace and newlines
        desc = ' '.join(desc.split())
        # Truncate if too long (>300 chars)
        if len(desc) > 300:
            # Lấy câu đầu tiên hoặc 200 ký tự đầu
            sentences = desc.split('. ')
            if len(sentences[0]) < 200:
                desc = sentences[0] + '.'
            else:
                desc = desc[:200] + '...'
    
    return desc


def extract_tools(frontmatter: Dict[str, Any]) -> List[str]:
    """Trích xuất hoặc tạo danh sách tools"""
    if 'tools' in frontmatter:
        tools = frontmatter['tools']
        # Normalize tool names
        if isinstance(tools, list):
            return [str(t).strip() for t in tools if t]
    
    # Determine default tools based on type
    droid_type = frontmatter.get('type', 'default')
    return DEFAULT_TOOLS_BY_TYPE.get(droid_type, DEFAULT_TOOLS_BY_TYPE['default'])


def extract_model(frontmatter: Dict[str, Any]) -> str:
    """Trích xuất model - ưu tiên 'inherit' theo Factory best practice"""
    model = frontmatter.get('model', 'inherit')
    # Convert specific models to inherit for flexibility
    if model in ['sonnet', 'claude-3-5-sonnet', 'gpt-4']:
        return 'inherit'
    return model


def generate_system_prompt(frontmatter: Dict[str, Any], markdown_body: str) -> str:
    """Tạo hoặc giữ nguyên system prompt"""
    if markdown_body and len(markdown_body) > 50:
        # Đã có system prompt
        return markdown_body
    
    # Tạo system prompt từ metadata
    name = frontmatter.get('name', 'agent')
    desc = extract_description(frontmatter)
    specialization = frontmatter.get('metadata', {}).get('specialization', '')
    
    prompt = f"""You are a specialized {name.replace('-', ' ')} agent.

{desc}

Your responsibilities:
- Analyze the task or context provided by the parent agent
- Apply your specialized expertise to deliver high-quality results
- Provide clear, actionable recommendations
- Structure your response with clear sections (Summary, Findings, Recommendations)
"""
    
    if specialization:
        prompt += f"\nSpecialization focus: {specialization}\n"
    
    prompt += """
Respond in a structured format:
- **Summary**: One-line overview of your analysis
- **Findings**: Key observations or issues identified
- **Recommendations**: Actionable next steps
"""
    
    return prompt.strip()


def convert_to_factory_format(filepath: Path, backup: bool = True) -> bool:
    """Chuyển đổi file droid sang Factory CLI format"""
    try:
        print(f"Converting: {filepath.name}")
        
        # Backup original file
        if backup:
            backup_path = filepath.with_suffix('.md.bak')
            if not backup_path.exists():
                filepath.rename(backup_path)
                filepath = backup_path.with_suffix('.md')
            else:
                # Nếu backup đã tồn tại, đọc từ file gốc
                pass
        
        # Parse file
        frontmatter, markdown_body = parse_droid_file(filepath if not backup else backup_path)
        
        # Extract required fields
        name = frontmatter.get('name', filepath.stem)
        description = extract_description(frontmatter)
        model = extract_model(frontmatter)
        tools = extract_tools(frontmatter)
        
        # Generate system prompt
        system_prompt = generate_system_prompt(frontmatter, markdown_body)
        
        # Create new YAML frontmatter
        new_frontmatter = {
            'name': name,
            'description': description,
            'model': model,
            'tools': tools
        }
        
        # Write new file
        new_content = "---\n"
        new_content += yaml.dump(new_frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content += "---\n\n"
        new_content += system_prompt
        
        # Write to file
        filepath.write_text(new_content, encoding='utf-8')
        
        print(f"  ✅ Converted: {name}")
        return True
        
    except Exception as e:
        print(f"  ❌ Error converting {filepath.name}: {e}")
        return False


def main():
    """Main conversion function"""
    droids_dir = Path(__file__).parent / 'droids'
    
    if not droids_dir.exists():
        print(f"❌ Droids directory not found: {droids_dir}")
        return
    
    print(f"🔍 Scanning droids directory: {droids_dir}")
    print("=" * 60)
    
    # Get all .md files
    md_files = list(droids_dir.glob('*.md'))
    print(f"Found {len(md_files)} droid files\n")
    
    # Convert each file
    success_count = 0
    failed_count = 0
    
    for md_file in sorted(md_files):
        if convert_to_factory_format(md_file, backup=True):
            success_count += 1
        else:
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"✅ Successfully converted: {success_count} files")
    print(f"❌ Failed: {failed_count} files")
    print(f"📦 Backup files created with .md.bak extension")
    print("\nConversion complete!")


if __name__ == '__main__':
    main()
