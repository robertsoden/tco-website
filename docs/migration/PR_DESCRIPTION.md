# Complete WordPress to Jekyll migration with templating system

## Summary

This PR completes the WordPress to Jekyll migration for the Toronto Climate Observatory website with significant improvements to code organization and maintainability.

### Key Changes

#### 🎨 Homepage Completion
- Added hero section background image (toronto-3112508.jpg)
- Implemented mission, partners, and funders sections
- Created responsive CSS with hover effects for logos
- Full viewport height hero with proper background positioning

#### 📁 File Organization & Structure
- Created `pages/` directory for all content pages
- Moved 12 content pages from root to `pages/`
- Removed duplicate/unused WordPress exports (home.md, blog.md, clients.md, etc.)
- Cleaned up teluro.md (WordPress theme scaffolding)
- Converted remaining HTML pages to Markdown format

#### 🔧 Smart Templating System
- **New Layout**: `_layouts/page.html` - Standardized page template with automatic headers
- **New Includes**:
  - `_includes/team-section.html` - Reusable team member grid (accepts category/title params)
  - `_includes/partners-logos.html` - Centralized partner logo display
  - `_includes/funders-logos.html` - Centralized funder logo display
  - `_includes/news-grid.html` - Reusable news/blog post grid

#### 📊 Code Quality Improvements
- Reduced team.md from 112 lines to 10 lines (91% reduction)
- Eliminated code duplication across pages
- Single source of truth for partner/funder logos
- Consistent page styling using page layout

#### 🧪 Testing & Verification
- Added `scripts/compare_sites.py` - Automated content comparison tool
- Compares WordPress and Jekyll sites programmatically
- Calculates similarity percentages and shows detailed diffs
- Documentation in `scripts/README.md`

### Files Changed

**Created:**
- `_layouts/page.html`
- `_includes/team-section.html`
- `_includes/partners-logos.html`
- `_includes/funders-logos.html`
- `_includes/news-grid.html`
- `scripts/compare_sites.py`
- `scripts/requirements.txt`
- `scripts/README.md`
- `assets/images/partners/` (6 logo files)
- `assets/images/funders/` (5 logo files)

**Modified:**
- `index.html` - Added hero background, mission, partners, funders sections with includes
- `pages/about.md` - Uses page layout and includes
- `pages/team.md` - Simplified using team-section include
- `pages/news.md` - Uses page layout
- `assets/css/style.css` - Hero section, mission, partners, funders styling

**Deleted:**
- `pages/teluro.md` - WordPress theme artifact

### Benefits

✅ **Maintainability** - DRY principle applied, single source of truth
✅ **Consistency** - All pages use standardized layouts
✅ **Performance** - Cleaner, more efficient templates
✅ **Testability** - Automated comparison script for verification

## Test Plan

### Local Testing
```bash
# 1. Install dependencies
bundle install

# 2. Start Jekyll server
bundle exec jekyll serve

# 3. Verify pages render correctly
- http://localhost:4000/ (homepage with hero, mission, partners, funders)
- http://localhost:4000/about/ (uses includes)
- http://localhost:4000/team/ (simplified template)
- http://localhost:4000/news/ (blog archive)
```

### Content Verification
```bash
# Install Python dependencies
pip install -r scripts/requirements.txt

# Run comparison script (requires Jekyll running)
python scripts/compare_sites.py
```

### Visual Checks
- [ ] Hero background image displays correctly
- [ ] Mission section appears on homepage
- [ ] Partner logos display with hover effects
- [ ] Funder logos display with hover effects
- [ ] Team page shows all members by category
- [ ] Responsive design works on mobile/tablet
- [ ] All navigation links work

## Migration Status

- ✅ Content migration complete
- ✅ Image path fixes applied
- ✅ Templating system implemented
- ✅ File organization completed
- ✅ Comparison tooling created
- ⚠️ 1 image still missing: IMG_1992-1-scaled.jpg (documented in IMAGE_FIX_SUMMARY.md)

## Next Steps

After merge:
1. Deploy to GitHub Pages
2. Verify production site matches WordPress
3. Update DNS/domain settings if needed
4. Archive WordPress site

## Notes

This work builds on the initial WordPress export and image migration from previous commits. The feature branch name follows the session ID convention: `claude/migrate-climate-observatory-content-011CV581pchTuQjx5pWLd5Be`

---

## How to Create the PR

**Option 1: Via GitHub Web UI**
1. Go to https://github.com/robertsoden/tco-website
2. Click "Pull requests" → "New pull request"
3. Set base: `main`, compare: `claude/migrate-climate-observatory-content-011CV581pchTuQjx5pWLd5Be`
4. Copy/paste this description
5. Click "Create pull request"

**Option 2: Via Command Line**
```bash
gh pr create --title "Complete WordPress to Jekyll migration with templating system" \
  --body-file PR_DESCRIPTION.md \
  --base main \
  --head claude/migrate-climate-observatory-content-011CV581pchTuQjx5pWLd5Be
```
