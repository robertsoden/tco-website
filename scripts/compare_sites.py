#!/usr/bin/env python3
"""
Compare WordPress site to Jekyll output

This script compares the content of the WordPress site with the Jekyll build
to verify that the migration preserved all content correctly.

Usage:
    python scripts/compare_sites.py

    # Or with custom URLs:
    python scripts/compare_sites.py --wp https://climateobservatory.ca --jekyll http://localhost:4000
"""
import requests
from bs4 import BeautifulSoup
import difflib
from urllib.parse import urljoin
import argparse
import sys

class SiteComparator:
    def __init__(self, wp_base, jekyll_base):
        self.wp_base = wp_base
        self.jekyll_base = jekyll_base

    def get_content(self, url):
        """Extract main content from a page"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch {url}: {e}")

        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove non-content elements
        for tag in soup.find_all(['script', 'style', 'nav', 'footer', 'header', 'meta', 'link']):
            tag.decompose()

        # Remove WordPress-specific elements
        for tag in soup.find_all(class_=['wp-block-navigation', 'wp-site-blocks']):
            tag.decompose()

        # Get main content
        main = (
            soup.find('main') or
            soup.find(class_='content') or
            soup.find(class_='main-content') or
            soup.find('body')
        )

        if not main:
            raise Exception(f"Could not find main content in {url}")

        # Extract text
        text = main.get_text(separator='\n', strip=True)

        # Normalize whitespace
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n'.join(lines)

    def compare_page(self, path):
        """Compare a single page"""
        print(f"\n{'='*70}")
        print(f"📄 Comparing: {path}")
        print('='*70)

        wp_url = urljoin(self.wp_base, path)
        jekyll_url = urljoin(self.jekyll_base, path)

        print(f"  WordPress: {wp_url}")
        print(f"  Jekyll:    {jekyll_url}")

        try:
            wp_content = self.get_content(wp_url)
            jekyll_content = self.get_content(jekyll_url)

            # Calculate similarity
            similarity = difflib.SequenceMatcher(
                None,
                wp_content,
                jekyll_content
            ).ratio()

            print(f"\n  📊 Similarity: {similarity*100:.1f}%")

            if similarity < 0.95:
                print("  ⚠️  Significant differences found")
                print("\n  First 30 lines of diff:")
                print("  " + "-"*66)
                # Show diff
                diff = difflib.unified_diff(
                    wp_content.splitlines()[:50],
                    jekyll_content.splitlines()[:50],
                    fromfile='WordPress',
                    tofile='Jekyll',
                    lineterm='',
                    n=2
                )
                diff_lines = list(diff)[:40]
                for line in diff_lines:
                    print(f"  {line}")
                if len(diff_lines) >= 40:
                    print(f"  ... (diff truncated)")
            elif similarity < 0.99:
                print("  ✓ Content mostly matches (minor differences)")
            else:
                print("  ✅ Content matches well")

            return similarity

        except Exception as e:
            print(f"  ❌ Error: {e}")
            return 0.0

    def compare_all(self, pages):
        """Compare multiple pages"""
        print("\n" + "="*70)
        print("WORDPRESS TO JEKYLL CONTENT COMPARISON")
        print("="*70)

        results = {}
        for page in pages:
            results[page] = self.compare_page(page)

        print("\n" + "="*70)
        print("📋 SUMMARY")
        print("="*70)

        if results:
            avg_similarity = sum(results.values()) / len(results)
            print(f"\nAverage similarity: {avg_similarity*100:.1f}%\n")

            # Sort by similarity (worst first)
            for page, sim in sorted(results.items(), key=lambda x: x[1]):
                if sim > 0.99:
                    status = "✅"
                elif sim > 0.95:
                    status = "✓ "
                elif sim > 0.80:
                    status = "⚠️ "
                else:
                    status = "❌"
                print(f"{status} {page:30s} {sim*100:.1f}%")

            # Final verdict
            print("\n" + "="*70)
            if avg_similarity > 0.95:
                print("✅ MIGRATION SUCCESSFUL - Content well preserved")
            elif avg_similarity > 0.80:
                print("⚠️  REVIEW NEEDED - Some content differences detected")
            else:
                print("❌ ISSUES FOUND - Significant content differences")
            print("="*70 + "\n")

            return avg_similarity > 0.95
        else:
            print("❌ No pages compared")
            return False


def main():
    parser = argparse.ArgumentParser(
        description='Compare WordPress site to Jekyll output'
    )
    parser.add_argument(
        '--wp',
        default='https://www.climateobservatory.ca',
        help='WordPress site base URL (default: https://www.climateobservatory.ca)'
    )
    parser.add_argument(
        '--jekyll',
        default='http://localhost:4000',
        help='Jekyll site base URL (default: http://localhost:4000)'
    )
    parser.add_argument(
        '--pages',
        nargs='+',
        help='Specific pages to compare (default: predefined list)'
    )

    args = parser.parse_args()

    # Default pages to compare
    default_pages = [
        '/',
        '/about/',
        '/team/',
        '/news/',
        '/our-work/',
        '/contact/',
    ]

    pages = args.pages if args.pages else default_pages

    comparator = SiteComparator(
        wp_base=args.wp,
        jekyll_base=args.jekyll
    )

    try:
        success = comparator.compare_all(pages)
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Comparison interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
