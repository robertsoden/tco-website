#!/usr/bin/env python3
"""
Create Jekyll blog posts from LinkedIn data
"""

import json
import os
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import urllib.request
import sys

# Read LinkedIn posts JSON
with open('linkedin-posts-raw.json', 'r') as f:
    posts = json.load(f)

# Reference date (today)
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

    if unit == 'h':  # hours
        return REFERENCE_DATE - timedelta(hours=amount)
    elif unit == 'd':  # days
        return REFERENCE_DATE - timedelta(days=amount)
    elif unit == 'w':  # weeks
        return REFERENCE_DATE - timedelta(weeks=amount)
    elif unit == 'mo':  # months
        return REFERENCE_DATE - timedelta(days=amount * 30)
    elif unit == 'y':  # years
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

    # Get first sentence
    first_sentence = re.split(r'[.!?]\s', content)[0]

    # Remove emojis and special characters
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

def download_image(url, filepath):
    """Download image from URL"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"  ✓ Downloaded image: {filepath}")
        return True
    except Exception as e:
        print(f"  ✗ Failed to download image: {e}")
        return False

# Create directories if they don't exist
Path('_posts').mkdir(exist_ok=True)
Path('assets/images/news').mkdir(parents=True, exist_ok=True)

# Process each post
created_posts = []

for i, post in enumerate(posts):
    content = post.get('content', '').strip()

    # Skip posts without sufficient content
    if len(content) < 50:
        print(f"Skipping post {i+1}: insufficient content")
        continue

    # Parse date
    date_str = post.get('date', '')
    post_date = parse_relative_date(date_str)
    date_formatted = post_date.strftime('%Y-%m-%d')

    # Extract title and create slug
    title = extract_title(content)
    slug = create_slug(title)

    # Clean content
    content = content.replace('…more', '').strip()
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Get excerpt (first paragraph, max 200 chars)
    first_para = content.split('\n\n')[0]
    excerpt = first_para[:200]
    if len(first_para) > 200:
        excerpt += '...'

    # Handle images
    main_image = get_main_image(post.get('images', []))
    image_path = None

    if main_image:
        img_url = main_image['url']
        # Determine file extension
        ext_match = re.search(r'\.(jpg|jpeg|png|gif|webp)', img_url, re.I)
        ext = ext_match.group(1) if ext_match else 'jpg'

        # Create filename
        img_filename = f"{date_formatted}-{slug}.{ext}"
        img_filepath = f"assets/images/news/{img_filename}"

        # Download image
        if download_image(img_url, img_filepath):
            image_path = f"/assets/images/news/{img_filename}"

    # Create front matter
    front_matter = f"""---
layout: post
title: "{title}"
date: {post_date.strftime('%Y-%m-%d')}
author: Toronto Climate Observatory
categories: [news, linkedin]
excerpt: "{excerpt}"
"""

    if image_path:
        front_matter += f"image: {image_path}\n"

    front_matter += "---\n\n"

    # Create post filename
    post_filename = f"_posts/{date_formatted}-{slug}.md"

    # Write post file
    with open(post_filename, 'w') as f:
        f.write(front_matter)
        f.write(content)
        f.write('\n')

        # Add links section if there are links
        links = post.get('links', [])
        external_links = [
            link for link in links
            if link.get('url') and not link['url'].startswith('https://www.linkedin.com/in/')
            and not link['url'].startswith('https://www.linkedin.com/company/')
            and not link['url'].startswith('https://www.linkedin.com/search/')
        ]

        if external_links:
            f.write('\n\n## Related Links\n\n')
            for link in external_links:
                url = link.get('url', '')
                text = link.get('text', url)
                # Clean up link text
                text = text.replace('\n', ' ').strip()
                if text and text != url:
                    f.write(f"- [{text}]({url})\n")
                else:
                    f.write(f"- {url}\n")

    created_posts.append(post_filename)
    print(f"✓ Created: {post_filename} - {title}")

print(f"\n{'='*60}")
print(f"Successfully created {len(created_posts)} Jekyll blog posts!")
print(f"{'='*60}")
