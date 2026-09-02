# Toronto Climate Observatory - Jekyll Site

This is a Jekyll implementation of the Toronto Climate Observatory website, designed for hosting on GitHub Pages.

## 🚀 Quick Start

### Prerequisites

- Ruby (version 2.7 or higher)
- RubyGems
- GCC and Make

### Local Development

1. Clone this repository:
```bash
git clone https://github.com/yourusername/climate-observatory.git
cd climate-observatory
```

2. Install dependencies:
```bash
bundle install
```

3. Run the local development server:
```bash
bundle exec jekyll serve
```

4. Open your browser to `http://localhost:4000`

## 📦 Deployment to GitHub Pages

### Option 1: GitHub Pages with Custom Domain

1. Create a new repository on GitHub named `yourusername.github.io` or use any repository name for a project site

2. Update `_config.yml`:
```yaml
url: "https://yourusername.github.io"  # For user site
# OR
url: "https://yourusername.github.io"
baseurl: "/repository-name"  # For project site
```

3. Push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/repository-name.git
git push -u origin main
```

4. Enable GitHub Pages:
   - Go to your repository Settings
   - Navigate to "Pages" in the left sidebar
   - Under "Source", select the `main` branch
   - Click "Save"

5. Your site will be published at:
   - User site: `https://yourusername.github.io`
   - Project site: `https://yourusername.github.io/repository-name`

### Option 2: Custom Domain

1. Add a `CNAME` file to the root directory:
```
climateobservatory.ca
```

2. Configure your DNS provider:
   - Add an A record pointing to GitHub's IPs:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - OR add a CNAME record: `yourusername.github.io`

3. In GitHub repository settings > Pages, enter your custom domain

## 📁 Project Structure

```
climate-observatory-jekyll/
├── _config.yml           # Site configuration
├── _layouts/             # Page templates
│   ├── default.html      # Base layout
│   ├── post.html         # Blog post layout
│   └── team-member.html  # Team member profile layout
├── _includes/            # Reusable components
│   ├── header.html       # Site header/navigation
│   └── footer.html       # Site footer
├── _posts/               # Blog posts (YYYY-MM-DD-title.md format)
├── _team/                # Team member profiles
├── _data/                # Data files (YAML, JSON, CSV)
├── pages/                # Static pages
│   ├── about.md
│   ├── team.html
│   ├── our-work.md
│   ├── contact.md
│   └── news.html
├── assets/
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── images/           # Images and media
├── index.html            # Homepage
├── Gemfile               # Ruby dependencies
└── README.md             # This file
```

## ✏️ Content Management

### Adding a Blog Post

Create a new file in `_posts/` with the format `YYYY-MM-DD-title.md`:

```markdown
---
layout: post
title: "Your Post Title"
date: 2024-10-08
author: Author Name
categories: [category1, category2]
excerpt: A brief description of your post.
---

Your post content goes here...
```

### Adding a Team Member

Create a new file in `_team/` with a descriptive filename:

```markdown
---
name: Full Name
title: Position Title
category: faculty  # Options: faculty, graduate, research-assistant, alumni
order: 1  # Display order within category
image: /assets/images/team/filename.jpg
email: email@domain.com
website: https://example.com
research_interests: Brief description of research interests
bio: |
  Full biography text here.
  Can span multiple lines.
---
```

### Adding Images

1. Place images in `assets/images/` or subdirectories
2. Reference them in markdown:
```markdown
![Alt text]({{ '/assets/images/filename.jpg' | relative_url }})
```

## 🎨 Customization

### Colors

Edit CSS variables in `assets/css/style.css`:

```css
:root {
    --primary-color: #2c5f2d;
    --secondary-color: #97bc62;
    --accent-color: #ff6b35;
    /* ... */
}
```

### Navigation

Edit the menu items in `_includes/header.html`:

```html
<ul class="nav-menu">
    <li><a href="{{ '/' | relative_url }}">Home</a></li>
    <!-- Add or modify menu items here -->
</ul>
```

### Site Information

Update `_config.yml`:

```yaml
title: Your Site Title
email: your-email@domain.com
description: Your site description
```

## 🔧 Advanced Configuration

### Adding Collections

1. Define the collection in `_config.yml`:
```yaml
collections:
  projects:
    output: true
    permalink: /projects/:name/
```

2. Create a directory `_projects/`
3. Add content files
4. Create a layout `_layouts/project.html`

### Using Data Files

1. Create YAML files in `_data/` (e.g., `partners.yml`)
2. Access in templates: `{% for partner in site.data.partners %}`

### Plugins

GitHub Pages supports these Jekyll plugins by default:
- jekyll-feed
- jekyll-seo-tag
- jekyll-sitemap
- jekyll-github-metadata
- jekyll-avatar
- jemoji

Add to `_config.yml`:
```yaml
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-sitemap
```

## 📱 Responsive Design

The site is fully responsive and tested on:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (up to 767px)

## 🐛 Troubleshooting

### Build Errors

If you encounter build errors:

1. Check Ruby and Bundler versions:
```bash
ruby -v
bundle -v
```

2. Clear cache and rebuild:
```bash
bundle exec jekyll clean
bundle exec jekyll build
```

3. Update dependencies:
```bash
bundle update
```

### GitHub Pages Not Updating

1. Check the Actions tab in your repository for build status
2. Verify your `_config.yml` settings
3. Make sure you're pushing to the correct branch
4. Clear browser cache

## 📝 License

[Add your license information here]

## 🤝 Contributing

[Add contribution guidelines here]

## 📧 Contact

For questions or support, contact: toronto@climateobservatory.ca

## 🔗 Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [Markdown Guide](https://www.markdownguide.org/)
