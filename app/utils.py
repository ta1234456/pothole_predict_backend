# Utility functions
from tkinter import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
import base64
import json
from ultralytics import YOLO
import os

model = YOLO("app/model/bestNew32_1.pt")
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
    print(image_path)

    results = model.predict(
        image_path,
        conf=0.8,
        save=False,
        show=False,
        project="results"
    )
    
    if results and len(results[0].boxes) > 0:

        plotted = results[0].plot()

        _, buffer = cv2.imencode(".jpg", plotted)

        image_base64 = base64.b64encode(buffer).decode("utf-8")

        # confidence = float(results[0].boxes[0].conf[0])

        print("Pothole detected")
        return json.dumps({"pothole": True, "image": image_base64})

    return(json.dumps({"pothole": False})) 

    # if not os.path.exists(image_path):
    #     return json.dumps({
    #         "error": "Image not found"
    #     })
    # else :
    #     results = model.predict(
    #         image_path,  # Replace with your image path
    #         conf=0.5,  # Confidence threshold
    #         save=False,
    #         show=False,  # Set to True if you want to display the image
    #         project="results"  # Directory to save results
    #     )          
    #     if results and len(results[0].boxes) > 0:
    #         _, buffer = cv2.imencode(".jpg", results[0].plot())
    #         buffer = base64.b64encode(buffer).decode("utf-8")
    #         print("Pothole detected")
    #         return(json.dumps({"pothole": True,"image": buffer}))  # Return "yes" if pothole is detected along with annotated image
    #     else:
    #         print("No pothole detected")
    #         return(json.dumps({"pothole": False}))  # Return "no" if no pothole is detected