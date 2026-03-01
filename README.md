# Medicine AI - Image Recognition System

AI-powered medicine identification system that recognizes medicines from images and provides detailed information.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/redeyessssss/infoai)

## Features

- 📸 Upload or capture medicine images
- 🔍 AI-powered medicine recognition using Google Gemini
- 📋 Detailed medicine information (uses, dosage, side effects, etc.)
- 🌍 Works with medicines from anywhere in the world
- 💊 Professional UI with organized information cards
- ☁️ Deploy to Vercel with one click

## Live Demo

[View Demo](https://infoai.vercel.app) (after deployment)

## Quick Deploy to Vercel

1. Click the "Deploy with Vercel" button above
2. Connect your GitHub account
3. Add environment variable:
   - `GEMINI_API_KEY`: Your Google Gemini API key ([Get free key](https://aistudio.google.com/app/apikey))
4. Click Deploy

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## Local Development

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
- `GET /api/health` - Check server status

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **AI**: Google Gemini 2.5 Flash
- **Deployment**: Vercel (Serverless)

## Requirements

- Python 3.8+
- Google Gemini API key (FREE)
- Modern web browser with camera access

## Project Structure

```
infoai/
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── utils/
│       ├── image_processor.py  # Image handling
│       └── medicine_info.py    # Medicine data lookup
├── frontend/
│   ├── index.html          # Main UI
│   ├── style.css           # Styling
│   └── app.js              # Frontend logic
├── vercel.json             # Vercel configuration
├── DEPLOYMENT.md           # Deployment guide
└── README.md               # This file
```

## Environment Variables

- `GEMINI_API_KEY`: Google Gemini API key (required)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Disclaimer

⚠️ This information is for educational purposes only. Always consult healthcare professionals for medical advice. Do not use this tool as a substitute for professional medical advice.

## Support

For issues and questions, please open an issue on GitHub.
