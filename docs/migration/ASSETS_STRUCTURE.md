# Assets Directory Structure

## Current Structure

```
assets/
├── css/                    # Stylesheets (15 KB)
│   └── style.css          # Main site styles
├── images/
│   └── uploads/           # All WordPress images (59 MB, 121 files)
└── js/                    # JavaScript (6.5 KB)
    └── main.js            # Site interactions
```

## Image Organization

All 121 migrated WordPress images are in `assets/images/uploads/`:
- Team member photos
- Blog post images (2021-2024)
- Project images
- Partner/funder logos
- PDF documents
- WordPress theme images

## Content References

All content files reference images as:
```liquid
{{ "/assets/images/uploads/filename.jpg" | relative_url }}
```

This structure is:
- ✅ Clean and simple
- ✅ Matches all content references
- ✅ Ready for Jekyll/GitHub Pages deployment
- ✅ No empty directories

## Adding New Images

Place new images in the appropriate directory:
```bash
# Add new images to uploads
cp new-image.jpg assets/images/uploads/

# Reference in content
![Description]({{ "/assets/images/uploads/new-image.jpg" | relative_url }})
```

## Future Organization (Optional)

If you want to organize images by type later, you could:
1. Create subdirectories (team/, news/, logos/, etc.)
2. Move images to appropriate folders
3. Update all image paths in content files

However, the current single-directory structure is simpler and works perfectly.
