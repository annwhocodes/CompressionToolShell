import os
import subprocess

# Function to compress a text file using Run-Length Encoding
def compress_file(input_filename):
    try:
        # Verify the input file exists
        if not os.path.isfile(input_filename):
            print(f"Error: File '{input_filename}' not found!")
            return None

        # Prepare output filename
        compressed_filename = f"{os.path.splitext(input_filename)[0]}_compressed.txt"

        # Compress the file
        with open(input_filename, 'r') as input_file, open(compressed_filename, 'w') as output_file:
            current_char = input_file.read(1)
            while current_char:
                count = 1
                while True:
                    next_char = input_file.read(1)
                    if not next_char or next_char != current_char:
                        break
                    count += 1
                output_file.write(f"{current_char}{count}")
                current_char = next_char

        print(f"File compressed successfully: {compressed_filename}")
        return compressed_filename
    except Exception as e:
        print(f"Error compressing file: {e}")
        return None


# Function to decompress a text file using Run-Length Encoding
def decompress_file(compressed_filename):
    try:
        # Verify the input file exists
        if not os.path.isfile(compressed_filename):
            print(f"Error: File '{compressed_filename}' not found!")
            return None

        # Prepare output filename
        decompressed_filename = f"{os.path.splitext(compressed_filename)[0]}_decompressed.txt"

        # Decompress the file
        with open(compressed_filename, 'r') as input_file, open(decompressed_filename, 'w') as output_file:
            while True:
                current_char = input_file.read(1)
                if not current_char:
                    break
                count = ''
                while True:
                    next_char = input_file.read(1)
                    if not next_char or not next_char.isdigit():
                        break
                    count += next_char
                count = int(count) if count else 1
                output_file.write(current_char * count)

        print(f"File decompressed successfully: {decompressed_filename}")
        return decompressed_filename
    except Exception as e:
        print(f"Error decompressing file: {e}")
        return None


# Function to calculate the compression ratio
def calculate_compression_ratio(original_filename, compressed_filename):
    try:
        original_size = os.path.getsize(original_filename)
        compressed_size = os.path.getsize(compressed_filename)

        if original_size > 0 and compressed_size > 0:
            ratio = original_size / compressed_size
            percentage = ((original_size - compressed_size) / original_size) * 100
            print(f"Compression Ratio: {ratio:.2f}")
            print(f"Compression Percentage: {percentage:.2f}%")
        else:
            print("Error: File sizes are invalid.")
    except Exception as e:
        print(f"Error calculating compression ratio: {e}")


# Function to compress an image file using ImageMagick
def compress_image_file(input_file):
    try:
        # Verify the input file exists
        if not os.path.isfile(input_file):
            print(f"Error: File '{input_file}' not found! Exiting.")
            return None

        # Prepare output filename
        compressed_filename = f"{os.path.splitext(input_file)[0]}_compressed.jpg"

        # Compress the image using ImageMagick
        result = subprocess.run(
            ['convert', input_file, '-resize', '50%', compressed_filename],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"Image '{input_file}' compressed successfully as '{compressed_filename}'.")
            return compressed_filename
        else:
            print(f"Error compressing image: {result.stderr}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Main function
def main():
    print("File Compression Utility")
    print("1. Text file compression (Run-Length Encoding)")
    print("2. Text file decompression (Run-Length Encoding)")
    print("3. Image file compression (Lossy)")

    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        input_filename = input("Enter the path of the text file to compress: ").strip()
        compressed_filename = compress_file(input_filename)
        if compressed_filename:
            calculate_compression_ratio(input_filename, compressed_filename)
    elif choice == '2':
        compressed_filename = input("Enter the path of the compressed file to decompress: ").strip()
        decompress_file(compressed_filename)
    elif choice == '3':
        input_file = input("Enter the path of the image file to compress: ").strip()
        compress_image_file(input_file)
    else:
        print("Invalid choice! Exiting...")


if __name__ == "__main__":
    main()

