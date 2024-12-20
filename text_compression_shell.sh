#!/bin/bash

echo "Run-Length Encoding (RLE) Text Compression Utility (Shell)"

# Prompt user for input file path
read -p "Enter the path of the text file to compress: " text_file

# Check if the input file exists
if [[ -f "$text_file" ]]; then
    # Prepare the output file name
    compressed_file="${text_file%.txt}_compressed.txt"

    # Initialize variables
    output_content=""
    while IFS= read -r -n1 char; do
        if [[ -z "$current_char" ]]; then
            current_char="$char"
            count=1
        elif [[ "$char" == "$current_char" ]]; then
            ((count++))
        else
            output_content+="$current_char$count"
            current_char="$char"
            count=1
        fi
    done < "$text_file"

    # Append the last character and count
    if [[ -n "$current_char" ]]; then
        output_content+="$current_char$count"
    fi

    # Write the compressed content to the output file
    echo -n "$output_content" > "$compressed_file"
    echo "Text file compressed successfully: $compressed_file"
else
    echo "File not found! Exiting."
    exit 1
fi

