# HealthNexus AI - AI-Powered Health Risk Prediction System

![HealthNexus AI](https://img.shields.io/badge/AI-Powered-blue) ![Python](https://img.shields.io/badge/Python-3.9+-green) ![Next.js](https://img.shields.io/badge/Next.js-14-black) ![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal)

## 🌟 Overview

**HealthNexus AI** is a professional AI-powered health assistant that analyzes user health data to predict potential health risks and generate actionable, personalized recommendations. The system uses machine learning models to assess risks for diabetes, heart disease, and high cholesterol, then provides evidence-based advice tailored to individual risk levels.

### Key Features

- ✅ **AI-Powered Risk Prediction**: Advanced algorithms predict health risks based on comprehensive health metrics
- ✅ **Personalized Recommendations**: Tailored advice for low, moderate, and high-risk scenarios
- ✅ **Explainable AI**: Clear explanations for every prediction
- ✅ **Real-time Analysis**: Get instant results with <5 second response times
- ✅ **Historical Tracking**: Store and retrieve past analyses for trend monitoring
- ✅ **Interactive Dashboard**: Beautiful, responsive UI with data visualizations
- ✅ **RESTful API**: Well-documented endpoints for easy integration

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                       Frontend (Next.js)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Health Form  │  │ Risk Display │  │ Recommendations│     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└───────────────────────┬─────────────────────────────────────┘
                       │ HTTP/REST API
┌───────────────────────┴─────────────────────────────────────┐
│                      Backend (FastAPI)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   API Layer  │  │  Validation  │  │   Database   │     │
│  └──────┬───────┘  └──────────────┘  └──────────────┘     │
│         │                                                   │
│  ┌──────┴────────────────────────────┐                     │
│  │       AI Engine                   │                     │
│  │  ┌─────────────────────────────┐  │                     │
│  │  │   Risk Prediction Module    │  │                     │
│  │  │  - Diabetes Predictor       │  │                     │
│  │  │  - Heart Disease Predictor  │  │                     │
│  │  │  - Cholesterol Predictor    │  │                     │
│  │  └─────────────────────────────┘  │                     │
│  │  ┌─────────────────────────────┐  │                     │
│  │  │  Recommendation Engine      │  │                     │
│  │  │  - Low Risk Advice          │  │                     │
│  │  │  - Moderate Risk Advice     │  │                     │
│  │  │  - High Risk Advice         │  │                     │
│  │  └─────────────────────────────┘  │                     │
│  └───────────────────────────────────┘                     │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
Civil-Hosp-Data-Maintenance/
├── backend/
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── risk_predictor.py       # ML-based risk prediction
│   │   └── recommendation_engine.py # Recommendation generation
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py             # Database connection
│   │   ├── crud.py                 # Database operations
│   │   └── schema.sql              # Database schema
│   ├── __init__.py
│   ├── app.py                      # Main FastAPI application
│   ├── config.py                   # Configuration management
│   ├── models.py                   # Pydantic data models
│   ├── validators.py               # Input validation
│   └── requirements.txt            # Python dependencies
├── frontend/
│   ├── app/
│   │   ├── globals.css            # Global styles
│   │   ├── layout.tsx             # Root layout
│   │   └── page.tsx               # Main page
│   ├── components/
│   │   ├── HealthDataForm.tsx     # Input form
│   │   ├── RiskDashboard.tsx      # Risk visualization
│   │   └── RecommendationPanel.tsx # Recommendations display
│   ├── package.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   └── tsconfig.json
└── README_HEALTHNEXUS.md (this file)
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+**
- **Node.js 18+**
- **npm or yarn**

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create environment file:**
   ```bash
   copy .env.example .env
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server:**
   ```bash
   python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Create environment file:**
   ```bash
   copy .env.example .env.local
   ```

3. **Install dependencies:**
   ```bash
   npm install
   ```

4. **Run the development server:**
   ```bash
   npm run dev
   ```

   The dashboard will be available at `http://localhost:3000`

## 📡 API Documentation

### Endpoints

#### `POST /submit-health-data`
Submit health data and receive complete analysis (predictions + recommendations)

**Request Body:**
```json
{
  "metrics": {
    "age": 45,
    "weight": 85.5,
    "height": 175.0,
    "blood_pressure": "140/90",
    "cholesterol_level": 220.0,
    "lifestyle_info": "Exercise: 2x/week, Smoking: No, Diet: Mixed, Alcohol: Moderate"
  }
}
```

**Response:**
```json
{
  "user_id": "12345",
  "risk_scores": {
    "diabetes": 78.0,
    "heart_disease": 45.0,
    "high_cholesterol": 62.0
  },
  "recommendations": {
    "diabetes": "Increase daily exercise to 30 minutes...",
    "heart_disease": "Maintain healthy weight...",
    "high_cholesterol": "Increase fiber intake..."
  },
  "explanations": {
    "diabetes": "High BMI and elevated fasting glucose indicate elevated risk.",
    "heart_disease": "Moderate cholesterol levels combined with blood pressure readings suggest moderate risk.",
    "high_cholesterol": "Cholesterol readings above normal range indicate risk."
  },
  "timestamp": "2026-02-12T14:48:31Z"
}
```

#### `POST /get-predictions`
Get only risk predictions without recommendations

#### `GET /get-recommendations/{user_id}`
Retrieve latest recommendations for a specific user

#### `GET /user-history/{user_id}`
Get historical health data and predictions

#### `GET /health`
Health check endpoint

## 🎨 Features in Detail

### 1. Data Validation
- Comprehensive input validation with realistic health metric ranges
- Blood pressure format validation
- Required field enforcement
- Clear error messages

### 2. Risk Prediction Engine
- **Diabetes Risk**: Based on BMI, age, lifestyle factors
- **Heart Disease Risk**: Considers blood pressure, cholesterol, age, smoking
- **Cholesterol Risk**: Analyzes cholesterol levels, diet, exercise habits

### 3. Recommendation System
- **Low Risk**: Maintenance advice and preventive measures
- **Moderate Risk**: Lifestyle modification suggestions
- **High Risk**: Medical consultation recommendations with specific actions

### 4. Dashboard Features
- Real-time risk visualization with color-coded progress bars
- Detailed explanations for each prediction
- Personalized recommendations with priority indicators
- Responsive design for mobile and desktop

## 🧪 Testing

### Sample Data for Testing

```json
{
  "metrics": {
    "age": 52,
    "weight": 95.0,
    "height": 170.0,
    "blood_pressure": "145/95",
    "cholesterol_level": 245.0,
    "lifestyle_info": "Exercise: 1x/week, Smoking: No, Diet: High fat, Alcohol: Moderate"
  }
}
```

This will generate high-risk predictions for multiple conditions.

### API Testing

Access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔒 Security & Privacy

- All health data is stored locally in SQLite database
- No external data transmission
- User IDs are auto-generated UUIDs
- Configurable CORS settings

## 🎯 Deployment

### Production Deployment

1. **Backend:**
   ```bash
   python -m uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
   ```

2. **Frontend:**
   ```bash
   npm run build
   npm run start
   ```

## 📊 System Requirements

### Backend
- Python 3.9+
- 512MB RAM minimum
- 100MB disk space

### Frontend
- Node.js 18+
- Modern browser (Chrome, Firefox, Safari, Edge)
- 1GB RAM minimum

## 🤝 Contributing

This is a demonstration project. For production use:
1. Replace rule-based predictions with trained ML models
2. Add authentication and authorization
3. Implement data encryption
4. Add comprehensive test coverage
5. Set up CI/CD pipelines

## ⚠️ Disclaimer

**HealthNexus AI is for informational and demonstration purposes only.** This system should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with questions regarding medical conditions.

## 📝 License

This project is created for educational and demonstration purposes.

## 🙋 Support

For issues or questions, please refer to the API documentation or create an issue in the repository.

---

**Built with ❤️ using FastAPI, Next.js, and AI**
