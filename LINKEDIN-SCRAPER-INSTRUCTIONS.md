# LinkedIn Post Scraper - Instructions

## Step-by-Step Guide

### 1. Open Your LinkedIn Company Posts Page

Navigate to: https://www.linkedin.com/company/toronto-climate-observatory/posts/

Make sure you're logged into LinkedIn with an account that has access to view the posts.

### 2. Load All Posts

Scroll down the page to load all the posts you want to extract. LinkedIn loads posts dynamically as you scroll, so keep scrolling until you've loaded all the posts you want to convert to Jekyll posts.

### 3. Open Browser Developer Tools

- **Chrome/Edge**: Press `F12` or `Ctrl+Shift+I` (Windows) / `Cmd+Option+I` (Mac)
- **Firefox**: Press `F12` or `Ctrl+Shift+K` (Windows) / `Cmd+Option+K` (Mac)
- **Safari**: Enable Developer menu first (Preferences > Advanced > Show Develop menu), then press `Cmd+Option+I`

Or right-click anywhere on the page and select "Inspect" or "Inspect Element".

### 4. Go to the Console Tab

In the Developer Tools panel, click on the "Console" tab.

### 5. Run the Scraper Script

1. Open the file `linkedin-scraper.js` in a text editor
2. Copy the entire contents (Ctrl+A, Ctrl+C)
3. Paste it into the Console (Ctrl+V)
4. Press Enter to run the script

### 6. Copy the Output

The script will:
- Extract all visible posts
- Display the data as JSON in the console
- Automatically copy it to your clipboard (if supported)

You should see output like:

```
✅ Successfully extracted X posts!

====== START JSON DATA ======
[
  {
    "content": "Post text here...",
    "date": "1w",
    "images": [...],
    ...
  }
]
====== END JSON DATA ======
```

### 7. Save the JSON Data

1. If the data was auto-copied to clipboard, paste it into a new file
2. Otherwise, manually copy everything between `====== START JSON DATA ======` and `====== END JSON DATA ======`
3. Save it as `linkedin-posts.json`

### 8. Share with Claude

Send the `linkedin-posts.json` file content to Claude, who will:
- Parse the JSON data
- Download any images
- Create properly formatted Jekyll blog posts in `_posts/`
- Organize images in `assets/images/news/`
- Commit everything to your git branch

## Troubleshooting

### "No posts found" Error
- Make sure you're on the correct page (company posts page, not just company page)
- Scroll down to load posts first
- Ensure you're logged into LinkedIn

### Only a Few Posts Extracted
- Scroll down more to load additional posts before running the script
- LinkedIn lazy-loads content, so posts need to be visible in the browser first

### Images Not Extracted
- Some images may be blocked by LinkedIn's loading strategy
- You may need to scroll to the post to trigger image loading
- We can manually add image URLs later if needed

### Browser Console Warnings
- You may see warnings about "pasting code into console" - this is a security feature
- Type `allow pasting` if prompted and try again
- This is safe when using code you trust

## Next Steps

Once you have the JSON data, simply share it with Claude and the Jekyll posts will be automatically created!
