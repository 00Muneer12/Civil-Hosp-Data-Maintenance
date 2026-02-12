#!/bin/bash

# HealthNexus AI - Quick Start Script
# This script starts both backend and frontend services

echo "🚀 Starting HealthNexus AI..."
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.9+ first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

echo "✅ Python version: $(python --version)"
echo "✅ Node.js version: $(node --version)"
echo ""

# Backend Setup
echo "📦 Setting up Backend..."
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -q -r requirements.txt

# Start backend in background
echo "🔧 Starting Backend API on http://localhost:8000"
uvicorn app:app --host 0.0.0.0 --port 8000 > ../logs/backend.log 2>&1 &
BACKEND_PID=$!
echo "Backend PID: $BACKEND_PID"

cd ..

# Frontend Setup
echo ""
echo "📦 Setting up Frontend..."
cd frontend

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "Installing Node.js dependencies..."
    npm install
fi

# Start frontend in background
echo "🎨 Starting Frontend on http://localhost:3000"
npm run dev > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!
echo "Frontend PID: $FRONTEND_PID"

cd ..

# Wait for services to start
echo ""
echo "⏳ Waiting for services to start..."
sleep 5

# Health check
echo ""
echo "🏥 Performing health checks..."

# Check backend
if curl -s http://localhost:8000/health > /dev/null; then
    echo "✅ Backend API is running"
else
    echo "❌ Backend API failed to start. Check logs/backend.log"
fi

# Check frontend
if curl -s http://localhost:3000 > /dev/null; then
    echo "✅ Frontend is running"
else
    echo "⏳ Frontend is still starting... (wait 10 more seconds)"
fi

echo ""
echo "🎉 HealthNexus AI is ready!"
echo ""
echo "📊 Access Points:"
echo "  Frontend:    http://localhost:3000"
echo "  Backend API: http://localhost:8000"
echo "  API Docs:    http://localhost:8000/docs"
echo ""
echo "📝 Logs:"
echo "  Backend:     tail -f logs/backend.log"
echo "  Frontend:    tail -f logs/frontend.log"
echo ""
echo "🛑 To stop services:"
echo "  kill $BACKEND_PID $FRONTEND_PID"
echo ""

# Save PIDs to file
echo "$BACKEND_PID" > .backend.pid
echo "$FRONTEND_PID" > .frontend.pid

echo "PIDs saved to .backend.pid and .frontend.pid"
