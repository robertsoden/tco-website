# Image Migration Guide

## Issue

The WordPress site (climateobservatory.ca) has security plugins that block direct downloads of images with 403 Forbidden errors. This means the 296 images from the WordPress export cannot be automatically downloaded.

## Image URLs

All 296 image URLs have been saved to: `images_to_download.txt`

## Manual Migration Options

### Option 1: Download from WordPress Admin (Recommended)

1. Log into WordPress admin at `https://climateobservatory.ca/wp-admin`
2. Go to **Media Library**
3. Select all images and use a plugin like "Export Media Library" to download them as a zip
4. Extract to `assets/images/uploads/`

### Option 2: Access Server Files Directly

If you have FTP/SSH access to the WordPress server:

```bash
# Connect to server and copy wp-content/uploads directory
scp -r user@server:/path/to/wp-content/uploads/* ./assets/images/uploads/
```

### Option 3: Use WordPress Export Plugin

Install a plugin like "All-in-One WP Migration" or "Duplicator" which includes media files in the export.

### Option 4: Download via WordPress Media Library Manager

Use a plugin like "Media Library Assistant" to export media files systematically.

## Image References in Content

The migration script has already updated all content files to reference images at:

```markdown
![alt text]({{ "/assets/images/uploads/filename.jpg" | relative_url }})
```

Once you place the images in `assets/images/uploads/`, all image links should work automatically.

## Team Member Photos

Team member profile photos need special attention. Current references point to:
- `/assets/images/uploads/` (from WordPress migration)

You may want to reorganize these to:
- `/assets/images/team/` (following Jekyll convention)

If you move them, update the `image:` field in each `_team/*.md` file.

## Image Optimization (Optional)

After migrating images, consider optimizing them for web:

```bash
# Install optimization tools
sudo apt-get install optipng jpegoptim

# Optimize PNGs
find assets/images -name "*.png" -exec optipng -o7 {} \;

# Optimize JPEGs
find assets/images -name "*.jpg" -exec jpegoptim --max=85 --strip-all {} \;
```

## Status

- ✅ Image URLs extracted (296 images)
- ✅ Content updated to reference new paths
- ❌ Images not yet downloaded (blocked by security plugin)
- ⏳ Awaiting manual transfer

## Next Steps

1. Choose one of the migration options above
2. Download/transfer all images to `assets/images/uploads/`
3. Test the site locally: `bundle exec jekyll serve`
4. Verify all images display correctly
5. (Optional) Reorganize images into subdirectories:
   - `/assets/images/team/` - Team photos
   - `/assets/images/news/` - Blog post images
   - `/assets/images/projects/` - Project images
   - `/assets/images/logos/` - Logos and branding
