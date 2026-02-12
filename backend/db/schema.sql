-- HealthNexus AI Database Schema

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Health data table
CREATE TABLE IF NOT EXISTS health_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    age INTEGER NOT NULL,
    weight REAL NOT NULL,
    height REAL NOT NULL,
    blood_pressure TEXT NOT NULL,
    cholesterol_level REAL NOT NULL,
    lifestyle_info TEXT NOT NULL,
    bmi REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Predictions table
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    diabetes_risk REAL NOT NULL,
    heart_disease_risk REAL NOT NULL,
    cholesterol_risk REAL NOT NULL,
    diabetes_explanation TEXT,
    heart_disease_explanation TEXT,
    cholesterol_explanation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Recommendations table
CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    prediction_id INTEGER NOT NULL,
    diabetes_recommendation TEXT,
    heart_disease_recommendation TEXT,
    cholesterol_recommendation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (prediction_id) REFERENCES predictions(id)
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_health_data_user_id ON health_data(user_id);
CREATE INDEX IF NOT EXISTS idx_health_data_created_at ON health_data(created_at);
CREATE INDEX IF NOT EXISTS idx_predictions_user_id ON predictions(user_id);
CREATE INDEX IF NOT EXISTS idx_predictions_created_at ON predictions(created_at);
CREATE INDEX IF NOT EXISTS idx_recommendations_user_id ON recommendations(user_id);
