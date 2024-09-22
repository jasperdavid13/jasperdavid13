from PIL import Image
import os

# Define the folder containing images and the target size
input_folder = "C:\\Users\\NALINI\\Desktop\\images backup\\200x200\\All brands misc"  # Replace with your folder path
output_folder = "C:\\Users\\NALINI\\Desktop\\images backup\\200x200\\All brands misc\\logos 200x200"  # Replace with your output folder path
target_size = (362, 446)
output_format = 'JPEG'  # Desired output format: 'JPEG', 'PNG', etc.

# Create the output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Check for image file extensions
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            # Convert image to RGB if it has an alpha channel (transparency) or is in palette mode
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Resize the image to the target size by stretching
            img_resized = img.resize(target_size)

            # Define the output file path with the desired format extension
            output_filename = os.path.splitext(filename)[0] + '.' + output_format.lower()
            output_path = os.path.join(output_folder, output_filename)

            # Save the resized image in the specified format
            img_resized.save(output_path, format=output_format)

print("Resizing and stretching completed successfully!")
