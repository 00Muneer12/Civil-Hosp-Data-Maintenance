# Civil Hospital OPD Dataset - Data Schema & Documentation

## Overview
This dataset provides a comprehensive classification system for civil hospital patients, organized by severity levels, disease categories, and prescribed medicines. The data reflects typical Pakistani civil hospital patterns.

---

## 1. SEVERITY CLASSIFICATION SYSTEM

### Severity Levels (4-Tier Triage)

| Level | Code | Color | Definition | Intervention | Wait Time | Examples |
|-------|------|-------|-----------|---|---|---|
| **Mild** | SEV001 | 🟢 Green | Simple infections, seasonal flu, minor injuries | Outpatient | 15-30 min | Common Cold, Cough, Minor Cuts |
| **Moderate** | SEV002 | 🟡 Yellow | Stable chronic conditions requiring monitoring | Monitored OPD | 30-60 min | Hypertension, Diabetes, Mild Dehydration |
| **Severe** | SEV003 | 🟠 Orange | Conditions requiring immediate intervention | Emergency Dept | Immediate | High Fever, Respiratory Distress |
| **Critical** | SEV004 | 🔴 Red | Life-threatening emergencies | ER/ICU | Immediate | Cardiac Emergency, Stroke, Trauma |

### Severity Distribution (Annual - 45,000 OPD patients)
- **Mild (45%)**: 20,250 patients
- **Moderate (35%)**: 15,750 patients
- **Severe (15%)**: 6,750 patients
- **Critical (5%)**: 2,250 patients

---

## 2. DISEASE-WISE DISTRIBUTION

### The "Big Three" Categories (60% of OPD Volume)

#### A. **INFECTIOUS DISEASES (24% - 10,800 patients)**
Primary diseases: Gastroenteritis (8%), Malaria (7%), Typhoid (5%), Dengue Fever (4%), Whooping Cough (3%), Measles (2%)

**Seasonal Pattern**: Monsoon (July-September) spike - 30% increase

**Top Medicines**: 
- Amoxicillin/Ceftiaxone (antibiotics)
- Chloroquine/Artemether (antimalarials)
- Ciprofloxacin (for gastrointestinal infections)

#### B. **RESPIRATORY DISEASES (20% - 9,000 patients)**
Primary diseases: URTI (15%), Asthma (8%), COPD (6%), Pneumonia (6%), Acute Bronchitis (5%)

**Seasonal Pattern**: Winter (October-March) spike - 35% increase

**Top Medicines**:
- Amoxicillin (bacteria)
- Salbutamol inhaler (for asthma/COPD)
- Paracetamol (fever/pain)

#### C. **NON-COMMUNICABLE DISEASES (16% - 7,200 patients)**
Primary diseases: Diabetes Mellitus (12%), Hypertension (10%), Anemia (5%), Protein-Energy Malnutrition (4%)

**Seasonal Pattern**: Year-round consistent

**Top Medicines**:
- Metformin (diabetes)
- Amlodipine/Lisinopril (hypertension)
- Iron supplements (anemia)

---

## 3. MEDICINE-WISE PATTERNS

### A. TOP ANTIBIOTICS (40% of medicine prescription rate)
1. **Amoxicillin/Clavulanate** - 18% usage
   - Indications: Respiratory infections, skin infections, UTI
   - Dosage: 500mg 3x/day (8-10 years), 1000mg 3x/day (adults)

2. **Ceftriaxone** - 12% usage
   - Indications: Severe infections, pneumonia, meningitis
   - Dosage: 1-2g IV/IM daily or divided

3. **Azithromycin** - 10% usage
   - Indications: Atypical respiratory infections
   - Dosage: 500mg day 1, then 250mg daily

### B. TOP MAINTENANCE MEDICINES (33% of medicine prescription rate)
1. **Metformin** - 14% usage
   - Indication: Type 2 Diabetes
   - Dosage: 500-2000mg daily (divided)

2. **Amlodipine** - 11% usage
   - Indication: Hypertension, Angina
   - Dosage: 5-10mg once daily

3. **Lisinopril** - 8% usage
   - Indication: Hypertension, Heart Failure
   - Dosage: 10-40mg once daily

### C. TOP PEDIATRIC MEDICINES (41% of pediatric prescriptions)
1. **Paracetamol (Panadol) Syrup** - 16% usage
   - Indication: Fever, mild pain
   - Dosage: 10-15mg/kg/dose, max 5 doses/day

2. **ORS (Oral Rehydration Solution)** - 13% usage
   - Indication: Dehydration, gastroenteritis
   - Dosage: 50-100ml/kg over 4 hours

