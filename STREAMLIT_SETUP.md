# 🏥 Hospital OPD Streamlit App - Setup & Run Guide

## ⚡ Quick Start (5 minutes)

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App
```bash
streamlit run app.py
```

### 3. Open in Browser
The app will automatically open at:
```
http://localhost:8501
```

---

## 📱 Features Included

### 📊 Dashboard
- Real-time system status
- Quick metrics cards
- Inventory overview
- Disease alerts summary

### ➕ Data Entry
- Fast patient registration (<2 min)
- Auto-populated fields
- Real-time validation
- One-click save

### 📦 Inventory Management
- Stock status overview
- Alert indicators (Green/Yellow/Red)
- Days-to-stockout predictions
- Order recommendations

### 🦠 Disease Outbreak Monitoring
- 30-day disease trends
- Alert status tracking
- High-risk disease alerts
- Case distribution analysis

### 📈 Analytics & Reports
- KPI dashboard (10 metrics)
- Doctor workload analysis
- Disease severity distribution
- Medicine usage patterns

### ⚙️ Settings
- System information
- Data management
- Logs viewer
- Data refresh options

---

## 🖥️ System Requirements

- Python 3.8+
- Windows/Mac/Linux
- 4GB RAM (minimum)
- Internet connection (for Plotly)

---

## 📂 File Structure

```
Civil-Hosp-Data-Maintenance/
├── app.py ........................... Main Streamlit application
├── requirements.txt ................. Python dependencies
├── data/
│   ├── opd_patients_100.csv
│   ├── prescription_log_daily.csv
│   ├── inventory_alerts.csv
│   ├── disease_outbreak_30day.csv
│   ├── kpi_dashboard.csv
│   └── ... (other reference files)
└── datasets/
    └── ... (historical data)
```

---

## 🚀 Running the App

### Option 1: Command Line (Windows PowerShell)
```powershell
cd d:\Civil-Hosp-Data-Maintenance
streamlit run app.py
```

### Option 2: Command Line (Mac/Linux)
```bash
cd Civil-Hosp-Data-Maintenance
streamlit run app.py
```

### Option 3: Create Batch File (Windows)
Create a file named `run_app.bat`:
```batch
@echo off
cd /d d:\Civil-Hosp-Data-Maintenance
streamlit run app.py
pause
```

Then double-click the file to run.

---

## 🌐 Accessing the App

Once running, the app will display:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.xxx:8501
```

### Open in Browser:
- **Same computer**: Click the URL or visit `http://localhost:8501`
- **Other computers**: Use the Network URL (IP address shown)

---

## 📊 App Navigation

### Left Sidebar Menu
Select one of 6 pages:

1. **📊 Dashboard** - Overview & key metrics
2. **➕ Data Entry** - Register new patients
3. **📦 Inventory** - Check stock levels
4. **🦠 Disease Monitor** - Track disease trends
5. **📈 Analytics** - Performance analysis
6. **⚙️ Settings** - System configuration

---

## 🎯 Common Tasks

### Register a Patient
1. Click "➕ Data Entry"
2. Enter: CNIC, Age, Gender
3. Select: Disease, Severity, Medicine
4. Click: **SAVE**
✓ Patient registered instantly

### Check Inventory
1. Click "📦 Inventory"
2. See all medicines with stock levels
3. Yellow/Red items need orders
4. Review action recommendations

### Monitor Disease Outbreaks
1. Click "🦠 Disease Monitor"
2. View 30-day trends
3. See alert status (Green/Yellow/Orange)
4. Check most affected ages

### View Performance
1. Click "📈 Analytics"
2. Review 10 KPIs
3. See charts and trends
4. Download reports

---

## ⚙️ Configuration

### Change Port (if 8501 is in use)
```bash
streamlit run app.py --server.port 8502
```

### Run in Headless Mode (no browser auto-open)
```bash
streamlit run app.py --logger.level=debug --client.showErrorDetails=false
```

### Full Width Layout
Already configured. If you want sidebar:
Edit app.py line 17:
```python
layout="centered"  # Change from "wide"
```

---

## 🐛 Troubleshooting

### Issue: Port already in use
**Solution**: Use different port
```bash
streamlit run app.py --server.port 8502
```

### Issue: Data files not found
**Solution**: Ensure app.py is in same directory as data/ folder
```
Civil-Hosp-Data-Maintenance/
├── app.py
└── data/
```

### Issue: Streamlit not installed
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Charts not displaying
**Solution**: Update Plotly
```bash
pip install --upgrade plotly
```

---

## 🔄 Real-Time Updates

The app caches data for performance. To force refresh:
1. Click "⚙️ Settings" page
2. Click "📥 Reload Data" button
Or restart the app: `Ctrl+C` then run again

---

## 📊 Data Files Used

### Primary Files
- `opd_patients_100.csv` - Patient database
- `prescription_log_daily.csv` - Daily prescriptions
- `inventory_alerts.csv` - Stock status
- `disease_outbreak_30day.csv` - Disease trends
- `kpi_dashboard.csv` - Performance metrics

### Reference Files
- `doctor_reference.csv` - Doctor info
- `medicine_reference.csv` - Medicine codes
- `disease_reference.csv` - Disease codes
- `severity_reference.csv` - Severity levels

---

## 📱 Mobile Access

The app is **responsive** and works on:
- Desktop browsers
- Tablets
- Smartphones

Just use the Network URL from another device on same network

---

## 📤 Export Data

Data can be exported from:
1. Dashboard: Click table → Export option
2. Analytics: Charts can be downloaded
3. Settings: "📄 Export Report" button

---

## 🔒 Security Notes

- App runs locally (no data uploaded)
- CVS files stored on your computer
- No authentication enabled (add if needed)
- Suitable for internal hospital use

---

## 📞 Support

### Common Questions

**Q**: Can I add more medicines?
**A**: Yes, edit `data/medicine_reference.csv`

**Q**: How do I customize the app?
**A**: Edit `app.py` and change sections

**Q**: Can it handle more patients?
**A**: Yes, just update CSV files

**Q**: How do I backup data?
**A**: Copy the entire `data/` folder

---

## 🎉 You're Ready!

Your Streamlit app is fully configured and ready to use!

**Run it now**:
```bash
streamlit run app.py
```

Enjoy your professional hospital management system! 🏥✨

---

**Version**: 1.0  
**Last Updated**: February 12, 2026  
**Status**: ✅ Production Ready
