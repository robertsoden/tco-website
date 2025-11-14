# TCO Website Migration Scripts

This directory contains utility scripts for the WordPress to Jekyll migration.

## Site Comparison Script

### Purpose

`compare_sites.py` compares the WordPress site content with the Jekyll site to verify the migration preserved all content correctly.

### Installation

Install required Python dependencies:

```bash
pip install -r scripts/requirements.txt
```

Or using a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r scripts/requirements.txt
```

### Usage

First, start the Jekyll development server:

```bash
bundle exec jekyll serve
```

Then in another terminal, run the comparison:

```bash
# Compare default pages
python scripts/compare_sites.py

# Compare with custom URLs
python scripts/compare_sites.py --wp https://climateobservatory.ca --jekyll http://localhost:4000

# Compare specific pages
python scripts/compare_sites.py --pages / /about/ /team/
```

### How It Works

The script:

1. Fetches HTML from both WordPress and Jekyll sites
2. Extracts main content (removes nav, footer, scripts, styles)
3. Normalizes whitespace
4. Calculates similarity percentage using text comparison
5. Shows differences when pages are <95% similar

### Interpreting Results

- **✅ 99-100%**: Perfect match
- **✓ 95-99%**: Good match with minor differences
- **⚠️ 80-95%**: Review needed - notable differences
- **❌ <80%**: Significant issues - content missing or wrong

### What It Checks

- ✅ Text content preservation
- ✅ Content structure
- ✅ Page accessibility

### What It Doesn't Check

- ❌ Visual styling/CSS
- ❌ Layout/positioning
- ❌ Images (only checks if they're referenced)
- ❌ JavaScript functionality

For visual verification, manually review the site or use visual regression testing tools like BackstopJS.

## Other Scripts

### Image Verification & Fixing

- `verify_images.py` - Checks for missing images
- `fix_image_paths.py` - Updates WordPress image paths to Jekyll format
- `fix_remaining_images.py` - Additional image path corrections

See `IMAGE_FIX_SUMMARY.md` in the root directory for details.
