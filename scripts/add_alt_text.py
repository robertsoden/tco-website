#!/usr/bin/env python3
"""
Add alt text to images that are missing it for accessibility.
"""

import re
import os
from pathlib import Path


def generate_alt_text(image_path, context=""):
    """Generate meaningful alt text from image filename and context."""
    # Extract filename without extension
    filename = Path(image_path).stem

    # Clean up filename
    alt = filename.replace('-', ' ').replace('_', ' ')

    # Capitalize words
    alt = ' '.join(word.capitalize() for word in alt.split())

    # Handle common patterns
    if 'logo' in filename.lower():
        alt = f"{alt} Logo"
    elif 'team' in image_path.lower() or 'portrait' in filename.lower():
        # For team photos, use the filename as name
        alt = f"Portrait of {alt}"
    elif any(term in filename.lower() for term in ['report', 'cover', 'banner']):
        alt = f"{alt} Cover"
    elif 'image-' in filename.lower() and filename.lower().startswith('image-'):
        # Generic image names - use context or generic description
        alt = "Illustration"

    return alt


def add_alt_text_to_content(content):
    """Add alt text to images with empty alt attributes."""

    # Pattern: ![]({{ "/assets/images/..." | relative_url }})
    # or: ![](/assets/images/...)
    pattern = r'!\[\]\(({{\s*["\']([^"\']+)["\']\s*\|\s*relative_url\s*}}|([^)]+))\)'

    def replace_empty_alt(match):
        full_match = match.group(0)
        # Extract the image path
        if '{{' in full_match:
            # Jekyll liquid tag format
            image_path = match.group(2) if match.group(2) else match.group(1)
        else:
            # Direct path format
            image_path = match.group(3) if match.group(3) else match.group(1)

        # Generate alt text
        alt_text = generate_alt_text(image_path)

        # Return with alt text
        return full_match.replace('![]', f'![{alt_text}]')

    # Replace all empty alt text
    updated_content = re.sub(pattern, replace_empty_alt, content)

    return updated_content


def process_file(file_path):
    """Process a single file to add alt text to images."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has images with empty alt text
    if '![](' in content:
        print(f"Processing: {file_path}")

        # Split front matter from content
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            body = parts[2]

            # Add alt text to body
            updated_body = add_alt_text_to_content(body)

            # Reconstruct file
            updated_content = f"---{front_matter}---{updated_body}"
        else:
            # No front matter
            updated_content = add_alt_text_to_content(content)

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"  ✓ Added alt text")
    else:
        print(f"Skipping {file_path} (no images with empty alt)")


def main():
    """Process all markdown files."""
    base_dir = Path(__file__).parent.parent

    # Process blog posts
    posts_dir = base_dir / '_posts'
    print("\n=== Adding Alt Text to Blog Posts ===")
    for post_file in sorted(posts_dir.glob('*.md')):
        process_file(post_file)

    # Process pages
    pages_dir = base_dir / 'pages'
    print("\n=== Adding Alt Text to Pages ===")
    for page_file in sorted(pages_dir.glob('*.md')):
        process_file(page_file)

    # Process index page
    index_file = base_dir / 'index.html'
    if index_file.exists():
        print("\n=== Processing Index Page ===")
        process_file(index_file)

    print("\n✅ Alt text added to all images!")


if __name__ == '__main__':
    main()
