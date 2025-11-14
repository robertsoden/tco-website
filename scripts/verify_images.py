#!/usr/bin/env python3
"""
Verify that all images referenced in blog posts actually exist.
"""

import os
import re
from pathlib import Path

def extract_image_refs(content):
    """Extract all image references from content"""
    # Pattern: {{ "/assets/images/filename" | relative_url }}
    pattern = r'\{\{\s*"(/assets/images/[^"]+)"\s*\|\s*relative_url\s*\}\}'
    matches = re.findall(pattern, content)
    return [match.lstrip('/') for match in matches]

def main():
    print("=" * 70)
    print("IMAGE VERIFICATION")
    print("=" * 70)
    print()

    # Process all markdown files in _posts
    posts_dir = Path('_posts')
    all_refs = set()
    missing_images = []

    for filepath in sorted(posts_dir.glob('*.md')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        refs = extract_image_refs(content)
        if refs:
            print(f"{filepath.name}:")
            for ref in refs:
                all_refs.add(ref)
                exists = os.path.exists(ref)
                status = "✅" if exists else "❌"
                filename = os.path.basename(ref)
                print(f"  {status} {filename}")
                if not exists:
                    missing_images.append((filepath.name, ref))
            print()

    print("=" * 70)
    print(f"SUMMARY")
    print("=" * 70)
    print(f"Total image references: {len(all_refs)}")
    print(f"Missing images: {len(missing_images)}")
    print()

    if missing_images:
        print("MISSING IMAGES:")
        for post, image in missing_images:
            print(f"  {post} -> {image}")
        print()

if __name__ == '__main__':
    main()
