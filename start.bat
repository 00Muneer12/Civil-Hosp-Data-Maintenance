@echo off
REM HealthNexus AI - Quick Start Script for Windows
REM This script starts both backend and frontend services

echo.
echo ========================================
echo   HealthNexus AI - Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed. Please install Python 3.9+
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js is not installed. Please install Node.js 18+
    pause
    exit /b 1
)

echo [OK] Python version:
python --version
echo [OK] Node.js version:
node --version
echo.

REM Create logs directory
if not exist "logs" mkdir logs

REM ========================================
REM Backend Setup
REM ========================================
echo.
echo [STEP 1] Setting up Backend...
cd backend

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo Creating Python virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Install dependencies
echo Installing Python dependencies...
pip install -q -r requirements.txt

REM Start backend
echo Starting Backend API on http://localhost:8000
start "HealthNexus Backend" /MIN cmd /c "uvicorn app:app --host 0.0.0.0 --port 8000 > ..\logs\backend.log 2>&1"

cd ..

REM ========================================
REM Frontend Setup
REM ========================================
echo.
echo [STEP 2] Setting up Frontend...
cd frontend

REM Install dependencies if node_modules doesn't exist
if not exist "node_modules" (
    echo Installing Node.js dependencies...
    echo This may take a few minutes...
    call npm install
)

REM Start frontend
echo Starting Frontend on http://localhost:3000
start "HealthNexus Frontend" /MIN cmd /c "npm run dev > ..\logs\frontend.log 2>&1"

cd ..

REM Wait for services to start
echo.
echo Waiting for services to start...
timeout /t 10 /nobreak > nul

REM ========================================
REM Health Check
REM ========================================
echo.
echo [STEP 3] Performing health checks...
echo.

REM Check backend (using curl if available, otherwise skip)
where curl >nul 2>&1
if %errorlevel% equ 0 (
    curl -s http://localhost:8000/health >nul 2>&1
    if errorlevel 1 (
        echo [WARN] Backend API may still be starting...
    ) else (
        echo [OK] Backend API is running
    )
) else (
    echo [INFO] curl not found, skipping health check
)

echo.
echo ========================================
echo   HealthNexus AI is ready!
echo ========================================
echo.
echo Access Points:
echo   Frontend:    http://localhost:3000
echo   Backend API: http://localhost:8000
echo   API Docs:    http://localhost:8000/docs
echo.
echo Logs:
echo   Backend:     logs\backend.log
echo   Frontend:    logs\frontend.log
echo.
echo Press any key to open the browser...
pause >nul

REM Open browser
start http://localhost:3000

echo.
echo System is running. Close this window to keep services running.
echo.
pause
