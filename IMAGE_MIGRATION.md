# Image Migration Guide

## Status: ✅ COMPLETE

All 121 images from WordPress have been successfully migrated and pushed to GitHub.

## What Was Completed

- ✅ Extracted all 121 images from WordPress export zip file
- ✅ All images committed to repository at `assets/images/uploads/`
- ✅ All images pushed to GitHub
- ✅ Content references properly configured with Jekyll paths

## Image Inventory

- **Total images:** 121 files (59 MB)
- **Location:** `assets/images/uploads/`
- **Includes:**
  - Team member photos
  - Blog post images (2021-2024)
  - Project images
  - Partner/funder logos
  - PDF documents (Bay Street Climate Report)
  - WordPress theme images

## Image References in Content

All content files reference images using Jekyll's relative_url filter:

```markdown
![alt text]({{ "/assets/images/uploads/filename.jpg" | relative_url }})
```

This ensures images work correctly whether deployed to GitHub Pages, custom domain, or localhost.

## Optional: Image Organization

If you want to reorganize images into subdirectories for better organization:

```bash
# Create organized structure
mkdir -p assets/images/{team,news,projects,logos}

# Example: Move team photos
mv assets/images/uploads/*-soden*.{jpg,png} assets/images/team/
mv assets/images/uploads/AL.png assets/images/team/
# etc.

# Example: Move logos
mv assets/images/uploads/*logo*.{png,svg} assets/images/logos/
mv assets/images/uploads/*Logo*.{png,svg} assets/images/logos/
```

**Important:** If you reorganize images, you must update the image paths in:
- Blog posts (`_posts/*.md`)
- Team member profiles (`_team/*.md`)
- Page files (`*.md`)

## Image Optimization (Optional)

To improve site performance, consider optimizing images:

```bash
# Install optimization tools
sudo apt-get install optipng jpegoptim

# Optimize PNGs
find assets/images -name "*.png" -exec optipng -o7 {} \;

# Optimize JPEGs
find assets/images -name "*.jpg" -exec jpegoptim --max=85 --strip-all {} \;
```

## Testing

Test images locally:

```bash
bundle exec jekyll serve
```

Open http://localhost:4000 and verify all images display correctly on:
- Blog posts
- Team member pages
- Home page and other content pages

## Deployment

Images are now in the repository and will automatically deploy with GitHub Pages. No additional configuration needed.
