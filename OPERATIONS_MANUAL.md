# Data Entry & Analysis System - Operations Manual

## 🟢 MODULE 1: REAL-TIME DATA ENTRY (Fast & Efficient)

### Purpose
Register patient CNICs, enter symptoms, prescribe medicines in real-time with minimal typing.

### Quick Entry Process (< 2 minutes per patient)

#### Step 1: Patient Registration
```
Use quick_entry_template.csv
- CNIC: Auto-validate format (12 digits)
- Age: Numeric only (0-120)
- Gender: M or F (single key)
- Disease: Use disease_code from disease_reference.csv (AST, DIA, MAL, etc.)
```

#### Step 2: Symptom Entry
- Select primary disease code (auto-populate common medicines)
- Confirm severity (M/MOD/SEV/CRI) using color codes

#### Step 3: Medicine Prescription
- Select medicine_code from medicine_reference.csv
- Standard dosage auto-fills
- Enter quantity (standard amounts: 1, 3, 5, 10, 12, 30, 60)
- One click to save

#### Step 4: Doctor Assignment
- Use Doctor_ID from doctor_reference.csv
- Auto-assign based on specialization/availability

### Color-Coded Severity Entry
```
🟢 M (Mild) - Press "1" - Green indicator
🟡 MOD (Moderate) - Press "2" - Yellow indicator
🟠 SEV (Severe) - Press "3" - Orange indicator
🔴 CRI (Critical) - Press "4" - Red indicator
```

### Quick Entry Shortcuts
- **Ctrl+N**: New patient entry
- **Ctrl+S**: Save prescription
- **Ctrl+D**: Quick disease lookup
- **Ctrl+M**: Quick medicine lookup
- **Tab**: Auto-complete common diseases/medicines
- **Enter**: Submit and next patient

### Data Validation Rules (Automatic)
✓ CNIC format: Must be 12 numeric characters  
✓ Age: Must be 0-120  
✓ Disease Code: Must exist in disease_reference.csv  
✓ Medicine Code: Must exist in medicine_reference.csv  
✗ Invalid entries: Marked red, cannot save until fixed  

---

## 🟠 MODULE 2: DATA ANALYSIS & MONITORING (Trends & Alerts)

### Purpose
Monitor disease outbreaks, check stock levels, identify trends over 30 days.

### Key Dashboards & Reports

#### Dashboard 1: Inventory Alerts (Daily Check)
**File**: inventory_alerts.csv
- **Green** ✓ Safe - >30 days supply remaining
- **Yellow** ⚠ Caution - 15-30 days remaining (monitor/order)
- **Red** 🛑 Critical - <15 days or below reorder level

**Action Items**:
1. Check Alert_Color daily
2. If Yellow: Monitor usage trends
3. If Red: Place emergency order immediately
4. Formula: Days_to_Stockout = Current_Stock ÷ Daily_Average_Usage

**Current Critical Status**: ORS + Zinc (Yellow - 31 days remaining)

---

#### Dashboard 2: Disease Outbreak Tracking (30-Day Trends)
**File**: disease_outbreak_30day.csv

**Key Metrics**:
- Cases_Last_30Days: Total cases in past month
- Daily_Average: Average cases per day
- Trend: Stable, Rising, or High
- Alert_Status: Green (normal), Yellow (monitor), Orange (outbreak)

**Disease Status Summary**:
```
🟢 Asthma: Stable (12 cases, 0.4/day)
🟡 Gastroenteritis: RISING (11 cases, trend upward) - MONITOR
🟡 Malaria: MODERATE (11 cases, yellowish pattern)
🟠 URTI (Flu): HIGH ALERT (11 cases, 0.37/day, 4 severe)
🟢 Type 2 Diabetes: Stable (13 cases)
🟡 Typhoid: RISING (11 cases, 2 severe)
```

**15-Case Threshold Rule**: 
- If any disease reaches 15 cases in 30 days → Escalate to Administration
- Currently monitoring: Gastroenteritis, URTI (Flu)

---

#### Dashboard 3: Prescription Log Analysis (7/14/30-Day)
**File**: prescription_log_daily.csv

**Analysis Points**:
1. **Daily Volume**: Count by date
2. **Doctor Workload**: Count by Doctor_Name
3. **Medicine Usage**: Count by medicine (predict stock needs)
4. **Severity Distribution**: % of Mild/Moderate/Severe/Critical
5. **Disease Pattern**: Track emerging diseases

**Current Week Summary (Feb 6-12)**:
- Total transactions: 30
- Daily average: 3.3 patients
- Most prescribed: Panadol (6), Metformin (4), Folic Acid+Iron (5)
- Severity: 47% Mild, 27% Moderate, 27% Severe (high severe cases)

---

#### Dashboard 4: KPI Monitoring (Real-Time Alerts)
**File**: kpi_dashboard.csv

**Watch These 5 Critical KPIs**:

1. **KPI005: ORS Stock Days** 📉 YELLOW ALERT
   - Current: 31 days
   - Target: 45 days
   - Action: Monitor daily, prepare order for 200 sachets

2. **KPI007: Disease Outbreak Incidents** 📈 ORANGE ALERT
   - Current: 3 (URTI, Gastroenteritis, Typhoid rising)
   - Target: <2
   - Action: Implement outbreak protocol

