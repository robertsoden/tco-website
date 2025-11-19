/**
 * LinkedIn Post Scraper - Browser Console Script
 *
 * Instructions:
 * 1. Open https://www.linkedin.com/company/toronto-climate-observatory/posts/ in your browser
 * 2. Make sure you're logged into LinkedIn
 * 3. Scroll down to load all the posts you want to extract
 * 4. Open browser Developer Tools (F12 or Right-click > Inspect)
 * 5. Go to the Console tab
 * 6. Copy and paste this entire script
 * 7. Press Enter to run it
 * 8. The script will output JSON data - copy it and save to a file
 */

(function() {
    console.log('🔍 Starting LinkedIn post extraction...');

    const posts = [];

    // Try multiple selectors as LinkedIn's HTML structure can vary
    const postSelectors = [
        'div.feed-shared-update-v2',
        'div[data-urn*="urn:li:activity"]',
        'div.scaffold-finite-scroll__content > div',
        'article'
    ];

    let postElements = [];

    // Find which selector works
    for (const selector of postSelectors) {
        postElements = document.querySelectorAll(selector);
        if (postElements.length > 0) {
            console.log(`✅ Found ${postElements.length} posts using selector: ${selector}`);
            break;
        }
    }

    if (postElements.length === 0) {
        console.error('❌ No posts found. Make sure you are on the company posts page and posts are loaded.');
        console.log('💡 Try scrolling down the page first to load posts, then run this script again.');
        return;
    }

    postElements.forEach((postElement, index) => {
        try {
            const post = {};

            // Extract post text/content
            const textSelectors = [
                '.feed-shared-update-v2__description',
                '.feed-shared-text',
                '.break-words',
                '[data-test-id="main-feed-activity-card__commentary"]',
                '.update-components-text'
            ];

            for (const selector of textSelectors) {
                const textElement = postElement.querySelector(selector);
                if (textElement) {
                    post.content = textElement.innerText.trim();
                    break;
                }
            }

            // Extract date
            const dateSelectors = [
                'span.feed-shared-actor__sub-description',
                'time',
                '.feed-shared-actor__description',
                '[data-test-id="feed-shared-actor__sub-description"]'
            ];

            for (const selector of dateSelectors) {
                const dateElement = postElement.querySelector(selector);
                if (dateElement) {
                    post.date = dateElement.innerText.trim();
                    // Also try to get datetime attribute if it's a time element
                    if (dateElement.getAttribute('datetime')) {
                        post.datetime = dateElement.getAttribute('datetime');
                    }
                    break;
                }
            }

            // Extract images
            const images = [];
            const imageElements = postElement.querySelectorAll('img[src*="media"]');
            imageElements.forEach(img => {
                const src = img.src;
                // Filter out profile pictures and icons, keep content images
                if (src && !src.includes('profile-displayphoto') && !src.includes('icon')) {
                    images.push({
                        url: src,
                        alt: img.alt || ''
                    });
                }
            });
            post.images = images;

            // Extract any links in the post
            const links = [];
            const linkElements = postElement.querySelectorAll('a[href*="http"]');
            linkElements.forEach(link => {
                const href = link.href;
                // Filter out LinkedIn internal links
                if (!href.includes('linkedin.com/feed') &&
                    !href.includes('linkedin.com/company/toronto-climate-observatory')) {
                    links.push({
                        url: href,
                        text: link.innerText.trim()
                    });
                }
            });
            post.links = links.length > 0 ? links : undefined;

            // Extract post URL/ID
            const postUrlElement = postElement.querySelector('a[href*="activity"]');
            if (postUrlElement) {
                post.postUrl = postUrlElement.href;
            }

            // Only add if we got at least some content
            if (post.content || post.images.length > 0) {
                post.index = index + 1;
                posts.push(post);
            }

        } catch (error) {
            console.warn(`⚠️ Error processing post ${index + 1}:`, error);
        }
    });

    console.log(`\n✅ Successfully extracted ${posts.length} posts!\n`);
    console.log('📋 Copy the JSON data below:\n');
    console.log('====== START JSON DATA ======');
    console.log(JSON.stringify(posts, null, 2));
    console.log('====== END JSON DATA ======\n');

    // Also copy to clipboard if possible
    const jsonData = JSON.stringify(posts, null, 2);

    if (navigator.clipboard) {
        navigator.clipboard.writeText(jsonData).then(() => {
            console.log('✅ JSON data has been copied to your clipboard!');
            console.log('📝 Paste it into a file named "linkedin-posts.json" and share with Claude.');
        }).catch(() => {
            console.log('⚠️ Could not auto-copy. Please manually copy the JSON data above.');
        });
    } else {
        console.log('⚠️ Auto-copy not available. Please manually copy the JSON data above.');
    }

    // Store in a global variable for easy access
    window.linkedInPosts = posts;
    console.log('\n💡 Data is also available in: window.linkedInPosts');

})();