3. **Amoxicillin Suspension** - 12% usage
   - Indication: Respiratory infections, skin infections
   - Dosage: 25-45mg/kg/day divided in 3 doses

---

## 4. AGE GROUP DISTRIBUTION

| Age Group | Percentage | Primary Conditions |
|-----------|-----------|-------------------|
| 0-5 years (Infant/Toddler) | 15% | URTI, Gastroenteritis, Immunization |
| 5-14 years (Child) | 12% | URTI, Tuberculosis, Malnutrition |
| 15-35 years (Young Adult) | 22% | Respiratory infections, Malaria, Typhoid |
| 35-60 years (Middle-aged) | 35% | Hypertension, Diabetes, Respiratory disease |
| 60+ years (Elderly) | 16% | COPD, Heart disease, Diabetes complications |

---

## 5. SEASONAL PATTERNS

| Season | Duration | Surge | Dominant Conditions |
|--------|----------|-------|-------------------|
| **Winter** | Oct-Mar | +35% | Respiratory infections, Asthma, COPD exacerbation |
| **Summer** | Apr-Jun | +20% | Gastroenteritis, Dehydration, Heat stroke |
| **Monsoon** | Jul-Sep | +30% | Malaria, Dengue, Typhoid, Waterborne diseases |
| **Fall/Rest** | - | +15% | Chronic disease management, routine care |

---

## 6. DATASET FILES DESCRIPTION

### A. `severity_classification.csv`
Lists all 4 severity levels with color codes, definitions, intervention types, and examples.

**Columns**: 
- Severity_ID
- Severity_Level
- Color_Code
- Definition
- Intervention_Type
- Average_Waiting_Time_Minutes
- Referral_Required
- Examples

### B. `diseases_distribution.csv`
Contains 15 major diseases with category, OPD volume percentage, age distribution, severity breakdown, and seasonal patterns.

**Columns**:
- Disease_ID
- Disease_Name
- Category
- OPD_Volume_Percentage
- Typical_Age_Group
- Severity_Distribution
- Management_Type
- Seasonal_Pattern

### C. `medicines_database.csv`
Database of 20 commonly prescribed medicines with indications, usage frequency, and dosage forms.

**Columns**:
- Medicine_ID
- Medicine_Name
- Generic_Name
- Category
- Typical_Use_Cases
- Dosage_Form
- Age_Group
- Severity_Level
- Frequency_in_OPD_Percentage

### D. `opd_statistics.json`
Comprehensive OPD statistics including severity distribution, disease-wise breakdown, top medicines by category, gender/age distribution, and seasonal patterns.

### E. `sample_patient_records.csv`
20 de-identified sample patient records showing realistic OPD visit documentation with diagnoses, severity levels, prescribed medicines, vital signs, and outcomes.

**Columns**:
- Patient_ID
- Registration_Date
- Age
- Gender
- Primary_Diagnosis
- Disease_Category
- Severity_Level
- Assigned_Doctor
- Medicine_Prescribed
- Dosage
- Duration_Days
- Vital_Signs_Note
- OPD_Visit_Outcome
- Referral_Status

---

## 7. DATA QUALITY STANDARDS

### Validation Rules
1. Severity levels must be one of: Mild, Moderate, Severe, Critical
2. Disease categories must match provided list
3. Patient ages must be numeric (0-120)
4. Medicine prescriptions must reference valid medicine IDs
5. All vital signs should be within physiological ranges

### Gender Distribution
- Male: 52%
- Female: 48%

---

## 8. USE CASES & APPLICATIONS

1. **Hospital Management**: Resource allocation, staffing requirements
2. **Inventory Management**: Medicine stock planning based on OPD volume
3. **Epidemiology**: Disease tracking and seasonal preparedness
4. **Training**: New staff familiarization with common conditions
5. **Research**: OPD pattern analysis and outcome studies
6. **Quality Assurance**: Benchmarking against national standards

---

## 9. NOTES & SPECIAL CONSIDERATIONS

- Data reflects **typical Pakistani civil hospital patterns**
- "Big Three" diseases account for 60% of OPD volume
- Winter season shows 35% patient surge
- Pediatric population (0-14 years) represents 27% of total OPD
- Critical cases (5%) require immediate ER/ICU referral
- Chronic disease management concentrated in 35-60 age group

---

**Dataset Version**: 1.0  
**Last Updated**: February 2026  
**Data Period**: Annual Average  
**Total OPD Patients Sample**: 45,000  
**Records Included**: 20+ sample patient cases

