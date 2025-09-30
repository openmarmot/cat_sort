'''
repo : https://github.com/openmarmot/cat_sort
email : andrew@openmarmot.com
notes :
takes pictures with laptop camera and sends to server
'''

import cv2
import requests
import time
import io

# Prompt for server IP
server_ip = input("Enter the server IP address: ")
SERVER_URL = f'http://{server_ip}:5000/upload'

# Capture interval in seconds
INTERVAL = 30  # Adjust as needed

cap = cv2.VideoCapture(0)  # 0 for default webcam
success_count=0
fail_count=0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    
    # Encode image to bytes
    _, buffer = cv2.imencode('.jpg', frame)
    img_bytes = io.BytesIO(buffer)
    
    # Send to server
    try:
        response = requests.post(SERVER_URL, files={'image': ('image.jpg', img_bytes, 'image/jpeg')})
        if response.status_code == 200:
            success_count+=1
            print("Image sent successfully")
        else:
            fail_count+=1
            print(f"Failed to send: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print(f'success: {success_count}',f'fail: {fail_count}')
    time.sleep(INTERVAL)

cap.release()