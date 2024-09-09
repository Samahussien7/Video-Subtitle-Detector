import cv2
import numpy as np

def create_directories(base_directory, subfolders):
    for subfolder in subfolders:
        path = os.path.join(base_directory, subfolder)
        os.makedirs(path, exist_ok=True)
        print(f"Directory created or already exists: {path}")

def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
    return gray, blurred, binary
