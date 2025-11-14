#!/usr/bin/env python3
"""
Clean WordPress HTML remnants from Jekyll blog posts and pages.
Converts WordPress blocks to clean Markdown.
"""

import re
import os
from pathlib import Path


def clean_wordpress_content(content):
    """Remove WordPress HTML comments and blocks, convert to clean Markdown."""

    # Remove all WordPress block comments
    content = re.sub(r'<!-- wp:[^>]+ -->\n?', '', content)
    content = re.sub(r'<!-- /wp:[^>]+ -->\n?', '', content)

    # Fix double parentheses in image references
    # From: ![](({{ ... }})) to: ![]({{ ... }})
    content = re.sub(r'!\[\]\(\(({{[^}]+}})\)\)', r'![](\1)', content)

    # Convert WordPress heading HTML to Markdown
    # <h1 class="...">Text</h1> to # Text
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.DOTALL)

    # Remove WordPress-specific mark tags but keep content
    content = re.sub(r'<mark[^>]*>(.*?)</mark>', r'\1', content, flags=re.DOTALL)

    # Clean up paragraph tags with WordPress classes
    # <p class="has-text-align-center">**Text**</p> to **Text**
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1', content, flags=re.DOTALL)

    # Remove WordPress div containers but keep content
    content = re.sub(r'<div class="wp-block-columns[^"]*">', '', content)
    content = re.sub(r'<div class="wp-block-column[^"]*">', '', content)
    content = re.sub(r'<div class="wp-block-buttons[^"]*">', '', content)
    content = re.sub(r'<div class="wp-block-button[^"]*">', '', content)
    content = re.sub(r'</div>', '', content)

    # Clean up figure tags (keep image content)
    content = re.sub(r'<figure[^>]*>', '', content)
    content = re.sub(r'</figure>', '', content)

    # Remove horizontal rule HTML, replace with Markdown
    content = re.sub(r'<hr class="wp-block-separator[^"]*"/>', '---', content)

    # Remove social links blocks (not needed in Jekyll)
    content = re.sub(r'<ul class="wp-block-social-links[^>]*>.*?</ul>', '', content, flags=re.DOTALL)

    # Clean up extra blank lines (more than 2 consecutive)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Clean up spaces at end of lines
    content = re.sub(r' +\n', '\n', content)

    return content


def process_file(file_path):
    """Process a single markdown file to clean WordPress remnants."""
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split front matter from content
    parts = content.split('---', 2)
    if len(parts) >= 3:
        front_matter = parts[1]
        body = parts[2]

        # Clean the body content
        cleaned_body = clean_wordpress_content(body)

        # Reconstruct file
        cleaned_content = f"---{front_matter}---{cleaned_body}"
    else:
        # No front matter, clean entire content
        cleaned_content = clean_wordpress_content(content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print(f"  ✓ Cleaned")


def main():
    """Clean all blog posts and pages."""
    base_dir = Path(__file__).parent.parent

    # Process blog posts
    posts_dir = base_dir / '_posts'
    print("\n=== Cleaning Blog Posts ===")
    for post_file in sorted(posts_dir.glob('*.md')):
        process_file(post_file)

    # Process pages
    pages_dir = base_dir / 'pages'
    print("\n=== Cleaning Pages ===")
    for page_file in sorted(pages_dir.glob('*.md')):
        process_file(page_file)

    print("\n✅ All files cleaned!")


if __name__ == '__main__':
    main()
