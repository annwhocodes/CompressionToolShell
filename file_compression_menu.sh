#!/bin/bash

echo "Welcome to File Compression Utility!"
echo "Choose your execution method:"
echo "1. Shell Execution"
echo "2. System Call (Python)"
read -p "Enter your choice (1 or 2): " method_choice

if [[ "$method_choice" -eq 1 ]]; then
    echo "You chose Shell Execution."
    echo "Choose the type of compression:"
    echo "1. Text Compression"
    echo "2. Image Compression"
    read -p "Enter your choice (1 or 2): " compression_choice

    if [[ "$compression_choice" -eq 1 ]]; then
        ./text_compression_shell.sh
    elif [[ "$compression_choice" -eq 2 ]]; then
        ./image_compression_shell.sh
    else
        echo "Invalid choice. Exiting."
        exit 1
    fi

elif [[ "$method_choice" -eq 2 ]]; then
    echo "You chose System Call (Python)."
    python3 file_compression_syscall.py
else
    echo "Invalid choice. Exiting."
    exit 1
fi
