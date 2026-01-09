from requests import post
from flask import Flask, request, jsonify
import os
from app import app
from app.utils import matchingImage, predictPothole
from io import BytesIO
from PIL import Image

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to Pothole Prediction API',
        'version': '1.0.0'
    })

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

@app.route('/api/predict', methods=['POST'])
def predict():
    """Prediction endpoint"""
    print(request)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    img = Image.open(BytesIO(request.files['file'].read()))
    predictResult = predictPothole(img)  # Replace None with actual model if needed
    return predictResult

@app.route('/api/upload', methods=['POST'])
def create_upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
            
        # Create uploads directory if it doesn't exist
        os.makedirs('uploads', exist_ok=True)
        
        file.save(f"uploads/{file.filename}")
        return jsonify({"filename": file.filename})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
@app.route('/api/match', methods=['POST'])
def match(): 
    print(request)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    print(request.files)
    img = Image.open(BytesIO(request.files['file'].read())).convert("RGB")
    template_image = Image.open(BytesIO(request.files['template'].read())).convert("RGB")
    matchResult = matchingImage(img,template_image)
    return jsonify({'match': matchResult})