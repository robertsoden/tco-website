#!/usr/bin/env python3
"""
Fix remaining image path issues:
- image-*.jpeg files are in root assets/images/ not uploads/
- OUR-VALUES size variants
- Inaugural summer school edited vs non-edited
"""

import re
from pathlib import Path

FIXES = [
    # Ontario Climate Risk Workshop images (in root, not uploads)
    ('assets/images/uploads/image-1.jpeg', 'assets/images/image-1.jpeg'),
    ('assets/images/uploads/image-2.jpeg', 'assets/images/image-2.jpeg'),
    ('assets/images/uploads/image-3.jpeg', 'assets/images/image-3.jpeg'),
    ('assets/images/uploads/image-4.jpeg', 'assets/images/image-4.jpeg'),
    ('assets/images/uploads/image-5.jpeg', 'assets/images/image-5.jpeg'),
    ('assets/images/uploads/image-6.jpeg', 'assets/images/image-6.jpeg'),
    ('assets/images/uploads/image-7.jpeg', 'assets/images/image-7.jpeg'),

    # Summer school image (in root, not uploads, and use non-edited version)
    ('assets/images/uploads/Inaugural-Toronto-Climate-Summer-School-shows-students-that-climate-edited.png',
     'assets/images/Inaugural-Toronto-Climate-Summer-School-shows-students-that-climate.png'),

    # OUR VALUES image (use base version without size suffix)
    ('assets/images/uploads/OUR-VALUES-1-1-1024x1024.png',
     'assets/images/OUR-VALUES-1-1.png'),
]

def fix_file(filepath):
    """Fix image paths in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for old_path, new_path in FIXES:
        # Simple string replacement
        content = content.replace(old_path, new_path)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 70)
    print("FIXING REMAINING IMAGE PATHS")
    print("=" * 70)
    print()

    posts_dir = Path('_posts')
    files_updated = 0

    for filepath in sorted(posts_dir.glob('*.md')):
        if fix_file(filepath):
            print(f"✅ Updated: {filepath.name}")
            files_updated += 1

    print()
    print(f"Updated {files_updated} files")

if __name__ == '__main__':
    main()
