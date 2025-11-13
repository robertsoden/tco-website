# Missing Images Report

## Summary

The WordPress export zip file (`upload_files_4.zip`) was **incomplete**. It contained 121 images, but only 39 are actually used by your migrated content, and **4 critical images are missing** from recent blog posts.

## Missing Images & Where They're Used

### High Priority - Recent Blog Posts

| Image File | Used In Post | Date |
|------------|--------------|------|
| `image-1.jpeg` through `image-7.jpeg` | Ontario Climate Risk Workshop Day 1 | 2024-10-30 |
| `IMG_*.jpg` files (multiple) | The Himalayan Climate Data Field Lab | 2024-12-17 |
| `Field-Lab-partial-group-photo_Week-1-1-1024x683.jpg` | The Himalayan Climate Data Field Lab | 2024-12-17 |
| Various numbered timestamps | TCO Newsletter December 2024 | 2024-12-18 |

### Complete Missing Images List

```
image-1.jpeg
image-2.jpeg
image-3.jpeg
image-4.jpeg
image-5.jpeg
image-6.jpeg
image-7.jpeg
image-10.png
image-9.png
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
26-1024x1024.png
image-2-1024x683.png
image-3-1024x293.png
image-4-1024x576.png
image-5-1024x681.png
image-6-791x1024.png
image-7-1024x964.png
image-8-1024x964.png
image-991x1024.png
Logo_BL_2-1024x470.png
OUR-VALUES-1-1-1024x1024.png
Inaugural-Toronto-Climate-Summer-School-shows-students-that-climate-edited.png
1731160879684
1731160879811
1731160879927
1731160880038
```

## How to Fix This

### Option 1: Complete WordPress Media Export (Recommended)

1. Log into WordPress admin at `https://climateobservatory.ca/wp-admin`
2. Go to **Media → Library**
3. Filter by upload date: **2024**
4. Use a plugin like:
   - "Export Media Library"
   - "All-in-One WP Migration"
   - "UpdraftPlus"
5. Download ALL media files
6. Extract to `assets/images/uploads/`

### Option 2: FTP/SSH Access

If you have direct server access:

```bash
# Connect to server and download WordPress uploads
scp -r user@server:/path/to/wp-content/uploads/2024/* ./assets/images/uploads/
```

### Option 3: Manual Download from WordPress

For each post with missing images:

1. Open the post in WordPress admin
2. Click on each image in the editor
3. Copy the image URL
4. Download manually
5. Place in `assets/images/uploads/`

### Option 4: Remove References to Missing Images

If the images aren't critical, you can edit the posts to remove the image references. The affected posts are:

- `_posts/2024-10-30-ontario-climate-risk-workshop-day-1.md`
- `_posts/2024-12-17-the-himalayan-climate-data-field-lab.md`
- `_posts/2024-12-18-tco-newsletter-december-2024.md`

## Current Status

✅ **Working:** 39 images properly migrated and displaying
❌ **Missing:** 43 images referenced but not present
⚠️ **Impact:** 3 recent blog posts will have broken images

## Next Steps

1. Choose one of the options above to get the missing images
2. Place them in `assets/images/uploads/`
3. Test locally: `bundle exec jekyll serve`
4. Verify all images display correctly
5. Commit and push

## Technical Details

The original WordPress export zip contained images primarily from 2023, but your most recent blog posts (October-December 2024) reference images that weren't included in that export. This suggests the zip was created from a partial backup or the Media Library export didn't include recent uploads.
