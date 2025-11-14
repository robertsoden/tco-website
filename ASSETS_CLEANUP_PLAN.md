# Assets Cleanup Plan

## Current Mess
- **385 images, 180MB** with massive duplication
- Same files exist in 3 locations:
  - `assets/images/uploads/` (correct)
  - `assets/images/upload_files_4/` (DELETE - duplicate)
  - `assets/images/uploads/upload_files_4/` (DELETE - duplicate)

## Actions Needed

### 1. Remove Duplicates
```bash
# Remove duplicate directory structures
rm -rf assets/images/upload_files_4/
rm -rf assets/images/uploads/upload_files_4/
```

### 2. Move Team Photos
```bash
# Team photos are correctly placed in assets/images/team/
# Keep as is
```

### 3. Move Root Images
```bash
# Move loose images from root to appropriate locations
# Keep assets/images/team/ for team photos
# Keep assets/images/uploads/ for blog/content images
```

## After Cleanup
- ~122 images in uploads/ (WordPress content)
- ~20 images in team/ (team photos)
- ~6 images in root (homepage/featured images)
- **Total: ~148 images, ~62MB** (down from 385/180MB)

## Still Missing
The 43 images from Nov-Dec 2024 posts are STILL NOT present. Those need to be downloaded separately from WordPress admin.
