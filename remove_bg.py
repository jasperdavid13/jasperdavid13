import os
from rembg import remove
from PIL import Image

# Paths for the input and output folders
input_folder_path = 'input_folder'
output_folder_path = 'output_folder'

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder_path):
    # Full path to the image file
    input_image_path = os.path.join(input_folder_path, filename)
    
    # Check if the file is an image (you can add more extensions if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Open the image file
        with Image.open(input_image_path) as img:
            # Remove the background
            output_image = remove(img)
            
            # Define the path for the output image
            output_image_path = os.path.join(output_folder_path, filename)
            
            # Save the result
            output_image.save(output_image_path)
            print(f'Processed {filename} and saved to {output_image_path}')
    else:
        print(f'Skipped {filename} (not an image)')

print('Processing complete!')
