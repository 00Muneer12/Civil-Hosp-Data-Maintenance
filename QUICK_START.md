# HealthNexus AI - Quick Start Guide

## 🚀 Running Locally

### Windows:
```bash
# Double-click or run:
start.bat
```

### Linux/Mac:
```bash
chmod +x start.sh
./start.sh
```

### Manual Start:

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## 🌐 Access Points

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

## 🧪 Test the System

1. Open http://localhost:3000
2. Fill the health data form
3. Click "Analyze Health Data"
4. View risk predictions and recommendations

## 📦 Deployment

See [deployment_guide.md](deployment_guide.md) for detailed deployment instructions.

**Recommended platforms:**
- **Railway.app** - Free tier, one-click deploy
- **Render.com** - Free tier, auto-deploy from Git
- **Vercel** (Frontend) + Railway (Backend) - Best performance

## 🛑 Stopping Services

**Windows:**
- Close the command windows
- Or use Task Manager to end Node.js and Python processes

**Linux/Mac:**
```bash
# If you have PIDs saved:
kill $(cat .backend.pid)
kill $(cat .frontend.pid)

# Or find and kill manually:
pkill -f uvicorn
pkill -f "next dev"
```
