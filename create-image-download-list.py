#!/usr/bin/env python3
"""
Add image references to Jekyll posts and create download list
"""

import json
import os
import re
from pathlib import Path

# Read LinkedIn posts JSON
with open('linkedin-posts-raw.json', 'r') as f:
    posts = json.load(f)

# Read the full original data to get all posts
with open('linkedin-posts.json', 'r') as f:
    full_data = json.load(f)

from datetime import datetime, timedelta

REFERENCE_DATE = datetime(2025, 11, 19)

def parse_relative_date(date_str):
    """Convert relative date like '4h', '2mo' to actual date"""
    if not date_str:
        return REFERENCE_DATE

    match = re.match(r'^(\d+)(h|d|w|mo|y)$', date_str)
    if not match:
        return REFERENCE_DATE

    amount, unit = match.groups()
    amount = int(amount)

    if unit == 'h':
        return REFERENCE_DATE - timedelta(hours=amount)
    elif unit == 'd':
        return REFERENCE_DATE - timedelta(days=amount)
    elif unit == 'w':
        return REFERENCE_DATE - timedelta(weeks=amount)
    elif unit == 'mo':
        return REFERENCE_DATE - timedelta(days=amount * 30)
    elif unit == 'y':
        return REFERENCE_DATE - timedelta(days=amount * 365)

    return REFERENCE_DATE

def create_slug(title):
    """Create URL-friendly slug from title"""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug[:60].strip('-')

def extract_title(content, max_length=80):
    """Extract title from post content"""
    if not content:
        return "LinkedIn Update"

    first_sentence = re.split(r'[.!?]\s', content)[0]
    cleaned = re.sub(r'[^\w\s-]', '', first_sentence)
    title = cleaned.strip()[:max_length]

    if len(first_sentence) > max_length:
        title += "..."

    return title if title else "TCO LinkedIn Update"

def get_main_image(images):
    """Get main content image (not logo)"""
    if not images:
        return None

    for img in images:
        url = img.get('url', '')
        if ('company-logo' not in url and
            'profile-framedphoto' not in url and
            '100_100' not in url and
            'media.licdn.com/dms/image' in url):
            return img

    return None

# Create download list
download_list = []
post_images = {}

for post in posts:
    content = post.get('content', '').strip()

    if len(content) < 50:
        continue

    # Parse date
    date_str = post.get('date', '')
    post_date = parse_relative_date(date_str)
    date_formatted = post_date.strftime('%Y-%m-%d')

    # Extract title and create slug
    title = extract_title(content)
    slug = create_slug(title)

    # Get main image
    main_image = get_main_image(post.get('images', []))

    if main_image:
        img_url = main_image['url']
        ext_match = re.search(r'\.(jpg|jpeg|png|gif|webp)', img_url, re.I)
        ext = ext_match.group(1) if ext_match else 'jpg'

        img_filename = f"{date_formatted}-{slug}.{ext}"
        img_filepath = f"assets/images/news/{img_filename}"

        download_list.append({
            'post_date': date_formatted,
            'post_title': title,
            'post_slug': slug,
            'image_url': img_url,
            'save_as': img_filepath
        })

        post_images[f"{date_formatted}-{slug}"] = {
            'image_path': f"/assets/images/news/{img_filename}",
            'image_url': img_url
        }

# Save download list as JSON
with open('images-to-download.json', 'w') as f:
    json.dump(download_list, f, indent=2)

# Create markdown instructions
with open('IMAGE-DOWNLOAD-INSTRUCTIONS.md', 'w') as f:
    f.write('# LinkedIn Post Images - Download Instructions\n\n')
    f.write('Download these images manually from LinkedIn and save them to the specified locations.\n\n')
    f.write(f'**Total images to download: {len(download_list)}**\n\n')
    f.write('## Quick Reference\n\n')
    f.write('You can download images using these methods:\n\n')
    f.write('### Method 1: Manual Download\n')
    f.write('1. Open each image URL in your browser\n')
    f.write('2. Right-click and "Save image as..."\n')
    f.write('3. Save to the location specified below\n\n')

    f.write('### Method 2: Command Line (curl)\n')
    f.write('```bash\n')
    f.write('# Create directory if needed\n')
    f.write('mkdir -p assets/images/news\n\n')
    f.write('# Download all images (copy/paste these commands)\n')
    for item in download_list:
        safe_url = item['image_url'].replace('&', '\\&')
        f.write(f"curl -L '{safe_url}' -o '{item['save_as']}'\n")
    f.write('```\n\n')

    f.write('### Method 3: Command Line (wget)\n')
    f.write('```bash\n')
    f.write('# Create directory if needed\n')
    f.write('mkdir -p assets/images/news\n\n')
    f.write('# Download all images\n')
    for item in download_list:
        f.write(f"wget '{item['image_url']}' -O '{item['save_as']}'\n")
    f.write('```\n\n')

    f.write('## Detailed Image List\n\n')

    for i, item in enumerate(download_list, 1):
        f.write(f"### {i}. {item['post_title']}\n\n")
        f.write(f"**Post Date:** {item['post_date']}\n\n")
        f.write(f"**Image URL:**\n")
        f.write(f"```\n{item['image_url']}\n```\n\n")
        f.write(f"**Save to:**\n")
        f.write(f"```\n{item['save_as']}\n```\n\n")
        f.write('---\n\n')

print(f"\n{'='*60}")
print(f"Created image download instructions!")
print(f"{'='*60}")
print(f"Images to download: {len(download_list)}")
print(f"\nFiles created:")
print(f"  - images-to-download.json")
print(f"  - IMAGE-DOWNLOAD-INSTRUCTIONS.md")
print(f"\nNext steps:")
print(f"  1. Review IMAGE-DOWNLOAD-INSTRUCTIONS.md")
print(f"  2. Download images using your preferred method")
print(f"  3. Images will automatically show up in posts once downloaded")
