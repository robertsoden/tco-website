# Site Comparison Scripts

Automated tools to compare the WordPress site with the Jekyll migration.

## Available Scripts

### 1. Content Comparison (`compare_sites.py`)

Compares the text content between WordPress and Jekyll sites.

```bash
# Basic usage (compares to localhost:4000)
python scripts/compare_sites.py

# Custom Jekyll URL
python scripts/compare_sites.py --jekyll http://localhost:4000

# Compare specific pages
python scripts/compare_sites.py --pages / /about/ /team/
```

**What it does:**
- Fetches pages from both sites
- Extracts and normalizes text content
- Calculates similarity percentage
- Shows content differences

**No installation required** - uses only standard Python libraries (requests, beautifulsoup4)

---

### 2. Visual Comparison (`visual_compare.py`)

Compares visual appearance and takes screenshots of both sites.

```bash
# Basic usage
python scripts/visual_compare.py

# Custom URLs and output directory
python scripts/visual_compare.py --wp https://climateobservatory.ca --jekyll http://localhost:4000 --output my_screenshots
```

**What it does:**
- Takes full-page screenshots of both sites
- Compares color schemes (hex and RGB values)
- Extracts and compares CSS classes
- Identifies visual differences

**Installation required:**
```bash
pip install playwright pillow beautifulsoup4 requests
playwright install chromium
```

**Output:**
- Screenshots saved to `screenshots/` directory (or custom `--output` dir)
- Side-by-side comparison files: `page_name_wordpress.png` and `page_name_jekyll.png`
- Terminal output showing color and style differences

---

## Quick Start

### Option 1: Content Only (No Installation)

```bash
# Start your Jekyll server
bundle exec jekyll serve

# In another terminal, run comparison
python scripts/compare_sites.py
```

### Option 2: Full Visual Comparison

```bash
# Install dependencies
pip install playwright pillow beautifulsoup4 requests
playwright install chromium

# Start Jekyll server
bundle exec jekyll serve

# Run visual comparison
python scripts/visual_compare.py
```

---

## Example Output

### Content Comparison
```
======================================================================
📄 Comparing: /about/
======================================================================
  WordPress: https://www.climateobservatory.ca/about/
  Jekyll:    http://localhost:4000/about/

  📊 Similarity: 94.3%
  ⚠️  Significant differences found
```

### Visual Comparison
```
======================================================================
📸 Comparing: home (/)
======================================================================
  WordPress: https://www.climateobservatory.ca/
  Jekyll:    http://localhost:4000/

  📷 Taking screenshots...
  ✅ Screenshots saved:
     - screenshots/home_wordpress.png
     - screenshots/home_jekyll.png

  🎨 Comparing Color Schemes...
     WordPress colors: 45
     Jekyll colors: 32
     Common colors: 18

     WordPress-only colors: ['#303e7a', '#f7e597', '#afa480', '#202a54', '#0f1325']
     Jekyll-only colors: ['#2c5f2d', '#97bc62', '#ff6b35']
```

---

## Troubleshooting

### "playwright not installed"
```bash
pip install playwright
playwright install chromium
```

### "Permission denied"
```bash
chmod +x scripts/compare_sites.py
chmod +x scripts/visual_compare.py
```

### Jekyll server not running
```bash
bundle exec jekyll serve
```

### Port already in use
```bash
bundle exec jekyll serve --port 4001
python scripts/visual_compare.py --jekyll http://localhost:4001
```

---

## Interpreting Results

### Content Similarity Scores
- **>99%**: Excellent - content is virtually identical
- **95-99%**: Good - minor formatting differences
- **80-95%**: Review needed - some content missing or different
- **<80%**: Issues - significant content differences

### Visual Differences to Look For
- **Color schemes**: Are the primary/secondary/accent colors matching?
- **Typography**: Font families, sizes, and weights
- **Layout**: Spacing, padding, margins
- **Components**: Card styles, button styles, navigation appearance

---

## Tips

1. **Run content comparison first** - it's faster and doesn't require installation
2. **Compare one page at a time** for detailed analysis:
   ```bash
   python scripts/compare_sites.py --pages /about/
   python scripts/visual_compare.py  # will include /about/
   ```
3. **Use screenshots** to manually spot visual differences
4. **Check color output** - WordPress uses blues/yellows, current Jekyll may use greens/oranges
5. **Compare on same viewport size** - visual comparison uses 1920x1080 by default
