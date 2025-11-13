# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Jekyll static site** for the Toronto Climate Observatory (TCO) - a research hub at the University of Toronto focused on supporting just, place-based climate action across the Greater Toronto Area. The site is designed for deployment on **GitHub Pages**.

## Development Commands

### Local Development
```bash
# Install dependencies (first time only)
bundle install

# Start local development server
bundle exec jekyll serve

# Start with live reload
bundle exec jekyll serve --livereload

# Start with drafts visible
bundle exec jekyll serve --drafts

# Build site (output to _site/)
bundle exec jekyll build

# Clean build artifacts
bundle exec jekyll clean
```

The local server runs at `http://localhost:4000`.

### Dependency Management
```bash
# Update all gems
bundle update

# Update specific gem
bundle update jekyll

# Check Ruby version
ruby -v

# Check Bundler version
bundle -v
```

## Jekyll Site Structure

### Expected Directory Organization

The site follows standard Jekyll conventions. Files should be organized as:

- **`_layouts/`** - Page templates (default.html, post.html, team-member.html)
- **`_includes/`** - Reusable components (header.html, footer.html)
- **`_posts/`** - Blog posts in `YYYY-MM-DD-title.md` format
- **`_team/`** - Team member profiles (collection)
- **`_projects/`** - Project pages (collection, if used)
- **`assets/css/`** - Stylesheets
- **`assets/js/`** - JavaScript files
- **`assets/images/`** - Image assets organized by subdirectory (team/, news/, projects/, partners/, funders/)
- **Root-level `.md` files** - Content pages (about.md, contact.md, our-work.md)

### Configuration

Site configuration is in `_config.yml`:
- Site metadata (title, email, description)
- Build settings (markdown processor, theme, plugins)
- Collections configuration (team, projects)
- Default front matter for different content types
- URL settings (url, baseurl) - **must be updated for deployment**

## Content Architecture

### Collections

The site uses Jekyll collections for structured content:

1. **Team Members** (`_team/` collection)
   - Outputs individual pages at `/team/:name/`
   - Uses `team-member` layout
   - Front matter fields: name, title, category (faculty/graduate/research-assistant/alumni), order, image, email, website, research_interests, bio

2. **Projects** (`_projects/` collection)
   - Outputs individual pages at `/projects/:name/`
   - Uses `project` layout

3. **Blog Posts** (`_posts/` directory)
   - Standard Jekyll posts
   - Uses `post` layout
   - Naming: `YYYY-MM-DD-title.md`
   - Front matter: layout, title, date, author, categories, excerpt

### Layouts

Three main layouts build on each other:

1. **default.html** - Base layout with header, footer, SEO tags
2. **post.html** - Extends default for blog posts
3. **team-member.html** - Extends default for team profiles

All layouts use Liquid templating with `{% include %}` tags for header and footer.

### Front Matter Defaults

The `_config.yml` sets automatic defaults:
- Posts automatically use `post` layout
- Team collection automatically uses `team-member` layout
- Projects collection automatically uses `project` layout

## Styling and Assets

### CSS Architecture

The site uses a single CSS file (`assets/css/style.css`) with:
- CSS custom properties (variables) in `:root` for theming
- Mobile-first responsive design
- Breakpoints for tablet (768px) and desktop (1200px+)

Key CSS variables:
```css
--primary-color: #2c5f2d;      /* Green for headers/nav */
--secondary-color: #97bc62;    /* Light green accent */
--accent-color: #ff6b35;       /* Orange for CTAs */
```

To change the color scheme, edit these variables at the top of `style.css`.

### JavaScript

`assets/js/main.js` provides:
- Mobile menu toggle functionality
- Hamburger icon animation
- Click-outside-to-close behavior
- Smooth scrolling for anchor links

### Image Management

Images should be organized by purpose:
- `assets/images/team/` - Team member photos
- `assets/images/news/` - Blog post/news images
- `assets/images/projects/` - Project images
- `assets/images/partners/` - Partner logos
- `assets/images/funders/` - Funder logos

Reference images in Liquid templates: `{{ '/assets/images/path/file.jpg' | relative_url }}`

## GitHub Pages Deployment

### Workflow File

`.github/workflows/jekyll.yml` (or `jekyll.yml` in root) provides automated deployment:
- Triggers on push to `main` branch
- Uses Ruby 3.1
- Builds with Jekyll
- Deploys to GitHub Pages

