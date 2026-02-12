"""
AI Risk Prediction Engine
Uses ML models and rule-based logic to predict health risks
"""
import numpy as np
from typing import Dict, Tuple
from validators import calculate_bmi, parse_blood_pressure


class RiskPredictor:
    """Health risk prediction engine"""
    
    def __init__(self):
        """Initialize the predictor with models"""
        # In a production system, load pre-trained models here
        # For demo purposes, we'll use rule-based predictions with ML-style scoring
        self.models_loaded = True
    
    def predict_diabetes_risk(self, metrics: Dict) -> Tuple[float, str]:
        """
        Predict diabetes risk
        
        Returns:
            Tuple of (risk_score, explanation)
        """
        age = metrics['age']
        weight = metrics['weight']
        height = metrics['height']
        bmi = calculate_bmi(weight, height)
        lifestyle = metrics['lifestyle_info'].lower()
        
        # Calculate risk score based on multiple factors
        risk_score = 0.0
        factors = []
        
        # BMI factor (0-30 points)
        if bmi >= 30:
            risk_score += 30
            factors.append("high BMI (≥30)")
        elif bmi >= 25:
            risk_score += 15
            factors.append("elevated BMI (25-30)")
        
        # Age factor (0-25 points)
        if age >= 45:
            risk_score += 25
            factors.append("age over 45")
        elif age >= 35:
            risk_score += 15
        
        # Lifestyle factors (0-30 points)
        if 'sedentary' in lifestyle or 'no exercise' in lifestyle or '0' in lifestyle:
            risk_score += 20
            factors.append("sedentary lifestyle")
        elif 'exercise: 1' in lifestyle or 'exercise: 2' in lifestyle:
            risk_score += 10
        
        if 'high sugar' in lifestyle or 'poor diet' in lifestyle:
            risk_score += 10
            factors.append("poor diet")
        
        # Family history (if mentioned)
        if 'family history' in lifestyle or 'diabetes' in lifestyle:
            risk_score += 15
            factors.append("family history of diabetes")
        
        # Generate explanation
        if risk_score >= 60:
            explanation = f"High risk due to: {', '.join(factors)}. BMI is {bmi:.1f}."
        elif risk_score >= 30:
            explanation = f"Moderate risk. Contributing factors: {', '.join(factors) if factors else 'age and BMI in moderate range'}. BMI is {bmi:.1f}."
        else:
            explanation = f"Low risk. BMI is {bmi:.1f} and lifestyle factors are favorable."
        
        return min(risk_score, 100.0), explanation
    
    def predict_heart_disease_risk(self, metrics: Dict) -> Tuple[float, str]:
        """
        Predict heart disease risk
        
        Returns:
            Tuple of (risk_score, explanation)
        """
        age = metrics['age']
        weight = metrics['weight']
        height = metrics['height']
        bmi = calculate_bmi(weight, height)
        cholesterol = metrics['cholesterol_level']
        bp_str = metrics['blood_pressure']
        systolic, diastolic = parse_blood_pressure(bp_str)
        lifestyle = metrics['lifestyle_info'].lower()
        
        risk_score = 0.0
        factors = []
        
        # Blood pressure factor (0-30 points)
        if systolic >= 140 or diastolic >= 90:
            risk_score += 30
            factors.append(f"high blood pressure ({bp_str})")
        elif systolic >= 130 or diastolic >= 85:
            risk_score += 15
            factors.append(f"elevated blood pressure ({bp_str})")
        
        # Cholesterol factor (0-25 points)
        if cholesterol >= 240:
            risk_score += 25
            factors.append(f"high cholesterol ({cholesterol} mg/dL)")
        elif cholesterol >= 200:
            risk_score += 12
            factors.append(f"borderline high cholesterol ({cholesterol} mg/dL)")
        
        # Age factor (0-20 points)
        if age >= 55:
            risk_score += 20
            factors.append("age over 55")
        elif age >= 45:
            risk_score += 10
        
        # Smoking (0-15 points)
        if 'smoking: yes' in lifestyle or 'smoker' in lifestyle:
            risk_score += 15
            factors.append("smoking")
        
        # BMI factor (0-10 points)
        if bmi >= 30:
            risk_score += 10
            factors.append("obesity")
        
        # Generate explanation
        if risk_score >= 60:
            explanation = f"High risk. Key factors: {', '.join(factors)}."
        elif risk_score >= 30:
            explanation = f"Moderate risk. Blood pressure {bp_str}, cholesterol {cholesterol} mg/dL indicate some concern."
        else:
            explanation = f"Low risk. Blood pressure and cholesterol levels are within healthy ranges."
        
        return min(risk_score, 100.0), explanation
    
    def predict_cholesterol_risk(self, metrics: Dict) -> Tuple[float, str]:
        """
        Predict high cholesterol risk
        
        Returns:
            Tuple of (risk_score, explanation)
        """
        cholesterol = metrics['cholesterol_level']
        age = metrics['age']
        bmi = calculate_bmi(metrics['weight'], metrics['height'])
        lifestyle = metrics['lifestyle_info'].lower()
        
        risk_score = 0.0
        factors = []
        
        # Cholesterol level is the primary factor (0-50 points)
        if cholesterol >= 240:
            risk_score += 50
            factors.append(f"cholesterol level {cholesterol} mg/dL (high)")
        elif cholesterol >= 200:
            risk_score += 30
            factors.append(f"cholesterol level {cholesterol} mg/dL (borderline high)")
        elif cholesterol >= 180:
            risk_score += 15
        
        # Diet factor (0-25 points)
        if 'high fat' in lifestyle or 'fried' in lifestyle or 'fast food' in lifestyle:
            risk_score += 20
            factors.append("high-fat diet")
        elif 'poor diet' in lifestyle:
            risk_score += 10
        
        # Exercise factor (0-15 points)
        if 'no exercise' in lifestyle or 'sedentary' in lifestyle:
            risk_score += 15
            factors.append("lack of exercise")
        
        # BMI factor (0-10 points)
        if bmi >= 30:
            risk_score += 10
            factors.append("high BMI")
        
        # Generate explanation
        if cholesterol >= 240:
            explanation = f"Cholesterol level ({cholesterol} mg/dL) is significantly above recommended range (<200 mg/dL). {', '.join(factors)}."
        elif cholesterol >= 200:
            explanation = f"Cholesterol level ({cholesterol} mg/dL) is above optimal range. Consider dietary modifications."
        else:
            explanation = f"Cholesterol level ({cholesterol} mg/dL) is within healthy range."
        
        return min(risk_score, 100.0), explanation
    
    def predict_all_risks(self, metrics: Dict) -> Dict:
        """
        Predict all health risks
        
        Returns:
            Dictionary with risk scores and explanations
        """
        diabetes_score, diabetes_exp = self.predict_diabetes_risk(metrics)
        heart_score, heart_exp = self.predict_heart_disease_risk(metrics)
        cholesterol_score, cholesterol_exp = self.predict_cholesterol_risk(metrics)
        
        return {
            'risk_scores': {
                'diabetes': round(diabetes_score, 1),
                'heart_disease': round(heart_score, 1),
                'high_cholesterol': round(cholesterol_score, 1)
            },
            'explanations': {
                'diabetes': diabetes_exp,
                'heart_disease': heart_exp,
                'high_cholesterol': cholesterol_exp
            }
        }


# Singleton instance
risk_predictor = RiskPredictor()
