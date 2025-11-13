#!/bin/bash
# Download missing images from WordPress site

cd assets/images/uploads

# Missing images from posts
images=(
"image-1.jpeg"
"image-2.jpeg"
"image-3.jpeg"
"image-4.jpeg"
"image-5.jpeg"
"image-6.jpeg"
"image-7.jpeg"
"image-10.png"
"image.png"
"image-9.png"
"Field-Lab-partial-group-photo_Week-1-1-1024x683.jpg"
"IMG_1992-1-1024x768.jpg"
"IMG_2077-1-1024x768.jpg"
"IMG_2454-768x1024.jpg"
"IMG_2490-1-768x1024.jpg"
"IMG_2977-1-1024x768.jpg"
"IMG_3516-2-1024x768.jpg"
"IMG_3995-1-1024x768.jpg"
"IMG_5131-1-1024x768.jpg"
"IMG_5249-1-768x1024.jpg"
"IMG_5249-768x1024.jpg"
"IMG_5295-1024x768.jpg"
"IMG_5534-1-1024x768.jpg"
"IMG_6216-1024x768.jpg"
"IMG_6410-768x1024.jpg"
"IMG_6484-768x1024.jpg"
"IMG_6906-768x1024.jpg"
"IMG_6920-1024x768.jpg"
"26-1024x1024.png"
"image-2-1024x683.png"
"image-3-1024x293.png"
"image-4-1024x576.png"
"image-5-1024x681.png"
"image-6-791x1024.png"
"image-7-1024x964.png"
"image-8-1024x964.png"
"image-991x1024.png"
"Logo_BL_2-1024x470.png"
"OUR-VALUES-1-1-1024x1024.png"
"Inaugural-Toronto-Climate-Summer-School-shows-students-that-climate-edited.png"
)

base_url="https://www.climateobservatory.ca/wp-content/uploads/2024"

# Try to download from different month directories
for img in "${images[@]}"; do
    if [ ! -f "$img" ]; then
        echo "Attempting to download: $img"

        # Try different month folders
        for month in {01..12}; do
            url="$base_url/$month/$img"
            wget -q "$url" -O "$img" 2>/dev/null

            if [ $? -eq 0 ] && [ -s "$img" ]; then
                echo "✓ Downloaded: $img from $month/"
                break
            else
                rm -f "$img"
            fi
        done

        if [ ! -f "$img" ]; then
            echo "✗ Failed to download: $img"
        fi
    fi
done

echo ""
echo "Download complete!"
