from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from io import BytesIO
from PIL import Image

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import after path is set
try:
    from backend.utils.image_processor import process_image
    from backend.utils.medicine_info import get_medicine_details
except ImportError:
    # Fallback for Vercel
    import importlib.util
    
    # Load image_processor
    spec = importlib.util.spec_from_file_location(
        "image_processor",
        os.path.join(os.path.dirname(__file__), '..', 'backend', 'utils', 'image_processor.py')
    )
    image_processor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(image_processor)
    process_image = image_processor.process_image
    
    # Load medicine_info
    spec = importlib.util.spec_from_file_location(
        "medicine_info",
        os.path.join(os.path.dirname(__file__), '..', 'backend', 'utils', 'medicine_info.py')
    )
    medicine_info = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(medicine_info)
    get_medicine_details = medicine_info.get_medicine_details

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/analyze', methods=['POST', 'OPTIONS'])
def analyze():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        image = request.files['image']
        if image.filename == '':
            return jsonify({'error': 'No image selected'}), 400
        
        # Process image and identify medicine
        medicine_name = process_image(image)
        
        # Get detailed information
        details = get_medicine_details(medicine_name)
        
        return jsonify(details)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

# Vercel serverless function handler
def handler(event, context):
    return app(event, context)
