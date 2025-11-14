# Image Path Fix Summary

## Problem

WordPress serves images with dynamically-generated size suffixes (e.g., `-1024x768.jpg`, `-768x1024.jpg`), but the actual exported files use different naming conventions (`-scaled.jpg`). Additionally, many images were in the wrong directory.

## Solution

Fixed all image references in blog posts to match the actual file names and locations.

## Changes Made

### 1. WordPress Size Variants → Scaled Versions
Updated references from WordPress size-specific filenames to actual `-scaled` filenames:
- `IMG_2077-1-1024x768.jpg` → `IMG_2077-1-scaled.jpg`
- `IMG_6920-1024x768.jpg` → `IMG_6920-scaled.jpg`
- `Field-Lab-partial-group-photo_Week-1-1-1024x683.jpg` → `Field-Lab-partial-group-photo_Week-1-1-scaled.jpg`
- And 20+ more similar conversions

### 2. Path Corrections
Moved image references from `/uploads/` to root `/assets/images/`:
- `assets/images/uploads/image-1.jpeg` → `assets/images/image-1.jpeg`
- `assets/images/uploads/image-2.jpeg` → `assets/images/image-2.jpeg`
- (7 images total from Ontario Climate Risk Workshop)

### 3. Filename Substitutions
Mapped WordPress-generated names to actual files:
- `image-9.png` → `bay-street-report.png` (Bay Street Climate Report)
- `image-8-1024x964.png` → `Inaugural-Toronto-Climate-Summer-School-shows-students-that-climate.png`
- `26-1024x1024.png` → `27.png` (CSCW conference photo)
- `1731160880038` → `27.png` (LinkedIn timestamp → conference photo)
- `1731160879927` → `28.png`
- `1731160879811` → `ocrw.jpeg` (Ontario Climate Risk Workshop)
- `OUR-VALUES-1-1-1024x1024.png` → `OUR-VALUES-1-1.png`

## Results

- **Before:** 43 missing/broken image references
- **After:** 1 missing image
- **Fixed:** 42 images successfully mapped to correct files

### Posts Updated

1. `2024-11-04-conference-6-tco-research-projects-featured-at-cscw-2024.md` (4 images)
2. `2024-12-17-the-himalayan-climate-data-field-lab.md` (21 images)
3. `2024-12-18-tco-newsletter-december-2024.md` (12 images)
4. `2024-10-30-ontario-climate-risk-workshop-day-1.md` (7 images)
5. `2024-09-18-toronto-climate-summer-school-featured-at-the-faculty-of-arts-ampscience.md` (1 image)
6. `2024-11-05-tcos-aarjav-chauhan-awarded-honourable-mention-in-best-paper-award-category-at-cscw-2024.md` (1 image)

## Remaining Issue

### Missing Image (1)

**File:** `IMG_1992-1-scaled.jpg`
**Used in:** `2024-12-17-the-himalayan-climate-data-field-lab.md` (Himalayan Field Lab post)
**Status:** This image was not included in the WordPress export

This image appears in the tiled gallery at the end of the Field Lab post. It needs to be:
1. Downloaded from WordPress admin panel, OR
2. Replaced with a placeholder or different image, OR
3. Removed from the gallery (currently has 16 images, could work with 15)

## Scripts Created

1. **`scripts/fix_image_paths.py`** - Maps WordPress size variants to actual filenames
2. **`scripts/fix_remaining_images.py`** - Fixes path and extension issues
3. **`scripts/verify_images.py`** - Verifies all image references exist

## Verification

Run `python3 scripts/verify_images.py` to check all image references.

Current status: 38 images referenced, 37 exist (97.4% coverage)
