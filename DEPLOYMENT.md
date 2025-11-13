# Deployment Checklist

## Before Deployment

### 1. Content Preparation
- [ ] Collect all images from the original site
- [ ] Save images to appropriate folders in `assets/images/`
- [ ] Update image paths in markdown files
- [ ] Create team member markdown files for all faculty, students, and staff
- [ ] Write or migrate blog posts to `_posts/` directory

### 2. Configuration
- [ ] Update `_config.yml` with correct site URL
- [ ] Set correct `baseurl` if using a project site
- [ ] Update site title, email, and description
- [ ] Verify all navigation links work

### 3. Customization
- [ ] Adjust color scheme in CSS if needed
- [ ] Add logo/favicon if available
- [ ] Customize footer content
- [ ] Add social media links

### 4. Testing Locally
- [ ] Run `bundle install`
- [ ] Run `bundle exec jekyll serve`
- [ ] Test all pages load correctly
- [ ] Check all links work
- [ ] Test on different screen sizes (mobile, tablet, desktop)
- [ ] Verify images display correctly
- [ ] Check navigation menu on mobile

## GitHub Repository Setup

### 5. Create Repository
- [ ] Create new repository on GitHub
- [ ] Name it appropriately (e.g., `yourusername.github.io` for user site)
- [ ] Initialize without README (you already have one)

### 6. Push Code
```bash
cd climate-observatory-jekyll
git init
git add .
git commit -m "Initial commit: Jekyll site for Toronto Climate Observatory"
git branch -M main
git remote add origin https://github.com/yourusername/repository-name.git
git push -u origin main
```

### 7. Enable GitHub Pages
- [ ] Go to repository Settings
- [ ] Navigate to "Pages" section
- [ ] Select source: Deploy from a branch
- [ ] Choose branch: `main`
- [ ] Choose folder: `/ (root)`
- [ ] OR enable GitHub Actions for deployment (recommended)

### 8. GitHub Actions Setup (Recommended)
- [ ] Verify `.github/workflows/jekyll.yml` is present
- [ ] Go to Settings > Pages
- [ ] Under "Build and deployment" select "GitHub Actions"
- [ ] Push a commit to trigger the workflow
- [ ] Check Actions tab for build status

## Custom Domain (Optional)

### 9. Configure Custom Domain
If using `climateobservatory.ca`:

- [ ] Create `CNAME` file in repository root:
```
climateobservatory.ca
```

- [ ] Configure DNS at your domain registrar:
  - Add A records pointing to:
    - 185.199.108.153
    - 185.199.109.153
    - 185.199.110.153
    - 185.199.111.153
  - OR add CNAME record: `yourusername.github.io`

- [ ] In GitHub Settings > Pages, enter custom domain
- [ ] Enable "Enforce HTTPS" (wait for certificate)

## Post-Deployment

### 10. Verification
- [ ] Visit the live site URL
- [ ] Test all pages and links
- [ ] Verify SSL certificate is active (https://)
- [ ] Test on multiple browsers (Chrome, Firefox, Safari, Edge)
- [ ] Test on mobile devices
- [ ] Check page load times
- [ ] Verify SEO meta tags

### 11. Monitoring & Maintenance
- [ ] Set up Google Analytics (optional)
- [ ] Set up Google Search Console (optional)
- [ ] Create backup of repository
- [ ] Document content update procedures
- [ ] Set up regular content review schedule

## Content Migration Priorities

### High Priority
1. All team member profiles with photos
2. Bay Street Climate Report information
3. Summer School information
4. About page values and mission
5. Contact information

### Medium Priority
1. News posts about recent grants and achievements
2. Our Work page with project descriptions
3. Partner and funder logos

### Low Priority
1. Historical blog posts
2. Additional project pages
3. Event archives

## Common Issues & Solutions

### Images Not Displaying
- Check image paths are correct: `{{ '/assets/images/filename.jpg' | relative_url }}`
- Verify images are in the repository
- Check file extensions match (case-sensitive on Linux)

### 404 Errors
- Verify `baseurl` in `_config.yml`
- Check permalink settings
- Ensure file names match URLs

### CSS Not Loading
- Clear browser cache
- Check CSS file path in `_layouts/default.html`
- Verify `assets/css/style.css` exists

### Build Failures
- Check Ruby version compatibility
- Run `bundle update`
- Check for syntax errors in frontmatter
- Review GitHub Actions logs

## Next Steps After Deployment

1. **Content Population**: Gradually migrate all content from original site
2. **SEO Optimization**: Add meta descriptions, optimize images
3. **Analytics**: Set up tracking to monitor visitor behavior
4. **Performance**: Optimize images, enable caching
5. **Accessibility**: Test with screen readers, ensure WCAG compliance
6. **Forms**: If needed, integrate form service (Formspree, Netlify Forms)
7. **Search**: Consider adding site search functionality
8. **Newsletter**: Integrate email newsletter if desired

## Maintenance Tasks

### Weekly
- [ ] Check for broken links
- [ ] Review new GitHub issues
- [ ] Monitor site uptime

### Monthly
- [ ] Update dependencies: `bundle update`
- [ ] Review analytics
- [ ] Backup content
- [ ] Check for security updates

### Quarterly
- [ ] Audit content freshness
- [ ] Review and update team information
- [ ] Performance optimization review
- [ ] Accessibility audit

## Support Resources

- Jekyll Documentation: https://jekyllrb.com/docs/
- GitHub Pages: https://docs.github.com/en/pages
- GitHub Community: https://github.community/
- Stack Overflow: Tag `jekyll`

## Contact for Help

For technical issues with the Jekyll implementation:
- Create an issue in the GitHub repository
- Contact the developer who created this site

For content questions:
- torontoclimateobservatory@gmail.com
