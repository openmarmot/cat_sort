import os
import uuid
import shutil
from PIL import Image
import imagehash
import cv2

# Prompt for input folder
input_folder = input("Enter the path to the input folder: ").strip()

# Create output folder with random suffix
suffix = str(uuid.uuid4())[:8]  # Short random suffix
output_folder = f'output_{suffix}'
os.makedirs(output_folder, exist_ok=True)

# Create subfolders
unique_folder = os.path.join(output_folder, 'unique')
duplicates_folder = os.path.join(output_folder, 'duplicates')
os.makedirs(unique_folder, exist_ok=True)
os.makedirs(duplicates_folder, exist_ok=True)

# Print output folder name
print(f"Output folder created: {output_folder}")

# Compute perceptual hash for an image
def get_image_hash(img_path):
    try:
        img = Image.open(img_path)
        return imagehash.phash(img)
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return None

# Threshold for considering images near-identical (Hamming distance)
SIMILARITY_THRESHOLD = 10  # Adjust after testing (0 = identical, higher = more different)

# Collect all image files
image_files = [
    f for f in os.listdir(input_folder)
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))
]

# Store hashes and their representative images
hashes = {}
unique_images = []
duplicate_images = []

# Process each image
for filename in image_files:
    img_path = os.path.join(input_folder, filename)
    img_hash = get_image_hash(img_path)
    
    if img_hash is None:
        print(f"Skipping invalid image: {filename}")
        continue
    
    # Compare with existing hashes
    is_duplicate = False
    for existing_hash, rep_filename in hashes.items():
        if img_hash - existing_hash <= SIMILARITY_THRESHOLD:
            is_duplicate = True
            duplicate_images.append(filename)
            shutil.copy(img_path, os.path.join(duplicates_folder, filename))
            print(f"Copied {filename} to duplicates (similar to {rep_filename})")
            break
    
    if not is_duplicate:
        unique_images.append(filename)
        hashes[img_hash] = filename
        shutil.copy(img_path, os.path.join(unique_folder, filename))
        print(f"Copied {filename} to unique")

print(f"Processing complete. {len(unique_images)} unique images, {len(duplicate_images)} duplicates.")