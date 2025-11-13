#!/usr/bin/env python3
"""
WordPress to Jekyll Migration Script
Parses WordPress XML export and creates Jekyll-formatted content
"""

import xml.etree.ElementTree as ET
import re
import os
from datetime import datetime
from urllib.parse import urlparse
import html

# WordPress XML namespaces
NAMESPACES = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/'
}

def clean_filename(title):
    """Convert title to a valid filename"""
    # Remove special characters, convert to lowercase, replace spaces with hyphens
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-')

def clean_content(content):
    """Clean WordPress content for Jekyll"""
    if not content:
        return ""

    # Unescape HTML entities
    content = html.unescape(content)

    # Remove WordPress-specific shortcodes
    content = re.sub(r'\[caption[^\]]*\](.*?)\[/caption\]', r'\1', content, flags=re.DOTALL)

    # Convert WordPress image syntax to Markdown
    # Match: <img src="..." alt="..." />
    def replace_img_with_alt(match):
        src = match.group(1)
        alt = match.group(2) if match.group(2) else ""
        # Extract filename from URL
        filename = os.path.basename(urlparse(src).path)
        return f'![{alt}]({{{{ "/assets/images/uploads/{filename}" | relative_url }}}})'

    def replace_img_no_alt(match):
        src = match.group(1)
        # Extract filename from URL
        filename = os.path.basename(urlparse(src).path)
        return f'![]({{{{ "/assets/images/uploads/{filename}" | relative_url }}}})'

    content = re.sub(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*/?>', replace_img_with_alt, content)
    content = re.sub(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*/?>', replace_img_no_alt, content)

    # Convert common HTML to Markdown
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content)
    content = re.sub(r'<i>(.*?)</i>', r'*\1*', content)

    # Handle links
    content = re.sub(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', r'[\2](\1)', content)

    # Remove extra blank lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    return content.strip()

def extract_excerpt(content):
    """Extract first paragraph as excerpt"""
    if not content:
        return ""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', content)
    # Get first sentence or first 150 characters
    sentences = re.split(r'[.!?]\s+', text)
    if sentences:
        excerpt = sentences[0]
        if len(excerpt) > 150:
            excerpt = excerpt[:150] + "..."
        return excerpt
    return ""

def parse_wordpress_xml(xml_file):
    """Parse WordPress XML and extract posts, pages, and attachments"""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    channel = root.find('channel')

    posts = []
    pages = []
    attachments = []

    for item in channel.findall('item'):
        # Get post type
        post_type_elem = item.find('wp:post_type', NAMESPACES)
        if post_type_elem is None:
            continue

        post_type = post_type_elem.text

        # Get status
        status_elem = item.find('wp:status', NAMESPACES)
        status = status_elem.text if status_elem is not None else 'draft'

        # Only process published content (except attachments - process all attachments)
        if status != 'publish' and post_type != 'attachment':
            continue

        # Common fields
        title_elem = item.find('title')
        title = title_elem.text if title_elem is not None and title_elem.text else "Untitled"

        content_elem = item.find('content:encoded', NAMESPACES)
        content = content_elem.text if content_elem is not None else ""

        date_elem = item.find('wp:post_date', NAMESPACES)
        pub_date = date_elem.text if date_elem is not None else ""

        author_elem = item.find('dc:creator', NAMESPACES)
        author = author_elem.text if author_elem is not None else "Unknown"

        # Get categories
        categories = []
        for cat in item.findall('category'):
            if cat.get('domain') == 'category' and cat.text:
                categories.append(cat.text)

        data = {
            'title': title,
            'content': content,
            'date': pub_date,
            'author': author,
            'categories': categories
        }

        if post_type == 'post':
            posts.append(data)
        elif post_type == 'page':
            # Get page slug
            slug_elem = item.find('wp:post_name', NAMESPACES)
            data['slug'] = slug_elem.text if slug_elem is not None else clean_filename(title)
            pages.append(data)
        elif post_type == 'attachment':
            # Get attachment URL
            url_elem = item.find('wp:attachment_url', NAMESPACES)
            if url_elem is not None and url_elem.text:
                attachments.append({
                    'title': title,
                    'url': url_elem.text,
                    'date': pub_date
                })

    return posts, pages, attachments

def create_jekyll_post(post, output_dir='_posts'):
    """Create a Jekyll post file"""
    os.makedirs(output_dir, exist_ok=True)

    # Parse date
    try:
        date_obj = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
        date_str = date_obj.strftime('%Y-%m-%d')
        year = date_obj.year
    except:
        date_str = '2024-01-01'
        year = 2024

    # Create filename
    title_slug = clean_filename(post['title'])
    filename = f"{date_str}-{title_slug}.md"
    filepath = os.path.join(output_dir, filename)

    # Create front matter
    front_matter = f"""---
layout: post
title: "{post['title']}"
date: {post['date']}
author: {post['author']}"""

    if post['categories']:
        cats = ', '.join(post['categories'])
        front_matter += f"\ncategories: [{cats}]"

    excerpt = extract_excerpt(post['content'])
    if excerpt:
        front_matter += f'\nexcerpt: "{excerpt}"'

    front_matter += "\n---\n\n"

    # Clean content
    content = clean_content(post['content'])

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        f.write(content)

    print(f"Created post: {filename}")
    return filepath

def create_jekyll_page(page, output_dir='.'):
    """Create a Jekyll page file"""
    # Create filename
    filename = f"{page['slug']}.md"
    filepath = os.path.join(output_dir, filename)

    # Skip if file already exists (to avoid overwriting custom pages)
    if os.path.exists(filepath):
        print(f"Skipped page (already exists): {filename}")
        return None

    # Create front matter
    front_matter = f"""---
layout: default
title: "{page['title']}"
permalink: /{page['slug']}/
---

# {page['title']}

"""

    # Clean content
    content = clean_content(page['content'])

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        f.write(content)

    print(f"Created page: {filename}")
    return filepath

def save_attachment_list(attachments, output_file='images_to_download.txt'):
    """Save list of image URLs to download"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for att in attachments:
            f.write(f"{att['url']}\n")
    print(f"\nSaved {len(attachments)} image URLs to {output_file}")

def main():
    xml_file = 'torontoclimateobservatory.WordPress.2025-11-13.xml'

    print("Parsing WordPress XML export...")
    posts, pages, attachments = parse_wordpress_xml(xml_file)

    print(f"\nFound:")
    print(f"  - {len(posts)} published posts")
    print(f"  - {len(pages)} published pages")
    print(f"  - {len(attachments)} attachments")

    print("\n" + "="*50)
    print("Creating Jekyll posts...")
    print("="*50)
    for post in posts:
        create_jekyll_post(post)

    print("\n" + "="*50)
    print("Creating Jekyll pages...")
    print("="*50)
    for page in pages:
        create_jekyll_page(page)

    print("\n" + "="*50)
    print("Saving attachment list...")
    print("="*50)
    save_attachment_list(attachments)

    print("\n✅ Migration complete!")
    print("\nNext steps:")
    print("  1. Download images using: wget -i images_to_download.txt -P assets/images/uploads/")
    print("  2. Review generated posts in _posts/")
    print("  3. Review generated pages in root directory")
    print("  4. Test with: bundle exec jekyll serve")

if __name__ == '__main__':
    main()
