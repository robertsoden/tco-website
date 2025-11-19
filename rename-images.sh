#!/bin/bash
# Rename and move LinkedIn post images

# Create target directory
mkdir -p assets/images/news

# Define the mapping (source -> target)
# Based on the order in images-to-download.json

declare -A rename_map=(
  ["image-1.jpeg"]="2025-11-18-two-weeks-ago-the-climate-aligned-finance-act-cafa-was-reint.jpg"
  ["image-2.jpeg"]="2025-11-19-workshop-alert.jpg"
  ["image-3.jpeg"]="2025-11-19-tco-voices-hear-from-dylan-van-bramer-a-new-addition-to-the.jpg"
  ["image-4.jpeg"]="2025-09-20-project-spotlight-reimagining-our-relationship-with-water-th.jpg"
  ["image-5.jpeg"]="2025-11-19-glimpses-from-compass-2025-hosted-by-university-of-toronto-a.jpg"
  ["image-6.jpeg"]="2025-08-21-from-july-22-25-university-of-toronto-hosted-the-2025-iterat.jpg"
  ["image-7.jpeg"]="2025-11-19-event-recap-the-looming-lng-glut-market-assessment-risks-thi.jpg"
  ["ocrw.jpeg"]="2025-07-22-last-month-we-officially-wrapped-up-the-toronto-climate-summ.jpg"
)

echo "Renaming and moving LinkedIn post images..."
echo ""

# Process each file
for source in "${!rename_map[@]}"; do
  target="${rename_map[$source]}"
  src_path="assets/images/posts/$source"
  dest_path="assets/images/news/$target"

  if [ -f "$src_path" ]; then
    cp "$src_path" "$dest_path"
    echo "✓ $source -> $target"
  else
    echo "✗ Not found: $src_path"
  fi
done

echo ""
echo "Image renaming complete!"
echo ""
echo "Images in assets/images/news/:"
ls -lh assets/images/news/*.jpg 2>/dev/null || echo "No images found"
