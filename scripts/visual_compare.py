#!/usr/bin/env python3
"""
Visual comparison of WordPress and Jekyll sites

This script takes screenshots of both sites and compares their visual appearance
and styling to identify differences.

Requirements:
    pip install playwright beautifulsoup4 requests pillow
    playwright install chromium

Usage:
    python scripts/visual_compare.py
    python scripts/visual_compare.py --wp https://climateobservatory.ca --jekyll http://localhost:4000
"""

import argparse
import sys
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

try:
    from playwright.sync_api import sync_playwright
    from PIL import Image
    VISUAL_AVAILABLE = True
except ImportError:
    VISUAL_AVAILABLE = False
    print("⚠️  playwright and/or pillow not installed. Visual comparison disabled.")
    print("   To enable: pip install playwright pillow && playwright install chromium")


class VisualComparator:
    def __init__(self, wp_base, jekyll_base, output_dir="screenshots"):
        self.wp_base = wp_base
        self.jekyll_base = jekyll_base
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def extract_computed_styles(self, url, selector=None):
        """Extract computed CSS styles from a page"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"  ❌ Failed to fetch {url}: {e}")
            return {}

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract inline and embedded styles
        styles = {}

        # Get all stylesheets
        style_tags = soup.find_all('style')
        for style in style_tags:
            if style.string:
                styles['embedded_css'] = styles.get('embedded_css', '') + style.string

        # Get inline styles on key elements
        selectors = [
            ('body', 'body'),
            ('header', 'header, .site-header, .header'),
            ('navigation', 'nav, .nav, .navigation'),
            ('hero', '.hero, .jumbotron, .banner'),
            ('cards', '.card, .news-item, .team-member-card'),
            ('buttons', 'button, .btn, .button, .cta-button'),
            ('footer', 'footer, .site-footer, .footer'),
        ]

        for name, sel in selectors:
            elements = soup.select(sel)
            if elements:
                elem = elements[0]
                style_attr = elem.get('style', '')
                if style_attr:
                    styles[f'{name}_inline'] = style_attr

                # Get CSS classes
                classes = elem.get('class', [])
                if classes:
                    styles[f'{name}_classes'] = ' '.join(classes)

        return styles

    def compare_colors(self, wp_url, jekyll_url):
        """Compare color schemes between sites"""
        print("\n  🎨 Comparing Color Schemes...")

        wp_styles = self.extract_computed_styles(wp_url)
        jekyll_styles = self.extract_computed_styles(jekyll_url)

        # Extract color patterns from CSS
        import re

        def extract_colors(css_text):
            colors = set()
            # Match hex colors
            colors.update(re.findall(r'#[0-9a-fA-F]{3,6}', css_text))
            # Match rgb/rgba colors
            colors.update(re.findall(r'rgba?\([^)]+\)', css_text))
            return colors

        wp_embedded = wp_styles.get('embedded_css', '')
        jekyll_embedded = jekyll_styles.get('embedded_css', '')

        wp_colors = extract_colors(wp_embedded)
        jekyll_colors = extract_colors(jekyll_embedded)

        # Find unique colors
        wp_only = wp_colors - jekyll_colors
        jekyll_only = jekyll_colors - wp_colors
        common = wp_colors & jekyll_colors

        print(f"     WordPress colors: {len(wp_colors)}")
        print(f"     Jekyll colors: {len(jekyll_colors)}")
        print(f"     Common colors: {len(common)}")

        if wp_only:
            print(f"\n     WordPress-only colors (first 5): {list(wp_only)[:5]}")
        if jekyll_only:
            print(f"     Jekyll-only colors (first 5): {list(jekyll_only)[:5]}")

        return {
            'wp_colors': len(wp_colors),
            'jekyll_colors': len(jekyll_colors),
            'common': len(common),
            'wp_only': len(wp_only),
            'jekyll_only': len(jekyll_only)
        }

    def take_screenshot(self, url, output_path, viewport_width=1920, viewport_height=1080):
        """Take a screenshot of a URL"""
        if not VISUAL_AVAILABLE:
            print(f"  ⚠️  Skipping screenshot (playwright not available)")
            return False

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                context = browser.new_context(
                    viewport={'width': viewport_width, 'height': viewport_height}
                )
                page = context.new_page()
                page.goto(url, wait_until='networkidle', timeout=30000)
                page.screenshot(path=str(output_path), full_page=True)
                browser.close()
            return True
        except Exception as e:
            print(f"  ❌ Screenshot failed: {e}")
            return False

    def compare_page(self, path, page_name):
        """Compare visual appearance of a page"""
        print(f"\n{'='*70}")
        print(f"📸 Comparing: {page_name} ({path})")
        print('='*70)

        wp_url = urljoin(self.wp_base, path)
        jekyll_url = urljoin(self.jekyll_base, path)

        print(f"  WordPress: {wp_url}")
        print(f"  Jekyll:    {jekyll_url}")

        # Create safe filename
        safe_name = page_name.replace('/', '_').replace(' ', '_')
        wp_screenshot = self.output_dir / f"{safe_name}_wordpress.png"
        jekyll_screenshot = self.output_dir / f"{safe_name}_jekyll.png"

        # Take screenshots
        print("\n  📷 Taking screenshots...")
        wp_success = self.take_screenshot(wp_url, wp_screenshot)
        jekyll_success = self.take_screenshot(jekyll_url, jekyll_screenshot)

        if wp_success and jekyll_success:
            print(f"  ✅ Screenshots saved:")
            print(f"     - {wp_screenshot}")
            print(f"     - {jekyll_screenshot}")

        # Compare colors
        color_comparison = self.compare_colors(wp_url, jekyll_url)

        # Compare styles
        print("\n  📋 Comparing CSS Classes...")
        wp_styles = self.extract_computed_styles(wp_url)
        jekyll_styles = self.extract_computed_styles(jekyll_url)

        for key in ['body_classes', 'header_classes', 'hero_classes']:
            wp_val = wp_styles.get(key, '')
            jekyll_val = jekyll_styles.get(key, '')
            if wp_val or jekyll_val:
                match = "✅" if wp_val == jekyll_val else "⚠️ "
                print(f"     {match} {key}:")
                print(f"        WP:     {wp_val[:60]}...")
                print(f"        Jekyll: {jekyll_val[:60]}...")

        return {
            'screenshots': wp_success and jekyll_success,
            'colors': color_comparison
        }

    def compare_all(self, pages):
        """Compare multiple pages"""
        print("\n" + "="*70)
        print("🎨 WORDPRESS TO JEKYLL VISUAL COMPARISON")
        print("="*70)
        print(f"📁 Screenshots will be saved to: {self.output_dir.absolute()}")

        if not VISUAL_AVAILABLE:
            print("\n⚠️  Visual comparison requires playwright and pillow")
            print("   Install with: pip install playwright pillow")
            print("   Then run: playwright install chromium")
            print("\n   Continuing with CSS comparison only...\n")

        results = {}
        for path, name in pages.items():
            results[name] = self.compare_page(path, name)

        print("\n" + "="*70)
        print("📊 SUMMARY")
        print("="*70)

        total_screenshots = sum(1 for r in results.values() if r.get('screenshots'))
        print(f"\n✅ Screenshots captured: {total_screenshots}/{len(results)}")

        # Color summary
        print(f"\n🎨 Color Scheme Analysis:")
        for name, result in results.items():
            colors = result.get('colors', {})
            if colors:
                wp_only = colors.get('wp_only', 0)
                jekyll_only = colors.get('jekyll_only', 0)
                if wp_only > 10 or jekyll_only > 10:
                    print(f"   ⚠️  {name}: {wp_only} WP-only colors, {jekyll_only} Jekyll-only colors")
                else:
                    print(f"   ✅ {name}: Color schemes similar")

        print("\n" + "="*70)
        print(f"📁 View screenshots in: {self.output_dir.absolute()}")
        print("="*70 + "\n")

        return True


def main():
    parser = argparse.ArgumentParser(
        description='Visual comparison of WordPress and Jekyll sites'
    )
    parser.add_argument(
        '--wp',
        default='https://www.climateobservatory.ca',
        help='WordPress site base URL'
    )
    parser.add_argument(
        '--jekyll',
        default='http://localhost:4000',
        help='Jekyll site base URL'
    )
    parser.add_argument(
        '--output',
        default='screenshots',
        help='Output directory for screenshots'
    )

    args = parser.parse_args()

    # Pages to compare
    pages = {
        '/': 'home',
        '/about/': 'about',
        '/team/': 'team',
        '/our-work/': 'our-work',
        '/news/': 'news',
        '/contact/': 'contact',
    }

    comparator = VisualComparator(
        wp_base=args.wp,
        jekyll_base=args.jekyll,
        output_dir=args.output
    )

    try:
        success = comparator.compare_all(pages)
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Comparison interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
