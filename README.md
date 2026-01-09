# Pothole Prediction API

A Flask-based REST API for pothole prediction.

## Project Structure

```
Pothole Prediction/
├── app/
│   ├── __init__.py       # App initialization
│   ├── routes.py         # API endpoints
│   ├── models.py         # Data models
│   ├── config.py         # Configuration
│   └── utils.py          # Utility functions
├── models/               # ML models (create this folder)
├── uploads/              # Uploaded files (create this folder)
├── server.py             # Main entry point
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python server.py
```

## API Endpoints

- `GET /` - Welcome message
- `GET /api/health` - Health check
- `POST /api/predict` - Prediction endpoint (accepts JSON data)

## Example Request

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"latitude": 13.7563, "longitude": 100.5018}'
```
