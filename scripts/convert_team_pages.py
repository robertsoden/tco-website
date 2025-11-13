#!/usr/bin/env python3
"""
Convert team member pages to _team collection format
"""

import os
import re

# List of team member page files
TEAM_MEMBERS = [
    'steve-easterbrook.md',
    'samar-sabie.md',
    'tegan-maharaj.md',
    'michael-classens.md',
    'karen-chapple.md',
    'ishtiaque-ahmed.md',
    'fadi-masoud.md',
    'michelle-murphy.md',
    'john-robinson.md',
    'imara-rolston.md',
    'hanna-morris.md',
    'nidhi-subramanyam.md',
    'nicole-spiegelaar.md',
    'laura-tozer.md',
    'fanny-chevalier.md'
]

def extract_text_from_html(content):
    """Extract plain text from HTML, preserving some structure"""
    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL|re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL|re.IGNORECASE)

    # Extract name from h1
    name_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else ""

    # Extract bio from paragraphs
    bio_parts = []
    for p_match in re.finditer(r'<p[^>]*>(.*?)</p>', content, re.DOTALL):
        text = p_match.group(1)
        # Clean up HTML entities and tags
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'&[a-z]+;', ' ', text)
        text = text.strip()
        if text and len(text) > 20:  # Filter out short/empty paragraphs
            bio_parts.append(text)

    bio = '\n  '.join(bio_parts) if bio_parts else ""

    # Extract image
    img_match = re.search(r'!\[\]\(\{\{ "(/assets/images/uploads/[^"]+)" \| relative_url \}\}\)', content)
    image = img_match.group(1) if img_match else ""

    return name, bio, image

def convert_team_page(filename):
    """Convert a team member page to _team collection format"""
    filepath = filename
    if not os.path.exists(filepath):
        print(f"Skipped: {filename} (not found)")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract information
    name, bio, image = extract_text_from_html(content)

    if not name:
        # Try to get name from filename
        name = filename.replace('.md', '').replace('-', ' ').title()

    # Clean up name (remove extra formatting)
    name = re.sub(r'\s+', ' ', name).strip()

    # Create proper front matter
    front_matter = f"""---
name: {name}
title: ""
category: faculty
order: 10
image: {image if image else '/assets/images/team/placeholder.jpg'}
email: ""
website: ""
research_interests: ""
bio: |
  {bio}
---
"""

    # Write to _team directory
    os.makedirs('_team', exist_ok=True)
    team_filepath = os.path.join('_team', filename)

    with open(team_filepath, 'w', encoding='utf-8') as f:
        f.write(front_matter)

    print(f"Converted: {filename} -> _team/{filename}")
    print(f"  Name: {name}")
    print(f"  Bio length: {len(bio)} chars")
    if image:
        print(f"  Image: {image}")
    print()

    # Remove original page file
    os.remove(filepath)

def main():
    print("Converting team member pages to _team collection...")
    print("="*60)
    print()

    for filename in TEAM_MEMBERS:
        convert_team_page(filename)

    print("="*60)
    print("✅ Team member conversion complete!")
    print("\nNote: You'll need to manually:")
    print("  1. Add missing information (titles, emails, websites, research interests)")
    print("  2. Verify category (faculty, graduate, research-assistant, alumni)")
    print("  3. Set proper order numbers")
    print("  4. Update image paths once images are uploaded")

if __name__ == '__main__':
    main()
