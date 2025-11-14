#!/usr/bin/env python3
"""
Script to extract team member photo URLs from WordPress HTML and download them
"""
import re
import os
import urllib.request
from pathlib import Path

# Team member name to expected filename mapping
TEAM_MEMBERS = {
    # Graduate Students
    'taneea s agrawaal': 'taneea-agrawaal',
    'rayan awad alim': 'rayan-alim',
    'mickell als': 'mickell-als',
    'aarjav chauhan': 'aarjav-chauhan',
    'hana darling-wolf': 'hana-darling-wolf',
    'harshit gujral': 'harshit-gujral',
    'navyata neeraj': 'navyata-neeraj',
    'shreyasha paudel': 'shreyasha-paudel',
    'reyna wu': 'reyna-wu',

    # Research Assistants
    'cassandra chanen': 'cassandra-chanen',
    'allegra nesbitt-jerman': 'allegra-nesbitt-jerman',
    'tolulope oshinowo': 'tolulope-oshinowo',
    'nadim mottu': 'nadim-mottu',

    # Alumni
    'lilly flawn': 'lilly-flawn',
    'rohini patel': 'rohini-patel',
    'nadine plachta': 'nadine-plachta',
    'bowen zhang': 'bowen-zhang',
    'austin lord': 'austin-lord',
    'sophia jit': 'sophia-jit',
}

def extract_photo_urls(html_file):
    """Extract team member photo URLs from WordPress HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all image URLs and their associated names
    photo_map = {}

    # Pattern to find heading followed by image
    # Look for h6 tags with names, then find the preceding img tag
    sections = re.findall(r'<img[^>]*src="([^"]+)"[^>]*>.*?<h6[^>]*>(.*?)</h6>', html, re.DOTALL)

    for img_url, name_html in sections:
        # Clean up the name
        name = re.sub(r'<[^>]+>', '', name_html).strip().lower()

        # Get the actual image URL (not the CDN version)
        # Convert i0.wp.com URLs back to direct URLs
        if 'i0.wp.com' in img_url:
            # Extract the actual URL from the CDN URL
            actual_url = re.sub(r'https://i0\.wp\.com/', 'https://', img_url)
            # Remove query parameters
            actual_url = actual_url.split('?')[0]
        else:
            actual_url = img_url.split('?')[0]

        if name in TEAM_MEMBERS:
            photo_map[TEAM_MEMBERS[name]] = actual_url
            print(f"Found photo for {name}: {actual_url}")

    return photo_map

def download_photos(photo_map, output_dir):
    """Download photos to the output directory"""
    os.makedirs(output_dir, exist_ok=True)

    downloaded = {}

    for filename, url in photo_map.items():
        # Determine file extension from URL
        ext = os.path.splitext(url)[1] or '.jpg'
        output_file = os.path.join(output_dir, f"{filename}{ext}")

        try:
            print(f"Downloading {url} to {output_file}")
            # Add headers to avoid 403 Forbidden
            req = urllib.request.Request(
                url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            )
            with urllib.request.urlopen(req) as response, open(output_file, 'wb') as out_file:
                out_file.write(response.read())
            downloaded[filename] = output_file
            print(f"  ✓ Downloaded successfully")
        except Exception as e:
            print(f"  ✗ Error downloading: {e}")

    return downloaded

if __name__ == '__main__':
    # Read the WordPress HTML
    html_file = '/home/user/tco-website/wp-html/team.html'

    # Extract photo URLs
    print("Extracting photo URLs from WordPress HTML...")
    photo_map = extract_photo_urls(html_file)

    print(f"\nFound {len(photo_map)} photos")

    # Download photos
    print("\nDownloading photos...")
    output_dir = '/home/user/tco-website/assets/images/team'
    downloaded = download_photos(photo_map, output_dir)

    print(f"\nSuccessfully downloaded {len(downloaded)} photos")

    # Print summary
    print("\nSummary:")
    for filename, path in downloaded.items():
        print(f"  {filename}: {path}")
