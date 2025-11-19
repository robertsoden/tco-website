#!/usr/bin/env node

/**
 * Process LinkedIn posts JSON and create Jekyll blog posts
 */

const fs = require('fs');
const path = require('path');

// Read the JSON data from command line argument or stdin
const jsonData = JSON.parse(fs.readFileSync(process.argv[2] || 0, 'utf8'));

// Helper function to convert relative date to actual date
function parseRelativeDate(dateStr, referenceDate = new Date('2025-11-19')) {
  if (!dateStr) return referenceDate;

  const match = dateStr.match(/^(\d+)(h|d|w|mo|y)$/);
  if (!match) return referenceDate;

  const [, amount, unit] = match;
  const num = parseInt(amount);
  const date = new Date(referenceDate);

  switch (unit) {
    case 'h': // hours
      date.setHours(date.getHours() - num);
      break;
    case 'd': // days
      date.setDate(date.getDate() - num);
      break;
    case 'w': // weeks
      date.setDate(date.getDate() - (num * 7));
      break;
    case 'mo': // months
      date.setMonth(date.getMonth() - num);
      break;
    case 'y': // years
      date.setFullYear(date.getFullYear() - num);
      break;
  }

  return date;
}

// Helper function to format date as YYYY-MM-DD
function formatDate(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

// Helper function to create a slug from title
function createSlug(title) {
  return title
    .toLowerCase()
    .replace(/[^\w\s-]/g, '') // Remove special characters
    .replace(/\s+/g, '-')      // Replace spaces with hyphens
    .replace(/-+/g, '-')       // Replace multiple hyphens with single
    .substring(0, 60);         // Limit length
}

// Helper function to extract title from content
function extractTitle(content, maxLength = 100) {
  if (!content) return 'LinkedIn Update';

  // Get first sentence or first line
  const firstSentence = content.split(/[.!?]\s/)[0];
  const title = firstSentence.substring(0, maxLength);

  return title + (firstSentence.length > maxLength ? '...' : '');
}

// Helper function to get main content image (not logo)
function getMainImage(images) {
  if (!images || images.length === 0) return null;

  // Filter out logos and small images
  const contentImages = images.filter(img => {
    const url = img.url || '';
    return !url.includes('company-logo') &&
           !url.includes('profile-framedphoto') &&
           !url.includes('100_100');
  });

  return contentImages[0] || null;
}

// Helper function to extract image filename from URL
function getImageFilename(url, postSlug, index = 0) {
  const ext = url.match(/\.(jpg|jpeg|png|gif|webp)/i)?.[1] || 'jpg';
  return `${postSlug}-${index}.${ext}`;
}

// Process each post
const postsData = [];

jsonData.forEach((post, index) => {
  // Skip posts without content
  if (!post.content || post.content.trim().length < 50) {
    console.log(`Skipping post ${index + 1}: insufficient content`);
    return;
  }

  // Parse date
  const postDate = post.datetime
    ? new Date(post.datetime)
    : parseRelativeDate(post.date);

  const dateStr = formatDate(postDate);

  // Extract title
  const title = extractTitle(post.content);
  const slug = createSlug(title);

  // Get main image
  const mainImage = getMainImage(post.images);

  // Clean content - remove "...more" and excessive whitespace
  let content = post.content
    .replace(/…more$/i, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();

  // Extract excerpt (first paragraph)
  const excerpt = content.split('\n\n')[0].substring(0, 200) + '...';

  // Prepare post data
  const postData = {
    date: dateStr,
    title: title,
    slug: slug,
    excerpt: excerpt,
    content: content,
    image: mainImage,
    links: post.links || [],
    postUrl: post.postUrl
  };

  postsData.push(postData);

  console.log(`Processed: ${dateStr} - ${title}`);
});

// Output the processed data as JSON
console.log('\n=== Processed Posts ===\n');
fs.writeFileSync('processed-posts.json', JSON.stringify(postsData, null, 2));
console.log(`Created processed-posts.json with ${postsData.length} posts`);
