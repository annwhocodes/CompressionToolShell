#!/bin/bash

echo "Image Compression Utility (Shell)"
read -p "Enter the path of the image file to compress: " image_file

if [[ -f "$image_file" ]]; then
    convert "$image_file" -quality 75% "${image_file%.*}_compressed.${image_file##*.}"
    echo "Image file compressed successfully: ${image_file%.*}_compressed.${image_file##*.}"
else
    echo "File not found! Exiting."
    exit 1
fi
