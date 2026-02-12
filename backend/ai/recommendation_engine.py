"""
Recommendation Engine
Generates personalized health advice based on risk predictions
"""
from typing import Dict
from ..validators import get_risk_category


class RecommendationEngine:
    """Generate personalized health recommendations"""
    
    def __init__(self):
        """Initialize recommendation templates"""
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load recommendation templates for different conditions and risk levels"""
        return {
            'diabetes': {
                'Low': [
                    "Continue maintaining healthy lifestyle habits.",
                    "Monitor blood sugar levels annually during regular check-ups.",
                    "Maintain current weight and exercise routine.",
                    "Keep consumption of refined sugars moderate."
                ],
                'Moderate': [
                    "Increase physical activity to 30 minutes of moderate exercise, 5 days per week.",
                    "Reduce intake of refined sugars and processed carbohydrates.",
                    "Monitor blood glucose levels every 3-6 months.",
                    "Consider consultation with a nutritionist for personalized meal planning.",
                    "Aim to achieve and maintain a healthy BMI (18.5-24.9)."
                ],
                'High': [
                    "**Consult a healthcare provider immediately** for comprehensive diabetes screening.",
                    "Increase daily exercise to at least 30-45 minutes of moderate intensity activity.",
                    "Significantly reduce sugar intake and follow a low-glycemic diet.",
                    "Monitor blood glucose levels weekly or as recommended by your doctor.",
                    "Work with a healthcare team (doctor, dietitian, diabetes educator) to create a prevention plan.",
                    "Consider medication if recommended by your physician."
                ]
            },
            'heart_disease': {
                'Low': [
                    "Continue current healthy habits.",
                    "Monitor blood pressure during annual check-ups.",
                    "Maintain a heart-healthy diet rich in fruits, vegetables, and whole grains.",
                    "Stay physically active with regular exercise."
                ],
                'Moderate': [
                    "Check blood pressure monthly or as recommended.",
                    "Reduce saturated fats and trans fats in your diet.",
                    "Increase consumption of omega-3 fatty acids (fish, nuts, seeds).",
                    "Maintain healthy weight through balanced diet and regular exercise.",
                    "Manage stress through relaxation techniques or meditation.",
                    "Limit sodium intake to less than 2,300 mg per day."
                ],
                'High': [
                    "**Schedule an appointment with a cardiologist** for comprehensive heart health evaluation.",
                    "Monitor blood pressure weekly or as directed by your doctor.",
                    "Follow DASH diet or similar heart-healthy eating plan.",
                    "Quit smoking immediately if you smoke.",
                    "Engage in cardiac rehabilitation or supervised exercise program.",
                    "Take prescribed medications as directed.",
                    "Reduce stress and ensure adequate sleep (7-9 hours)."
                ]
            },
            'high_cholesterol': {
                'Low': [
                    "Maintain current healthy eating habits.",
                    "Check cholesterol levels every 4-6 years during routine physicals.",
                    "Continue regular physical activity.",
                    "Limit dietary cholesterol and saturated fats."
                ],
                'Moderate': [
                    "Increase fiber intake through whole grains, fruits, and vegetables.",
                    "Limit fried foods and foods high in saturated fats.",
                    "Choose lean proteins (fish, poultry, legumes).",
                    "Exercise regularly (at least 150 minutes per week).",
                    "Have cholesterol levels checked annually.",
                    "Consider plant sterols/stanols in diet."
                ],
                'High': [
                    "**Consult your doctor** about cholesterol-lowering medication (statins).",
                    "Adopt a strict low-cholesterol, low-saturated fat diet.",
                    "Increase fiber intake to 25-30 grams per day.",
                    "Eliminate trans fats completely from your diet.",
                    "Exercise at least 30 minutes daily, most days of the week.",
                    "Have cholesterol levels monitored every 3 months.",
                    "If overweight, work toward gradual, sustainable weight loss."
                ]
            }
        }
    
    def generate_recommendations(self, risk_scores: Dict[str, float]) -> Dict[str, str]:
        """
        Generate recommendations based on risk scores
        
        Args:
            risk_scores: Dictionary mapping condition -> risk score (0-100)
        
        Returns:
            Dictionary mapping condition -> recommendation text
        """
        recommendations = {}
        
        for condition, score in risk_scores.items():
            risk_level = get_risk_category(score)
            
            if condition in self.templates:
                advice_list = self.templates[condition][risk_level]
                recommendations[condition] = " ".join(advice_list)
            else:
                recommendations[condition] = "No specific recommendations available."
        
        return recommendations
    
    def generate_detailed_recommendations(self, risk_scores: Dict[str, float]) -> Dict:
        """
        Generate detailed recommendations with action items
        
        Returns:
            Dictionary with recommendations and action lists
        """
        detailed = {}
        
        for condition, score in risk_scores.items():
            risk_level = get_risk_category(score)
            
            if condition in self.templates:
                actions = self.templates[condition][risk_level]
                detailed[condition] = {
                    'risk_level': risk_level,
                    'score': score,
                    'advice': " ".join(actions),
                    'actions': actions,
                    'priority': 'High' if risk_level == 'High' else 'Medium' if risk_level == 'Moderate' else 'Low'
                }
        
        return detailed
    
    def get_confidence_levels(self, risk_scores: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate confidence levels for recommendations
        
        Returns:
            Dictionary mapping condition -> confidence (0-100)
        """
        confidence = {}
        
        for condition, score in risk_scores.items():
            # Higher confidence for more extreme scores
            if score >= 70 or score <= 20:
                confidence[condition] = 95.0
            elif score >= 50 or score <= 40:
                confidence[condition] = 85.0
            else:
                confidence[condition] = 75.0
        
        return confidence


# Singleton instance
recommendation_engine = RecommendationEngine()