### Pre-Deployment Checklist

Before deploying, update `_config.yml`:
```yaml
url: "https://yourusername.github.io"     # Your GitHub Pages URL
baseurl: "/repository-name"                # For project sites, or "" for user site
```

Enable GitHub Pages in repository Settings > Pages > Build and deployment > Source: "GitHub Actions"

## Content Management

### Adding a Blog Post

1. Create file: `_posts/YYYY-MM-DD-title.md`
2. Add front matter:
   ```yaml
   ---
   layout: post
   title: "Post Title"
   date: 2024-10-08
   author: Author Name
   categories: [category1, category2]
   excerpt: Brief description
   ---
   ```
3. Write content in Markdown below front matter
4. Add associated images to `assets/images/news/`

### Adding a Team Member

1. Create file: `_team/firstname-lastname.md`
2. Add front matter:
   ```yaml
   ---
   name: Full Name
   title: Position Title
   category: faculty  # or graduate, research-assistant, alumni
   order: 1
   image: /assets/images/team/photo.jpg
   email: email@domain.com
   website: https://example.com
   research_interests: Brief description
   bio: |
     Multi-line biography
   ---
   ```
3. Add photo to `assets/images/team/`

### Editing Page Content

Main pages are markdown files in root or under a `pages/` directory:
- `about.md` - Mission, values, partners
- `our-work.md` - Research approach, projects
- `contact.md` - Contact information
- `index.html` - Homepage (uses HTML for complex layout)
- `news.html` - Blog archive page
- `team.html` - Team directory page

## Key Conventions

### Liquid Templating

- Use `{{ }}` for output: `{{ site.title }}`
- Use `{% %}` for logic: `{% if page.title %}`
- Use `| relative_url` filter for all internal links and assets
- Loop through collections: `{% for member in site.team %}`

### Markdown Content

- Use standard Markdown syntax
- Jekyll uses **Kramdown** as the Markdown processor
- Front matter must be at the top of every content file

### File Naming

- Blog posts: `YYYY-MM-DD-descriptive-title.md` (dashes, lowercase)
- Team members: `firstname-lastname.md` (dashes, lowercase)
- Other content: descriptive names with dashes

## Dependencies

### Ruby Gems (via Gemfile)

- **github-pages** - Meta-gem that includes all GitHub Pages-compatible gems
- **jekyll-feed** - Generates RSS/Atom feed
- **jekyll-seo-tag** - Adds SEO meta tags

The `github-pages` gem ensures local development matches GitHub Pages environment.

### Platform-Specific Gems

- Windows: tzinfo, tzinfo-data, wdm
- JRuby: http_parser.rb

## Important Notes

### GitHub Pages Limitations

- Only certain Jekyll plugins are supported (jekyll-feed, jekyll-seo-tag, jekyll-sitemap, etc.)
- No custom plugins that require code execution
- Site builds in safe mode

### URL Configuration

The site uses `relative_url` filter throughout, which respects the `baseurl` setting. This allows the same code to work for:
- User sites (`username.github.io`) - empty baseurl
- Project sites (`username.github.io/project`) - baseurl is "/project"
- Custom domains - baseurl typically empty

### Content in Root vs. Subdirectories

Currently some files may be in the root directory that should be organized into Jekyll directories:
- If `default.html`, `post.html`, `team-member.html` are in root, they belong in `_layouts/`
- If `header.html`, `footer.html` are in root, they belong in `_includes/`
- If `style.css` is in root, it belongs in `assets/css/`
- If `main.js` is in root, it belongs in `assets/js/`

### Testing Before Deployment

Always test locally with `bundle exec jekyll serve` before pushing changes. Check:
- All pages render correctly
- Navigation links work
- Images display
- Mobile responsive design works
- No console errors in browser

## Project Context

### Site Purpose

The Toronto Climate Observatory studies and supports climate action in the Greater Toronto Area, with focus on:
- Climate finance and accountability (e.g., Bay Street Climate Report)
- Equity and environmental justice
- Place-based climate solutions
- Community capacity building

### Key Content Areas

1. **Research** - Climate finance, flood information, urban climate impacts
2. **Education** - Summer School program for undergraduates
3. **Engagement** - Capacity building, knowledge mobilization
4. **Team** - Faculty, graduate students, research assistants from multiple disciplines

When working with content, maintain the site's academic tone while ensuring accessibility for broader audiences.
