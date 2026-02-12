"""
Configuration module for HealthNexus AI
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""
    
    # API Settings
    API_TITLE: str = "HealthNexus AI API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "AI-powered health risk prediction and recommendation system"
    
    # Database Settings
    DATABASE_URL: str = "sqlite:///./healthnexus.db"
    
    # Model Settings
    MODEL_PATH: str = "./ai/models"
    
    # CORS Settings
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:3001"]
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Risk Thresholds
    LOW_RISK_THRESHOLD: float = 30.0
    MODERATE_RISK_THRESHOLD: float = 60.0
    HIGH_RISK_THRESHOLD: float = 100.0
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
