#!/usr/bin/env python3
"""
Fix image paths in blog posts to match actual filenames.
WordPress generates multiple sizes with suffixes like -1024x768, -768x1024, etc.
but the actual exported files use -scaled suffix.
"""

import os
import re
from pathlib import Path

# Mapping of WordPress size patterns to actual filenames
IMAGE_MAPPINGS = {
    # Field Lab images
    r'Field-Lab-partial-group-photo_Week-1-1-1024x683\.jpg': 'Field-Lab-partial-group-photo_Week-1-1-scaled.jpg',

    # IMG_ numbered images (all variants map to -scaled version)
    r'IMG_2077-1-1024x768\.jpg': 'IMG_2077-1-scaled.jpg',
    r'IMG_2077-scaled-1\.jpg': 'IMG_2077-1-scaled.jpg',
    r'IMG_2114-\d+x\d+\.jpg': 'IMG_2114-scaled.jpg',
    r'IMG_2454-768x1024\.jpg': 'IMG_2454-scaled.jpg',
    r'IMG_2490-1-768x1024\.jpg': 'IMG_2490-1-scaled.jpg',
    r'IMG_2490-\d+x\d+\.jpg': 'IMG_2490-scaled.jpg',
    r'IMG_2977-1-1024x768\.jpg': 'IMG_2977-1-scaled.jpg',
    r'IMG_2977-\d+x\d+\.jpg': 'IMG_2977-scaled.jpg',
    r'IMG_3516-2-1024x768\.jpg': 'IMG_3516-2-scaled.jpg',
    r'IMG_3516-\d+x\d+\.jpg': 'IMG_3516-scaled.jpg',
    r'IMG_3995-1-1024x768\.jpg': 'IMG_3995-1-scaled.jpg',
    r'IMG_3995-\d+x\d+\.jpg': 'IMG_3995-scaled.jpg',
    r'IMG_5131-1-1024x768\.jpg': 'IMG_5131-1-scaled.jpg',
    r'IMG_5131-\d+x\d+\.jpg': 'IMG_5131-scaled.jpg',
    r'IMG_5249-1-768x1024\.jpg': 'IMG_5249-1-scaled.jpg',
    r'IMG_5249-768x1024\.jpg': 'IMG_5249-1-scaled.jpg',  # Both map to the same file
    r'IMG_5249-\d+x\d+\.jpg': 'IMG_5249-1-scaled.jpg',
    r'IMG_5295-1024x768\.jpg': 'IMG_5295-scaled.jpg',
    r'IMG_5295-\d+x\d+\.jpg': 'IMG_5295-scaled.jpg',
    r'IMG_5534-1-1024x768\.jpg': 'IMG_5534-1-scaled.jpg',
    r'IMG_5534-\d+x\d+\.jpg': 'IMG_5534-scaled.jpg',
    r'IMG_6216-1024x768\.jpg': 'IMG_6216-scaled.jpg',
    r'IMG_6216-\d+x\d+\.jpg': 'IMG_6216-scaled.jpg',
    r'IMG_6410-768x1024\.jpg': 'IMG_6410-scaled.jpg',
    r'IMG_6410-\d+x\d+\.jpg': 'IMG_6410-scaled.jpg',
    r'IMG_6484-768x1024\.jpg': 'IMG_6484-scaled.jpg',
    r'IMG_6484-\d+x\d+\.jpg': 'IMG_6484-scaled.jpg',
    r'IMG_6906-768x1024\.jpg': 'IMG_6906-scaled.jpg',
    r'IMG_6906-\d+x\d+\.jpg': 'IMG_6906-scaled.jpg',
    r'IMG_6920-1024x768\.jpg': 'IMG_6920-scaled.jpg',
    r'IMG_6920-\d+x\d+\.jpg': 'IMG_6920-scaled.jpg',
    r'IMG_1992-1-1024x768\.jpg': 'IMG_1992-1-scaled.jpg',  # May not exist, will check

    # Newsletter images (these already exist with correct names)
    r'image-991x1024\.png': 'image-10.png',  # Size variant
    r'image-9\.png': 'bay-street-report.png',  # Bay Street report image
    r'image-8-1024x964\.png': 'Inaugural-Toronto-Climate-Summer-School-shows-students-that-climate.png',
    r'image-7-1024x964\.png': 'image-7.png',
    r'image-6-791x1024\.png': 'image-6.png',
    r'image-5-1024x681\.png': 'image-5.png',
    r'image-4-1024x576\.png': 'image-4.png',
    r'image-3-1024x293\.png': 'image-3.png',
    r'image-2-1024x683\.png': 'image-2.png',
    r'image-1\.png': 'image-1.png',
    r'image-10\.png': 'image-10.png',

    # Conference images
    r'26-1024x1024\.png': '27.png',  # Conference photo
    r'Logo_BL_2-1024x470\.png': 'uploads/Logo_BL_2.png',  # TCO logo

    # Timestamp images (from November CSCW post - these are LinkedIn post images)
    r'1731160880038': '27.png',  # Conference photos
    r'1731160879927': '28.png',
    r'1731160879811': 'ocrw.jpeg',  # Climate risk workshop
    r'1731160879684': 'ocrw.jpeg',
}

def fix_image_path(match):
    """Replace image path with corrected version"""
    full_path = match.group(1)
    filename = os.path.basename(full_path)

    # Try to find a mapping
    for pattern, replacement in IMAGE_MAPPINGS.items():
        if re.search(pattern, filename):
            # Return the new path
            return f'{{{{ "/assets/images/{replacement}" | relative_url }}}}'

    # If no mapping found, return original
    return match.group(0)

def process_file(filepath):
    """Process a single markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Find all image references
    # Pattern: {{ "/assets/images/uploads/filename" | relative_url }}
    content = re.sub(
        r'\{\{\s*"(/assets/images/uploads/[^"]+)"\s*\|\s*relative_url\s*\}\}',
        fix_image_path,
        content
    )

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 70)
    print("IMAGE PATH FIXER")
    print("=" * 70)
    print()
    print("Fixing WordPress size-specific image paths to match actual filenames...")
    print()

    # Process all markdown files in _posts
    posts_dir = Path('_posts')
    files_updated = 0

    for filepath in sorted(posts_dir.glob('*.md')):
        if process_file(filepath):
            print(f"✅ Updated: {filepath.name}")
            files_updated += 1
        else:
            print(f"   No changes: {filepath.name}")

    print()
    print("=" * 70)
    print(f"COMPLETE: Updated {files_updated} files")
    print("=" * 70)

if __name__ == '__main__':
    main()
