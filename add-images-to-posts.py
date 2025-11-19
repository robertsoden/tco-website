#!/usr/bin/env python3
"""
Add image references to existing Jekyll posts
"""

import json
import re
from pathlib import Path

# Read the image mapping
with open('images-to-download.json', 'r') as f:
    image_data = json.load(f)

# Create a lookup dictionary: post-slug -> image path
image_lookup = {}
for item in image_data:
    key = f"{item['post_date']}-{item['post_slug']}"
    image_lookup[key] = item['save_as'].replace('assets/', '/assets/')

# Process all 2025 posts
posts_dir = Path('_posts')
updated_count = 0

for post_file in posts_dir.glob('2025-*.md'):
    # Extract date and slug from filename
    filename = post_file.stem  # Remove .md extension

    # Check if we have an image for this post
    if filename in image_lookup:
        # Read the post
        with open(post_file, 'r') as f:
            content = f.read()

        # Check if image already exists in front matter
        if 'image:' in content:
            print(f"  ⊙ Skipped {post_file.name} (already has image)")
            continue

        # Split front matter and body
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            body = parts[2]

            # Add image line before the closing ---
            # Insert it after the excerpt line
            image_line = f"image: {image_lookup[filename]}\n"

            # Add the image field
            front_matter_lines = front_matter.strip().split('\n')
            front_matter_lines.append(image_line.strip())
            new_front_matter = '\n'.join(front_matter_lines)

            # Reconstruct the file
            new_content = f"---\n{new_front_matter}\n---{body}"

            # Write back
            with open(post_file, 'w') as f:
                f.write(new_content)

            print(f"  ✓ Updated {post_file.name}")
            updated_count += 1
        else:
            print(f"  ✗ Failed to parse {post_file.name}")

print(f"\n{'='*60}")
print(f"Updated {updated_count} posts with image references")
print(f"{'='*60}")
