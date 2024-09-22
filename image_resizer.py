from PIL import Image, ImageOps
import os

# Define the folder containing images and the target size
input_folder = "C:\\Users\\NALINI\\Desktop\\Brookfield"  # Replace with your folder path
output_folder = "C:\\Users\\NALINI\\Desktop\\drive upload 200x200\\Brookfield" # Replace with your output folder path
target_size = (200, 200)
output_format = 'JPEG'  # Desired output format: 'JPEG', 'PNG', etc.

# Create the output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Check for image file extensions
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            # Calculate the aspect ratio
            aspect_ratio = img.width / img.height
            target_aspect_ratio = target_size[0] / target_size[1]

            # Resize and pad the image accordingly
            if aspect_ratio > target_aspect_ratio:  # Image is wider
                img = ImageOps.pad(img, target_size, method=Image.Resampling.LANCZOS, color='white')
            else:  # Image is taller or the same aspect ratio
                img = ImageOps.fit(img, target_size, method=Image.Resampling.LANCZOS)

            # Convert image to RGB if it has an alpha channel (transparency) or is in palette mode
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            # Define the output file path with the desired format extension
            output_filename = os.path.splitext(filename)[0] + '.' + output_format.lower()
            output_path = os.path.join(output_folder, output_filename)

            # Save the resized image in the specified format
            img.save(output_path, format=output_format)

print("Resizing, padding, and format conversion completed successfully!")
