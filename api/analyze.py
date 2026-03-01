from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from utils.image_processor import process_image
from utils.medicine_info import get_medicine_details

app = Flask(__name__)
CORS(app)

def handler(request):
    """Vercel serverless function handler"""
    if request.method == 'OPTIONS':
        return jsonify({}), 200
        
    if request.method != 'POST':
        return jsonify({'error': 'Method not allowed'}), 405
    
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    try:
        # Process image and identify medicine
        medicine_name = process_image(image)
        
        # Get detailed information
        details = get_medicine_details(medicine_name)
        
        return jsonify(details)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# For Vercel
if __name__ != '__main__':
    app = handler
