import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import io

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def process_image(image_file):
    """Process uploaded image and identify medicine using Google Gemini Vision API"""
    
    # Read image
    image_data = image_file.read()
    image = Image.open(io.BytesIO(image_data))
    
    # Use Gemini 2.5 Flash model (supports vision)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = """Identify this medicine from the image. Provide:
1. Medicine name (generic and brand if visible)
2. Active ingredient(s)
3. Common dosage form (tablet, capsule, syrup, etc.)

Be precise and concise."""
    
    response = model.generate_content([prompt, image])
    medicine_name = response.text.strip()
    return medicine_name
