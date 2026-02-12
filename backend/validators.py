"""
Input validation utilities
"""
from typing import Dict, Tuple


def validate_health_metrics(metrics: Dict) -> Tuple[bool, str]:
    """
    Validate health metrics for realistic ranges
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    
    # Age validation
    if not (0 <= metrics.get('age', -1) <= 120):
        return False, "Age must be between 0 and 120 years"
    
    # Weight validation
    if not (20 <= metrics.get('weight', 0) <= 500):
        return False, "Weight must be between 20 and 500 kg"
    
    # Height validation
    if not (50 <= metrics.get('height', 0) <= 300):
        return False, "Height must be between 50 and 300 cm"
    
    # Cholesterol validation
    if not (0 <= metrics.get('cholesterol_level', -1) <= 500):
        return False, "Cholesterol level must be between 0 and 500 mg/dL"
    
    # Blood pressure validation
    bp = metrics.get('blood_pressure', '')
    try:
        parts = bp.split('/')
        if len(parts) != 2:
            return False, "Blood pressure must be in format 'systolic/diastolic'"
        
        systolic = int(parts[0])
        diastolic = int(parts[1])
        
        if not (50 <= systolic <= 250):
            return False, "Systolic pressure must be between 50 and 250"
        if not (30 <= diastolic <= 150):
            return False, "Diastolic pressure must be between 30 and 150"
        if systolic <= diastolic:
            return False, "Systolic pressure must be greater than diastolic"
            
    except:
        return False, "Invalid blood pressure format"
    
    # Lifestyle info validation
    if not metrics.get('lifestyle_info') or len(metrics.get('lifestyle_info', '')) < 10:
        return False, "Lifestyle information is required and must be descriptive"
    
    return True, "Valid"


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI from weight (kg) and height (cm)"""
    height_m = height / 100
    return weight / (height_m ** 2)


def parse_blood_pressure(bp_string: str) -> Tuple[int, int]:
    """Parse blood pressure string into systolic and diastolic values"""
    parts = bp_string.split('/')
    return int(parts[0]), int(parts[1])


def get_risk_category(score: float) -> str:
    """Categorize risk score into Low, Moderate, or High"""
    if score < 30:
        return "Low"
    elif score < 60:
        return "Moderate"
    else:
        return "High"
