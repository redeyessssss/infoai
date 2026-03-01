from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from io import BytesIO
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def process_image_inline(image_file):
    """Process uploaded image and identify medicine"""
    try:
        # Read image
        image_data = image_file.read()
        image = Image.open(BytesIO(image_data))
        
        # Use Gemini model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = """Identify this medicine from the image. Provide:
1. Medicine name (generic and brand if visible)
2. Active ingredient(s)
3. Common dosage form (tablet, capsule, syrup, etc.)

Be precise and concise."""
        
        response = model.generate_content([prompt, image])
        medicine_name = response.text.strip()
        return medicine_name
    except Exception as e:
        raise Exception(f"Image processing error: {str(e)}")

def get_medicine_details_inline(medicine_name):
    """Get comprehensive medicine information"""
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""Provide detailed information about this medicine: {medicine_name}

Include the following in JSON format:
- generic_name: Generic/scientific name
- brand_names: Common brand names (array)
- active_ingredients: Active ingredients (array)
- uses: Medical uses and indications (array)
- dosage: Typical dosage information
- side_effects: Common side effects (array)
- precautions: Important precautions and warnings (array)
- interactions: Drug interactions to be aware of
- storage: Storage instructions

Return ONLY valid JSON, no markdown formatting."""
        
        response = model.generate_content(prompt)
        
        # Clean response text
        text = response.text.strip()
        if text.startswith('```json'):
            text = text[7:]
        if text.startswith('```'):
            text = text[3:]
        if text.endswith('```'):
            text = text[:-3]
        text = text.strip()
        
        details = json.loads(text)
        details['identified_medicine'] = medicine_name
        return details
    except json.JSONDecodeError:
        return {
            'identified_medicine': medicine_name,
            'generic_name': 'Information retrieved',
            'description': response.text,
            'note': 'Please consult a healthcare professional for accurate information'
        }
    except Exception as e:
        raise Exception(f"Medicine info error: {str(e)}")

@app.route('/api/analyze', methods=['POST', 'OPTIONS'])
def analyze():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
    try:
        # Check for API key
        if not os.getenv('GEMINI_API_KEY'):
            return jsonify({'error': 'API key not configured'}), 500
        
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        image = request.files['image']
        if image.filename == '':
            return jsonify({'error': 'No image selected'}), 400
        
        # Process image and identify medicine
        medicine_name = process_image_inline(image)
        
        # Get detailed information
        details = get_medicine_details_inline(medicine_name)
        
        return jsonify(details), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    api_key_set = bool(os.getenv('GEMINI_API_KEY'))
    return jsonify({
        'status': 'healthy',
        'api_key_configured': api_key_set
    }), 200

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Medicine AI API'}), 200
