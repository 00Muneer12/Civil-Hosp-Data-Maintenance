"""
CRUD operations for database
"""
import sqlite3
from typing import List, Dict, Optional
from datetime import datetime
from config import settings


class HealthDataCRUD:
    """CRUD operations for health data"""
    
    def __init__(self):
        self.db_path = settings.DATABASE_URL.replace('sqlite:///', '')
    
    def _get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_path)
    
    def create_user(self, user_id: str) -> bool:
        """Create a new user if not exists"""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
                (user_id,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def save_health_data(self, user_id: str, metrics: Dict, bmi: float) -> Optional[int]:
        """Save health data to database"""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Ensure user exists
            self.create_user(user_id)
            
            cursor.execute("""
                INSERT INTO health_data 
                (user_id, age, weight, height, blood_pressure, cholesterol_level, lifestyle_info, bmi)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                metrics['age'],
                metrics['weight'],
                metrics['height'],
                metrics['blood_pressure'],
                metrics['cholesterol_level'],
                metrics['lifestyle_info'],
                bmi
            ))
            
            data_id = cursor.lastrowid
            conn.commit()
            conn.close()
            return data_id
        except Exception as e:
            print(f"Error saving health data: {e}")
            return None
    
    def save_predictions(self, user_id: str, risk_scores: Dict, explanations: Dict) -> Optional[int]:
        """Save prediction results"""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO predictions 
                (user_id, diabetes_risk, heart_disease_risk, cholesterol_risk,
                 diabetes_explanation, heart_disease_explanation, cholesterol_explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                risk_scores.get('diabetes', 0),
                risk_scores.get('heart_disease', 0),
                risk_scores.get('high_cholesterol', 0),
                explanations.get('diabetes', ''),
                explanations.get('heart_disease', ''),
                explanations.get('high_cholesterol', '')
            ))
            
            prediction_id = cursor.lastrowid
            conn.commit()
            conn.close()
            return prediction_id
        except Exception as e:
            print(f"Error saving predictions: {e}")
            return None
    
    def save_recommendations(self, user_id: str, prediction_id: int, recommendations: Dict) -> bool:
        """Save recommendations"""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO recommendations 
                (user_id, prediction_id, diabetes_recommendation, 
                 heart_disease_recommendation, cholesterol_recommendation)
                VALUES (?, ?, ?, ?, ?)
            """, (
                user_id,
                prediction_id,
                recommendations.get('diabetes', ''),
                recommendations.get('heart_disease', ''),
                recommendations.get('high_cholesterol', '')
            ))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error saving recommendations: {e}")
            return False
    
    def get_user_history(self, user_id: str, limit: int = 10) -> List[Dict]:
        """Get user's health data history"""
        try:
            conn = self._get_connection()
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM health_data 
                WHERE user_id = ? 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (user_id, limit))
            
            rows = cursor.fetchall()
            conn.close()
            
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Error getting user history: {e}")
            return []
    
    def get_user_predictions(self, user_id: str, limit: int = 10) -> List[Dict]:
        """Get user's prediction history"""
        try:
            conn = self._get_connection()
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM predictions 
                WHERE user_id = ? 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (user_id, limit))
            
            rows = cursor.fetchall()
            conn.close()
            
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Error getting user predictions: {e}")
            return []
    
    def get_latest_analysis(self, user_id: str) -> Optional[Dict]:
        """Get the latest complete analysis for a user"""
        try:
            conn = self._get_connection()
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT 
                    p.*,
                    r.diabetes_recommendation,
                    r.heart_disease_recommendation,
                    r.cholesterol_recommendation
                FROM predictions p
                LEFT JOIN recommendations r ON p.id = r.prediction_id
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
                LIMIT 1
            """, (user_id,))
            
            row = cursor.fetchone()
            conn.close()
            
            if row:
                return dict(row)
            return None
        except Exception as e:
            print(f"Error getting latest analysis: {e}")
            return None


# Singleton instance
db_crud = HealthDataCRUD()
