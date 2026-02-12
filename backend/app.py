"""
HealthNexus AI - Main FastAPI Application
Professional AI-powered health risk prediction system
"""
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uuid
import logging

from config import settings
from models import HealthDataInput, HealthResponse
from validators import validate_health_metrics, calculate_bmi, get_risk_category
from ai.risk_predictor import risk_predictor
from ai.recommendation_engine import recommendation_engine
from db.database import init_db
from db.crud import db_crud

# Configure logging
logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description=settings.API_DESCRIPTION
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    logger.info("Initializing HealthNexus AI API...")
    init_db()
    logger.info("Database initialized successfully")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to HealthNexus AI",
        "version": settings.API_VERSION,
        "description": "AI-powered health risk prediction and recommendation system"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


@app.post("/submit-health-data", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def submit_health_data(data: HealthDataInput):
    """
    Submit health data and receive risk predictions with recommendations
    
    This endpoint combines data submission, prediction, and recommendation generation
    in a single call for convenience.
    """
    try:
        # Generate user_id if not provided
        user_id = data.user_id or str(uuid.uuid4())
        
        # Extract metrics
        metrics = data.metrics.model_dump()
        
        # Validate metrics
        is_valid, error_msg = validate_health_metrics(metrics)
        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Validation error: {error_msg}"
            )
        
        # Calculate BMI
        bmi = calculate_bmi(metrics['weight'], metrics['height'])
        
        # Save health data to database
        data_id = db_crud.save_health_data(user_id, metrics, bmi)
        if not data_id:
            logger.warning("Failed to save health data to database")
        
        # Get risk predictions
        predictions = risk_predictor.predict_all_risks(metrics)
        risk_scores = predictions['risk_scores']
        explanations = predictions['explanations']
        
        # Add risk levels
        risk_levels = {
            condition: get_risk_category(score)
            for condition, score in risk_scores.items()
        }
        
        # Save predictions to database
        prediction_id = db_crud.save_predictions(user_id, risk_scores, explanations)
        
        # Generate recommendations
        recommendations = recommendation_engine.generate_recommendations(risk_scores)
        
        # Save recommendations to database
        if prediction_id:
            db_crud.save_recommendations(user_id, prediction_id, recommendations)
        
        # Prepare response
        response = HealthResponse(
            user_id=user_id,
            risk_scores=risk_scores,
            recommendations=recommendations,
            explanations=explanations,
            timestamp=datetime.now()
        )
        
        logger.info(f"Successfully processed health data for user {user_id}")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing health data: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@app.post("/get-predictions")
async def get_predictions(data: HealthDataInput):
    """
    Get risk predictions for provided health data
    
    Returns only predictions without recommendations
    """
    try:
        # Generate user_id if not provided
        user_id = data.user_id or str(uuid.uuid4())
        
        # Extract metrics
        metrics = data.metrics.model_dump()
        
        # Validate metrics
        is_valid, error_msg = validate_health_metrics(metrics)
        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Validation error: {error_msg}"
            )
        
        # Get risk predictions
        predictions = risk_predictor.predict_all_risks(metrics)
        risk_scores = predictions['risk_scores']
        explanations = predictions['explanations']
        
        # Add risk levels
        risk_levels = {
            condition: get_risk_category(score)
            for condition, score in risk_scores.items()
        }
        
        return {
            "user_id": user_id,
            "risk_scores": risk_scores,
            "explanations": explanations,
            "risk_levels": risk_levels,
            "timestamp": datetime.now().isoformat()
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting predictions: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@app.get("/get-recommendations/{user_id}")
async def get_recommendations(user_id: str):
    """
    Get latest recommendations for a user
    
    Retrieves the most recent analysis and recommendations from the database
    """
    try:
        # Get latest analysis
        analysis = db_crud.get_latest_analysis(user_id)
        
        if not analysis:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No analysis found for user {user_id}"
            )
        
        # Prepare response
        return {
            "user_id": user_id,
            "risk_scores": {
                "diabetes": analysis['diabetes_risk'],
                "heart_disease": analysis['heart_disease_risk'],
                "high_cholesterol": analysis['cholesterol_risk']
            },
            "recommendations": {
                "diabetes": analysis['diabetes_recommendation'],
                "heart_disease": analysis['heart_disease_recommendation'],
                "high_cholesterol": analysis['cholesterol_recommendation']
            },
            "explanations": {
                "diabetes": analysis['diabetes_explanation'],
                "heart_disease": analysis['heart_disease_explanation'],
                "high_cholesterol": analysis['cholesterol_explanation']
            },
            "timestamp": analysis['created_at']
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting recommendations: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@app.get("/user-history/{user_id}")
async def get_user_history(user_id: str, limit: int = 10):
    """
    Get user's health data and prediction history
    
    Returns historical data for trend analysis
    """
    try:
        health_history = db_crud.get_user_history(user_id, limit)
        prediction_history = db_crud.get_user_predictions(user_id, limit)
        
        return {
            "user_id": user_id,
            "health_data": health_history,
            "predictions": prediction_history
        }
        
    except Exception as e:
        logger.error(f"Error getting user history: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
