import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def get_medicine_details(medicine_name):
    """Get comprehensive medicine information"""
    
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
    
    try:
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
        # Fallback if JSON parsing fails
        return {
            'identified_medicine': medicine_name,
            'generic_name': 'Information retrieved',
            'description': response.text,
            'note': 'Please consult a healthcare professional for accurate information'
        }