3. **KPI003: Stock Availability** 📉 YELLOW ALERT
   - Current: 87.5%
   - Target: 95%
   - Action: Review ordering frequency

4. **KPI002: Prescription Accuracy** 📊 YELLOW
   - Current: 97%
   - Target: 99%
   - Action: Review data entry validation

5. **KPI006: Average Wait Time** ⏱️ YELLOW ALERT
   - Current: 22 min
   - Target: 15 min
   - Action: Optimize patient flow

---

### Weekly Analysis Report (Generate Every Monday)

1. **Disease Summary**: 
   - Top 3 diseases last week
   - Case increase/decrease vs previous week
   - Severe/critical cases trend

2. **Inventory Summary**:
   - Medicines running low (Yellow/Red)
   - Recommended orders
   - Cost impact

3. **Performance Summary**:
   - Doctor workload distribution
   - Average cases per doctor
   - Prescriptions accuracy rate

4. **Alerts**:
   - Any KPIs in Red
   - Emerging disease patterns
   - Stock shortages predicted

---

### Monthly Analysis Report (Generate Every 1st)

1. **Epidemiological Summary**:
   - Disease distribution (%)
   - Seasonal patterns observed
   - Any new diseases identified

2. **Operational Performance**:
   - Total patients: 100
   - Total prescriptions: 115
   - Doctor productivity
   - Patient satisfaction trends

3. **Financial Impact**:
   - Inventory turnover rate
   - Stock waste/loss
   - Medicine costs by disease

4. **Strategic Recommendations**:
   - Staffing adjustments needed
   - Inventory optimization
   - Process improvements

---

## 📊 Color-Code Alert System Reference

### Inventory Status Colors
```
🟢 GREEN: Safe stock level (>30 days supply)
🟡 YELLOW: Caution zone (15-30 days - monitor closely)
🔴 RED: Critical (< 15 days - order immediately)
```

### Disease Outbreak Colors
```
🟢 GREEN: Normal pattern (<5 cases/day on average)
🟡 YELLOW: Watch (5-10 cases/day, rising trend)
🟠 ORANGE: Alert (10-15 cases/day, outbreak risk)
🔴 RED: Outbreak (>15 cases/day, escalate)
```

### KPI Status Colors
```
🟢 GREEN: On or above target
🟡 YELLOW: Below target but acceptable (80-95% of target)
🔴 RED: Critical (Below 80% of target)
```

---

## 🔍 Quick Analysis Tricks

### Identify Stock Problems
1. Open inventory_alerts.csv
2. Filter for Alert_Color = "Yellow" or "Red"
3. Action: Order immediately (use Recommended_Order_Qty)

### Find Disease Outbreaks
1. Open disease_outbreak_30day.csv
2. Sort by Trend = "Rising" or "High"
3. Filter Alert_Status = "Yellow" or "Orange"
4. Monitor daily prescriptions for confirmation

### Check Doctor Workload
1. Open prescription_log_daily.csv
2. Count by Doctor_Name
3. Target: 4-5 patients per doctor per day
4. If >6: Consider redistribution

### Predict Medicine Shortage
```
Days_Until_Stockout = Current_Stock ÷ Daily_Average_Usage
If < 30 days: Prepare order
If < 15 days: Place order immediately
If < 7 days: Emergency procurement
```

---

## Example Scenarios

### Scenario 1: ORS Stock Running Low
**Alert**: Inventory_alerts.csv shows "ORS + Zinc" = Yellow, 31 days remaining
**Action**:
1. Note: Using 10 sachets/day (310 ÷ 31)
2. Place order: 500-750 sachets (2-3 months supply)
3. Estimated arrival: 5-7 days
4. Update alert status to "Under Order"
5. Monitor daily until arrival

### Scenario 2: URTI (Flu) Cases Increasing
**Alert**: disease_outbreak_30day.csv shows URTI "High" trend, 11 cases in 30 days, 4 severe
**Action**:
1. Increased Panadol usage (11 patients) - currently safe stock
2. Monitor next 3 days for trend continuation
3. If >1 new case/day: Implement outbreak precautions
4. Check Panadol stock weekly (currently 380 tablets)
5. Forecast: 11 cases/month uses ~11 tablets = safe

### Scenario 3: Low Prescription Accuracy
**Alert**: KPI002 shows 97%, target 99%
**Action**:
1. Review last 30 transactions in prescription_log_daily.csv
2. Identify errors (wrong dosage, medicine, patient)
3. Retrain staff on data entry
4. Re-run validation checks
5. Retest after 1 week

---

## Integration Notes

### FOR IT TEAMS
- **Real-time sync**: Quick_entry_template feeds → prescription_log_daily.csv (auto)
- **Calculation updates**: Daily script updates Days_to_Stockout in inventory_alerts.csv
- **Alert triggers**: Daily script checks KPI thresholds, sets colors
- **Data format**: All CSV, compatible with Excel, SQL databases, Python/Pandas

### FOR HOSPITAL STAFF
- Data entry staff: Use Module 1 (quick_entry_template.csv)
- Managers: Check Module 2 dashboards daily (5 min)
- Doctors: Reference doctor_reference.csv for workload
- Pharmacist: Monitor inventory_alerts.csv (critical)

---

**Last Update**: February 12, 2026  
**Systems Status**: All operational  
**Next Sync**: Daily at 6:00 PM (automated)

