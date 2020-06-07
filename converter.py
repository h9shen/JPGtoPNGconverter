from PIL import Image, ImageFilter
import sys
import os

# Grab the input and output folder
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if output folder exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}', 'png')

print('all done!')
