#!/usr/bin/env python3
"""
Civil Hospital OPD Data Analysis Tool
Analyzes prescription data, inventory, and disease outbreaks in real-time
"""

import pandas as pd
import json
from datetime import datetime, timedelta
from pathlib import Path

class HospitalAnalytics:
    """Analyze hospital OPD data and generate insights"""
    
    def __init__(self, data_path="d:\\Civil-Hosp-Data-Maintenance\\data"):
        self.data_path = Path(data_path)
        self.load_data()
    
    def load_data(self):
        """Load all CSV files"""
        try:
            self.patients = pd.read_csv(self.data_path / "opd_patients_100.csv")
            self.prescriptions = pd.read_csv(self.data_path / "prescription_log_daily.csv")
            self.inventory = pd.read_csv(self.data_path / "inventory_alerts.csv")
            self.diseases = pd.read_csv(self.data_path / "disease_outbreak_30day.csv")
            self.kpis = pd.read_csv(self.data_path / "kpi_dashboard.csv")
            print("✓ All data loaded successfully")
        except Exception as e:
            print(f"✗ Error loading data: {e}")
    
    def generate_daily_report(self):
        """Generate daily operations report"""
        print("\n" + "="*60)
        print("DAILY OPERATIONS REPORT")
        print("="*60)
        
        # Prescription summary
        today = pd.Timestamp.today().strftime('%Y-%m-%d')
        today_rx = self.prescriptions[self.prescriptions['Date'] == today]
        print(f"\n📋 TODAY'S PRESCRIPTIONS ({today})")
        print(f"   Total: {len(today_rx)} patients")
        if len(today_rx) > 0:
            by_disease = today_rx['Disease'].value_counts()
            print("   By Disease:")
            for disease, count in by_disease.items():
                print(f"      - {disease}: {count}")
        
        # Inventory alerts
        print("\n📦 INVENTORY STATUS")
        yellow_items = self.inventory[self.inventory['Alert_Color'] == 'Yellow']
        red_items = self.inventory[self.inventory['Alert_Color'] == 'Red']
        
        if len(red_items) > 0:
            print("   🔴 CRITICAL (Red):")
            for _, item in red_items.iterrows():
                print(f"      - {item['Medicine_Name']}: {item['Days_to_Stockout']} days left")
        
        if len(yellow_items) > 0:
            print("   🟡 CAUTION (Yellow):")
            for _, item in yellow_items.iterrows():
                print(f"      - {item['Medicine_Name']}: {item['Days_to_Stockout']} days left")
        
        green_items = len(self.inventory) - len(red_items) - len(yellow_items)
        print(f"   🟢 SAFE (Green): {green_items} medicines")
        
        # Disease alerts
        print("\n🦠 DISEASE MONITORING")
        alerts = self.diseases[self.diseases['Alert_Status'].isin(['Orange', 'Yellow'])]
        for _, disease in alerts.iterrows():
            status_icon = "🟠" if disease['Alert_Status'] == 'Orange' else "🟡"
            print(f"   {status_icon} {disease['Disease_Name']}")
            print(f"      - Cases (30-day): {disease['Cases_Last_30Days']}")
            print(f"      - Daily avg: {disease['Daily_Average']:.2f}")
            print(f"      - Trend: {disease['Trend']}")
            print(f"      - Severe cases: {disease['Severity_Distribution']}")
    
    def analyze_stock_prediction(self):
        """Predict when medicines will run out"""
        print("\n" + "="*60)
        print("STOCK PREDICTION ANALYSIS")
        print("="*60)
        
        critical_medicines = []
        for _, med in self.inventory.iterrows():
            days_left = med['Days_to_Stockout']
            if days_left < 45:
                critical_medicines.append({
                    'name': med['Medicine_Name'],
                    'days': days_left,
                    'status': 'CRITICAL' if days_left < 15 else 'MONITOR',
                    'order_qty': med['Recommended_Order_Qty']
                })
        
        if critical_medicines:
            print("\n⚠️  Medicines Needing Attention:")
            for med in sorted(critical_medicines, key=lambda x: x['days']):
                print(f"\n   {med['name']}")
                print(f"   Days remaining: {med['days']}")
                print(f"   Status: {med['status']}")
                if med['order_qty'] > 0:
                    print(f"   Recommend order: {med['order_qty']} units")
        else:
            print("\n✓ All medicines have adequate stock (>45 days)")
    
    def analyze_disease_patterns(self):
        """Identify disease patterns and outbreaks"""
        print("\n" + "="*60)
        print("DISEASE PATTERN ANALYSIS (30-Day)")
        print("="*60)
        
        print("\nTop Diseases by Volume:")
        top_diseases = self.diseases.nlargest(5, 'Cases_Last_30Days')
        for idx, (_, disease) in enumerate(top_diseases.iterrows(), 1):
            print(f"\n   {idx}. {disease['Disease_Name']}")
            print(f"      Total cases: {disease['Cases_Last_30Days']}")
            print(f"      Daily avg: {disease['Daily_Average']:.2f}")
            print(f"      Alert status: {disease['Alert_Status']}")
        
        print("\n\n📈 Rising Trend Diseases (Monitor):")
        rising = self.diseases[self.diseases['Trend'].isin(['Rising', 'High'])]
        for _, disease in rising.iterrows():
            print(f"\n   {disease['Disease_Name']}")
            print(f"      Trend: {disease['Trend']}")
            print(f"      Cases: {disease['Cases_Last_30Days']}")
            print(f"      Peak date: {disease['Peak_Date']}")
    
    def generate_kpi_summary(self):
        """Summarize KPI status"""
        print("\n" + "="*60)
        print("KEY PERFORMANCE INDICATORS (KPI)")
        print("="*60)
        
        red_kpis = self.kpis[self.kpis['Alert_Level'] == 'Red']
        yellow_kpis = self.kpis[self.kpis['Alert_Level'] == 'Yellow']
        green_kpis = self.kpis[self.kpis['Alert_Level'] == 'Green']
        
        print(f"\n🟢 On Target (Green): {len(green_kpis)}")
        for _, kpi in green_kpis.iterrows():
            print(f"   ✓ {kpi['KPI_Name']}: {kpi['Current_Value']}")
        
        if len(yellow_kpis) > 0:
            print(f"\n🟡 Below Target (Yellow): {len(yellow_kpis)}")
            for _, kpi in yellow_kpis.iterrows():
                print(f"   ⚠ {kpi['KPI_Name']}: {kpi['Current_Value']} (Target: {kpi['Target_Value']})")
        
        if len(red_kpis) > 0:
            print(f"\n🔴 Critical (Red): {len(red_kpis)}")
            for _, kpi in red_kpis.iterrows():
                print(f"   ✗ {kpi['KPI_Name']}: {kpi['Current_Value']} (Target: {kpi['Target_Value']})")
    
    def prescription_insights(self):
        """Analyze prescription patterns"""
        print("\n" + "="*60)
        print("PRESCRIPTION ANALYSIS")
        print("="*60)
        
        print("\nTop Prescribed Medicines:")
        top_meds = self.prescriptions['Prescribed_Medicine'].value_counts().head(5)
        for med, count in top_meds.items():
            print(f"   - {med}: {count} prescriptions")
        
        print("\nSeverity Distribution:")
        severity_dist = self.prescriptions['Severity'].value_counts()
        for severity, count in severity_dist.items():
            pct = (count / len(self.prescriptions)) * 100
            print(f"   - {severity}: {count} ({pct:.1f}%)")
        
        print("\nTop Doctors by Workload:")
        doc_load = self.prescriptions['Doctor_Name'].value_counts().head(5)
        for doc, count in doc_load.items():
            print(f"   - {doc}: {count} patients")
    
    def generate_report_json(self):
        """Generate JSON report for API/Dashboard"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_patients_today': len(self.prescriptions[self.prescriptions['Date'] == pd.Timestamp.today().strftime('%Y-%m-%d')]),
                'medicines_safe': len(self.inventory[self.inventory['Alert_Color'] == 'Green']),
                'medicines_warning': len(self.inventory[self.inventory['Alert_Color'] == 'Yellow']),
                'medicines_critical': len(self.inventory[self.inventory['Alert_Color'] == 'Red']),
            },
            'inventory_alerts': self.inventory.to_dict('records'),
            'kpi_status': {
                'green': len(self.kpis[self.kpis['Alert_Level'] == 'Green']),
                'yellow': len(self.kpis[self.kpis['Alert_Level'] == 'Yellow']),
                'red': len(self.kpis[self.kpis['Alert_Level'] == 'Red']),
            },
            'diseases_alert': self.diseases[self.diseases['Alert_Status'].isin(['Orange', 'Yellow', 'Red'])].to_dict('records'),
        }
        return report
    
    def generate_full_report(self):
        """Generate complete analysis report"""
        self.generate_daily_report()
        self.analyze_stock_prediction()
        self.analyze_disease_patterns()
        self.prescription_insights()
        self.generate_kpi_summary()
        
        print("\n" + "="*60)
        print("END OF REPORT")
        print("="*60)


def main():
    """Run analysis"""
    try:
        analytics = HospitalAnalytics()
        analytics.generate_full_report()
        
        # Save JSON report
        report = analytics.generate_report_json()
        with open('hospital_analysis_report.json', 'w') as f:
            json.dump(report, f, indent=2, default=str)
        print("\n✓ JSON report saved: hospital_analysis_report.json")
        
    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
