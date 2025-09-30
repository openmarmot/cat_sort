'''
repo : https://github.com/openmarmot/cat_sort
email : andrew@openmarmot.com
notes :
receives, classifies, and saves images
'''

from flask import Flask, request
from ultralytics import YOLO
import cv2
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)

# Load YOLO model (download weights automatically on first run)
model = YOLO('yolo11n.pt')  # Nano version for speed; 

# Directory to save cat images
SAVE_DIR = 'cat_images'
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No image file", 400
    
    file = request.files['image']
    img_bytes = file.read()
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Run YOLO detection
    results = model(img, device=0)  # Use GPU
    
    # Check if 'cat' class is detected (class ID 15 in COCO)
    # https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml
    for r in results:
        boxes = r.boxes
        for box in boxes:
            if int(box.cls) == 15:  # 15 is 'cat'
                # Save image if cat detected
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                save_path = os.path.join(SAVE_DIR, f'cat_{timestamp}.jpg')
                cv2.imwrite(save_path, img)
                return "Cat detected and saved", 200
    
    return "No cat detected", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)