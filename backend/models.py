"""
Pydantic models for data validation
"""
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict
from datetime import datetime


class HealthMetrics(BaseModel):
    """Basic health metrics input model"""
    
    age: int = Field(..., ge=0, le=120, description="Age in years")
    weight: float = Field(..., gt=0, le=500, description="Weight in kg")
    height: float = Field(..., gt=0, le=300, description="Height in cm")
    blood_pressure: str = Field(..., description="Blood pressure as systolic/diastolic (e.g., '120/80')")
    cholesterol_level: float = Field(..., ge=0, le=500, description="Cholesterol level in mg/dL")
    lifestyle_info: str = Field(..., description="Lifestyle information: exercise frequency, smoking, diet, alcohol")
    
    @validator('blood_pressure')
    def validate_blood_pressure(cls, v):
        """Validate blood pressure format"""
        try:
            parts = v.split('/')
            if len(parts) != 2:
                raise ValueError("Blood pressure must be in format 'systolic/diastolic'")
            
            systolic = int(parts[0])
            diastolic = int(parts[1])
            
            if not (50 <= systolic <= 250):
                raise ValueError("Systolic pressure must be between 50 and 250")
            if not (30 <= diastolic <= 150):
                raise ValueError("Diastolic pressure must be between 30 and 150")
            
            return v
        except Exception as e:
            raise ValueError(f"Invalid blood pressure format: {str(e)}")
    
    class Config:
        json_schema_extra = {
            "example": {
                "age": 45,
                "weight": 85.5,
                "height": 175.0,
                "blood_pressure": "140/90",
                "cholesterol_level": 220.0,
                "lifestyle_info": "Exercise: 2x/week, Smoking: No, Diet: Mixed, Alcohol: Moderate"
            }
        }


class HistoricalData(BaseModel):
    """Optional historical health data"""
    
    previous_tests: Optional[Dict] = Field(default=None, description="Previous test results")
    past_diagnoses: Optional[list] = Field(default=None, description="Past medical diagnoses")
    trend_data: Optional[Dict] = Field(default=None, description="Historical vital trends")


class HealthDataInput(BaseModel):
    """Combined health data input"""
    
    user_id: Optional[str] = Field(default=None, description="User identifier")
    metrics: HealthMetrics
    historical: Optional[HistoricalData] = None


class RiskScore(BaseModel):
    """Individual risk score"""
    
    condition: str
    probability: float = Field(..., ge=0, le=100, description="Risk probability (0-100%)")
    explanation: str
    risk_level: str = Field(..., description="Low, Moderate, or High")


class RiskScores(BaseModel):
    """Risk prediction output"""
    
    user_id: str
    timestamp: datetime
    risk_scores: Dict[str, float] = Field(..., description="Condition -> probability mapping")
    explanations: Dict[str, str] = Field(..., description="Condition -> explanation mapping")
    risk_levels: Dict[str, str] = Field(..., description="Condition -> risk level mapping")


class Recommendation(BaseModel):
    """Individual recommendation"""
    
    condition: str
    advice: str
    confidence_level: Optional[float] = Field(default=None, ge=0, le=100)
    actions: list[str]


class Recommendations(BaseModel):
    """Recommendation output"""
    
    user_id: str
    timestamp: datetime
    recommendations: Dict[str, str] = Field(..., description="Condition -> advice mapping")
    confidence_levels: Optional[Dict[str, float]] = None


class HealthResponse(BaseModel):
    """Complete health analysis response"""
    
    user_id: str
    risk_scores: Dict[str, float]
    recommendations: Dict[str, str]
    explanations: Dict[str, str]
    timestamp: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "12345",
                "risk_scores": {
                    "diabetes": 78.0,
                    "heart_disease": 45.0,
                    "high_cholesterol": 62.0
                },
                "recommendations": {
                    "diabetes": "Increase daily exercise to 30 minutes, reduce sugar intake, monitor blood glucose weekly.",
                    "heart_disease": "Maintain healthy weight, check blood pressure monthly, reduce saturated fats.",
                    "high_cholesterol": "Increase fiber intake, limit fried foods, consult doctor for cholesterol-lowering medication."
                },
                "explanations": {
                    "diabetes": "High BMI and elevated fasting glucose indicate elevated risk.",
                    "heart_disease": "Moderate cholesterol levels combined with blood pressure readings suggest moderate risk.",
                    "high_cholesterol": "Cholesterol readings above normal range indicate risk."
                },
                "timestamp": "2026-02-12T14:48:31Z"
            }
        }
