#!/usr/bin/env python3
"""
Find images that are actually referenced in Jekyll content
and identify unused images that can be removed.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def find_image_references(content_dir, extensions=None):
    """Find all image references in markdown/html files"""
    if extensions is None:
        extensions = ['.md', '.html', '.markdown']

    image_refs = set()
    file_count = 0

    for root, dirs, files in os.walk(content_dir):
        # Skip hidden directories and build directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['_site', 'node_modules']]

        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                file_count += 1

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Find markdown image syntax: ![alt](path)
                    md_images = re.findall(r'!\[.*?\]\((.*?)\)', content)

                    # Find HTML img tags: <img src="path">
                    html_images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)

                    # Find Jekyll liquid syntax: {{ "path" | relative_url }}
                    liquid_images = re.findall(r'\{\{\s*["\']([^"\']+)["\'].*?\|\s*relative_url', content)

                    # Find CSS background images
                    css_images = re.findall(r'background-image:\s*url\(["\']?([^"\')\s]+)["\']?\)', content)

                    for img in md_images + html_images + liquid_images + css_images:
                        # Extract just the filename or path within assets
                        img = img.strip()
                        # Remove any leading /
                        if img.startswith('/'):
                            img = img[1:]
                        # Only track images in assets directory
                        if img.startswith('assets/'):
                            # Store the full path and just the filename
                            image_refs.add(img)
                            # Also add just the filename for matching
                            filename = os.path.basename(img)
                            image_refs.add(filename)

                except Exception as e:
                    print(f"Warning: Error reading {filepath}: {e}")

    print(f"Scanned {file_count} content files")
    return image_refs

def find_actual_images(images_dir):
    """Find all actual image files in the directory"""
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico', '.bmp'}
    actual_images = {}

    for root, dirs, files in os.walk(images_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, start='.')
                actual_images[file] = rel_path

    return actual_images

def main():
    print("="*70)
    print("IMAGE USAGE ANALYZER")
    print("="*70)
    print()

    # Find all image references in content
    print("Step 1: Scanning content files for image references...")
    print("-" * 70)

    content_dirs = [
        '_posts',
        '_team',
        '_includes',
        '_layouts',
        '.'  # Root for page files
    ]

    all_refs = set()
    for content_dir in content_dirs:
        if os.path.exists(content_dir):
            refs = find_image_references(content_dir)
            all_refs.update(refs)
            print(f"  {content_dir}: {len(refs)} references")

    print(f"\nTotal unique image references: {len(all_refs)}")
    print()

    # Find actual images
    print("Step 2: Scanning for actual image files...")
    print("-" * 70)

    images_dir = 'assets/images'
    if not os.path.exists(images_dir):
        print(f"ERROR: {images_dir} directory not found!")
        return

    actual_images = find_actual_images(images_dir)
    print(f"Found {len(actual_images)} image files")
    print()

    # Compare and identify used/unused
    print("Step 3: Identifying used and unused images...")
    print("-" * 70)

    used_images = []
    unused_images = []

    for filename, filepath in actual_images.items():
        # Check if filename is referenced
        is_used = False

        # Direct filename match
        if filename in all_refs:
            is_used = True

        # Full path match
        if filepath in all_refs:
            is_used = True

        # Check if any reference contains this filename
        if not is_used:
            for ref in all_refs:
                if filename in ref or filepath in ref:
                    is_used = True
                    break

        if is_used:
            used_images.append(filepath)
        else:
            unused_images.append(filepath)

    # Print results
    print()
    print("="*70)
    print("RESULTS")
    print("="*70)
    print()

    print(f"✅ USED IMAGES: {len(used_images)}")
    if used_images and len(used_images) <= 20:
        for img in sorted(used_images):
            print(f"   - {img}")
    elif used_images:
        print(f"   (Showing first 20 of {len(used_images)})")
        for img in sorted(used_images)[:20]:
            print(f"   - {img}")
    print()

    print(f"❌ UNUSED IMAGES: {len(unused_images)}")
    if unused_images:
        for img in sorted(unused_images):
            print(f"   - {img}")
    print()

    # Calculate sizes
    total_size = 0
    unused_size = 0

    for filepath in actual_images.values():
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            total_size += size
            if filepath in unused_images:
                unused_size += size

    print("="*70)
    print("STORAGE SUMMARY")
    print("="*70)
    print(f"Total images size: {total_size / 1024 / 1024:.2f} MB")
    print(f"Unused images size: {unused_size / 1024 / 1024:.2f} MB")
    print(f"Potential savings: {unused_size / total_size * 100:.1f}%")
    print()

    # Save unused images list
    if unused_images:
        with open('unused_images.txt', 'w') as f:
            for img in sorted(unused_images):
                f.write(f"{img}\n")
        print(f"✅ Saved list of unused images to: unused_images.txt")
        print()

        # Create deletion script
        with open('delete_unused_images.sh', 'w') as f:
            f.write("#!/bin/bash\n")
            f.write("# Script to delete unused images\n")
            f.write("# Review carefully before running!\n\n")
            f.write("set -e\n\n")
            f.write(f"echo 'This will delete {len(unused_images)} unused images ({unused_size / 1024 / 1024:.2f} MB)'\n")
            f.write("read -p 'Are you sure? (yes/no): ' confirm\n\n")
            f.write('if [ "$confirm" != "yes" ]; then\n')
            f.write('    echo "Cancelled."\n')
            f.write('    exit 0\n')
            f.write('fi\n\n')
            f.write("echo 'Deleting unused images...'\n\n")

            for img in sorted(unused_images):
                f.write(f'rm -f "{img}"\n')

            f.write(f"\necho 'Deleted {len(unused_images)} files'\n")
            f.write("echo 'Done!'\n")

        os.chmod('delete_unused_images.sh', 0o755)
        print(f"✅ Created deletion script: delete_unused_images.sh")
        print()
        print("To delete unused images, run:")
        print("  ./delete_unused_images.sh")
        print()
    else:
        print("✅ All images are being used!")

    print("="*70)
    print("RECOMMENDATIONS")
    print("="*70)
    print()

    if unused_images:
        print("1. Review unused_images.txt to verify these images aren't needed")
        print("2. Check if any images are used in:")
        print("   - CSS files")
        print("   - JavaScript files")
        print("   - External references")
        print("3. If confirmed unnecessary, run: ./delete_unused_images.sh")
    else:
        print("All images appear to be in use. No cleanup needed!")

    print()

if __name__ == '__main__':
    main()
