from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.image_processor import process_image
from utils.medicine_info import get_medicine_details

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/analyze', methods=['POST'])
def analyze_medicine():
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

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
