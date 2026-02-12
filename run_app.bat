@echo off
REM Hospital OPD Management System - Streamlit App Launcher
REM Run this file to start the web app

echo.
echo ========================================
echo 🏥 Hospital OPD Management System
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Streamlit app...
echo.
streamlit run app.py

pause
