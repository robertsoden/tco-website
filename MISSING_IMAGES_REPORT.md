# Missing Images Report

## Problem

**43 images** are referenced in blog posts but are missing from the repository. The WordPress export zip file did not include these images.

## Affected Posts

3 recent blog posts have broken image links:

1. **2024-11-04**: Conference - 6 TCO Research Projects Featured at CSCW 2024
   - Missing: 4 numbered timestamp images (1731160879684, etc.)

2. **2024-12-17**: The Himalayan Climate Data Field Lab
   - Missing: 19 IMG_*.jpg files (field trip photos)
   - Missing: Field-Lab-partial-group-photo_Week-1-1-1024x683.jpg

3. **2024-12-18**: TCO Newsletter December 2024
   - Missing: Various IMG_*.jpg files and logos

## Complete List of Missing Images

```
1731160879684
1731160879811
1731160879927
1731160880038
26-1024x1024.png
Field-Lab-partial-group-photo_Week-1-1-1024x683.jpg
IMG_1992-1-1024x768.jpg
IMG_2077-1-1024x768.jpg
IMG_2454-768x1024.jpg
IMG_2490-1-768x1024.jpg
IMG_2977-1-1024x768.jpg
IMG_3516-2-1024x768.jpg
IMG_3995-1-1024x768.jpg
IMG_5131-1-1024x768.jpg
IMG_5249-1-768x1024.jpg
IMG_5249-768x1024.jpg
IMG_5295-1024x768.jpg
IMG_5534-1-1024x768.jpg
IMG_6216-1024x768.jpg
IMG_6410-768x1024.jpg
IMG_6484-768x1024.jpg
IMG_6906-768x1024.jpg
IMG_6920-1024x768.jpg
Inaugural-Toronto-Climate-Summer-School-shows-students-that-climate-edited.png
Logo_BL_2-1024x470.png
OUR-VALUES-1-1-1024x1024.png
image-1.jpeg through image-10.png (various sizes)
```

## Why This Happened

The WordPress export zip file (`upload_files_4.zip`) was incomplete. It contained older images from 2023-2024, but was missing images from the most recent posts (November-December 2024).

## Solutions

### Option 1: Get Complete WordPress Export (Recommended)

You need to export ALL media from WordPress, specifically the 2024 uploads:

1. Log into WordPress admin: `https://climateobservatory.ca/wp-admin`
2. Go to **Media → Library**
3. Filter by: **Upload date → November 2024 and December 2024**
4. Use a plugin to export these files:
   - "Export Media Library" plugin
   - "All-in-One WP Migration"
   - "UpdraftPlus"
5. Extract downloaded files to `assets/images/uploads/`
6. Commit and push

### Option 2: Download Via FTP/SSH

If you have server access:

```bash
# Download November and December 2024 uploads
scp -r user@server:/path/to/wp-content/uploads/2024/11/* assets/images/uploads/
scp -r user@server:/path/to/wp-content/uploads/2024/12/* assets/images/uploads/
```

### Option 3: Manual Download

For each affected post:
1. Open in WordPress editor
2. Click each image
3. Copy image URL
4. Download manually
5. Place in `assets/images/uploads/`

### Option 4: Remove Images from Posts

If these images aren't critical, edit the 3 affected posts to remove the broken image references.

## Current Status

- ✅ 121 images successfully migrated (older posts work fine)
- ❌ 43 images missing (3 recent posts have broken images)
- ⚠️ WordPress export was incomplete

## Next Steps

1. Choose one of the solutions above
2. Add the 43 missing images to `assets/images/uploads/`
3. Test locally: `bundle exec jekyll serve`
4. Verify the 3 affected posts display correctly
5. Commit and push
