# Utility functions
from tkinter import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
import base64
import json
from ultralytics import YOLO

def matchingImage(current_image, template_image):
    # Set Image For Matching
    current_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_RGB2BGR)
    template_image = cv2.cvtColor(np.array(template_image), cv2.COLOR_RGB2BGR)
    # resize images to same size
    current_image = cv2.resize(current_image, (300, 300))
    template_image = cv2.resize(template_image, (300, 300))

    # Perform template matching
    res = cv2.matchTemplate(current_image, template_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  

    # Find locations where matching exceeds threshold
    loc = np.where(res >= threshold)
    match_found = len(loc[0]) > 0
    return match_found

def predictPothole(image_path):
    # Make prediction
    model = YOLO("app\\model\\best_d12_11_32.pt")  # Load a custom model
    print(image_path)
    results = model.predict(
        source=image_path,  # Replace with your image path
        conf=0.8,  # Confidence threshold
        save=False,  # Save the result with bounding boxes
        show=False,  # Set to True if you want to display the image
        project="results"  # Directory to save results
    )   
    if len(results[0].boxes) > 0:
        _, buffer = cv2.imencode(".jpg", results[0].plot())
        buffer = base64.b64encode(buffer).decode("utf-8")
        print("Pothole detected")
        return(json.dumps({"pothole": True,"image": buffer}))  # Return "yes" if pothole is detected along with annotated image
    else:
        print("No pothole detected")
        return(json.dumps({"pothole": False}))  # Return "no" if no pothole is detected