# built in
import os
import shutil
import uuid

# external
from ultralytics import YOLO
import cv2 # from opencv-python package

# Prompt for input folder
input_folder = input("Enter the path to the input folder: ").strip()

# Load YOLO model (uses GPU if available)
model = YOLO('yolo11m.pt')  # m model for greater accuracy

# Create output folder with random suffix in the current working directory
suffix = str(uuid.uuid4())[:8]  # Short random suffix
output_folder = f'output_{suffix}'
os.makedirs(output_folder, exist_ok=True)

# Create subfolders
match_folder = os.path.join(output_folder, 'match')
rejected_folder = os.path.join(output_folder, 'rejected')
os.makedirs(match_folder, exist_ok=True)
os.makedirs(rejected_folder, exist_ok=True)

# Print the output folder name
print(f"Output folder created: {output_folder}")

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Support common image formats
        img_path = os.path.join(input_folder, filename)
        
        # Load image
        img = cv2.imread(img_path)
        if img is None:
            print(f"Skipping invalid image: {filename}")
            continue
        
        # Run YOLO detection
        results = model(img)
        
        # Check for person (COCO class 0)
        has_person = False
        for r in results:
            boxes = r.boxes
            for box in boxes:
                if int(box.cls) == 0:
                    has_person = True
                    break
            if has_person:
                break
        
        # Copy to appropriate folder
        if has_person:
            shutil.copy(img_path, os.path.join(match_folder, filename))
            print(f"Copied {filename} to match (person detected)")
        else:
            shutil.copy(img_path, os.path.join(rejected_folder, filename))
            print(f"Copied {filename} to rejected (no person detected)")

print("Processing complete.")