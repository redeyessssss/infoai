# Medicine AI - Image Recognition System

AI-powered medicine identification system that recognizes medicines from images and provides detailed information.

## Features

- 📸 Upload or capture medicine images
- 🔍 AI-powered medicine recognition using Google Gemini
- 📋 Detailed medicine information (uses, dosage, side effects, etc.)
- 🌍 Works with medicines from anywhere in the world
- 💊 Professional UI with organized information cards

## Setup

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Add your Google Gemini API key to `.env`:
```
GEMINI_API_KEY=your_actual_api_key_here
```

Get a FREE API key at: https://aistudio.google.com/app/apikey

6. Run the server:
```bash
python app.py
```

### Frontend Setup

1. Open `frontend/index.html` in a browser, or serve it:
```bash
cd frontend
python3 -m http.server 8000
```

2. Visit `http://localhost:8000`

## Usage

1. Click "Upload Image" to select a medicine photo or "Capture Photo" to use your camera
2. Click "Analyze Medicine" to process the image
3. View detailed information about the identified medicine

## API Endpoints

- `POST /api/analyze` - Analyze medicine image
- `GET /health` - Check server status

## Requirements

- Python 3.8+
- Google Gemini API key (FREE)
- Modern web browser with camera access

## Note

This is for informational purposes only. Always consult healthcare professionals for medical advice.
