# Data Validation Rules & Implementation Guide

## Validation Rules for Dataset Input

### 1. SEVERITY LEVEL VALIDATION
```
Valid Values: Mild, Moderate, Severe, Critical
Rule: Case-sensitive, exact match required
Severity Color Mapping:
  - Mild → Green (SEV001)
  - Moderate → Yellow (SEV002)
  - Severe → Orange (SEV003)
  - Critical → Red (SEV004)
```

### 2. DISEASE VALIDATION
```
Valid Disease Categories:
  - Infectious Diseases
  - Respiratory
  - Non-Communicable
  
Valid diseases: See diseases_distribution.csv
Must include Disease_ID reference
```

### 3. AGE VALIDATION
```
Range: 0-120 years
Format: Numeric values only
Age Group Mapping:
  - 0-5: Infant/Toddler
  - 5-14: Child
  - 15-35: Young Adult
  - 35-60: Middle-aged
  - 60+: Elderly
```

### 4. GENDER VALIDATION
```
Valid Values: M, F (or Male, Female)
Distribution Target:
  - Male: 52%
  - Female: 48%
```

### 5. VITAL SIGNS VALIDATION
```
Blood Pressure (mmHg):
  Normal: 90-140 systolic / 60-90 diastolic
  Alert if: <90 or >160 systolic

Temperature (°F):
  Normal: 97-99
  Mild fever: 100-101
  Moderate fever: 101.5-102.5
  High fever: >102.5 (may indicate SEVERE/CRITICAL)

Heart Rate (bpm):
  Normal: 60-100
  Alert if: <40 or >120

Respiratory Rate (/min):
  Normal: 12-20
  Alert if: >26

SpO2 (%):
  Normal: 95-100
  Mild hypoxemia: 90-95 (possible MODERATE)
  Alert: <90 (SEVERE/CRITICAL)
```

### 6. MEDICINE VALIDATION
```
Format: Valid Medicine_ID from medicines_database.csv
Dosage must be specified
Duration must be numeric (days)
Age-appropriate medicine selection

Invalid combinations:
  - Adult medicine for pediatric patient
  - Dosage exceeding maximum for age/weight
  - Contraindicated medicine combinations
```

### 7. VISIT OUTCOME VALIDATION
```
Valid values:
  - Discharged
  - Admitted
  - Referred to [Department]
  - Scheduled Revisit
  - LAMA (Left Against Medical Advice)
  - Deceased (in critical cases)
```

### 8. REFERRAL VALIDATION
```
Severe/Critical cases: MUST have Referral_Status = Yes
Referral destination should be specified:
  - Emergency Room
  - Medicine Ward
  - Pediatric Ward
  - ICU/Intensive Care
  - Cardiology
  - Other department
```

---

## VALIDATION CHECKLIST

### For Each Patient Record:
- [ ] Patient_ID is unique
- [ ] Age is between 0-120
- [ ] Gender is M or F
- [ ] Primary_Diagnosis exists in diseases list
- [ ] Disease_Category matches diagnosis
- [ ] Severity_Level is valid (Mild/Moderate/Severe/Critical)
- [ ] Temperature is in °F and between 95-106
- [ ] BP follows systolic/diastolic format
- [ ] HR is between 40-180 bpm
- [ ] SpO2 is between 70-100% (if recorded)
- [ ] Medicine_ID exists in medicines database
- [ ] Dosage is age-appropriate
- [ ] Duration is positive number
- [ ] OPD_Visit_Outcome is from valid list
- [ ] Referral_Status = Yes if Severe/Critical
- [ ] All mandatory fields are filled

---

## DATA QUALITY STANDARDS

### Completeness
- No empty mandatory fields
- All foreign key references resolvable
- Dates in YYYY-MM-DD format

### Accuracy
- Severity matches clinical presentation
- Vital signs are physiologically plausible
- Medicine selection matches diagnosis/severity
- Dosing follows standard guidelines

### Consistency
- Age-appropriate treatments
- Expected medicines for disease
- Outcomes align with severity
- Referral logic is sound

### Timeliness
- Records entered same day as visit
- No future-dated records
- Dates in proper sequence

---

## COMMON ERRORS & CORRECTIONS

| Error | Impact | Fix |
|-------|--------|-----|
| Mild severity + Respiratory distress + SpO2 90% | Severity mismatch | Change to SEVERE |
| Pediatric patient given adult dosage | Patient safety risk | Adjust dosage per age |
| Moderate severity with no referral but needs admission | Process error | Add referral status |
| Disease category doesn't match diagnosis | Data integrity | Align with master diseases list |
| Future dates in records | Data quality | Correct to visit date |

---

## IMPORT CHECKLIST (Database/System)

**Before importing to Hospital System:**

1. **Validation Pass**
   - [ ] Run validation script against all records
   - [ ] Fix or flag errors
   - [ ] Document any manual corrections

2. **Data Cleaning**
   - [ ] Remove duplicate Patient_IDs
   - [ ] Standardize date formats
   - [ ] Trim whitespace
   - [ ] Correct case issues in categorical fields

3. **Mapping & Transformation**
   - [ ] Map Severity to system color codes
   - [ ] Map Disease_IDs to hospital ICD codes
   - [ ] Map Medicine_IDs to hospital formulary
   - [ ] Convert units if needed

4. **Integration**
   - [ ] Load to staging database
   - [ ] Run data warehouse validations
   - [ ] Verify referential integrity
   - [ ] Test reporting queries

5. **Go-Live**
   - [ ] User acceptance testing
   - [ ] Staff training on new data
   - [ ] Monitor for issues week 1
   - [ ] Create data backup

---

## SAMPLE VALIDATION SQL QUERIES

```sql
-- Check severity distribution
SELECT Severity_Level, COUNT(*) as Count,
  ROUND(COUNT(*)*100.0/(SELECT COUNT(*) FROM patients),1) as Percentage
FROM patients
GROUP BY Severity_Level
ORDER BY Percentage DESC;

-- Find records with missing vital signs
SELECT Patient_ID, Age, Severity_Level
FROM patients
WHERE OR BP IS NULL OR Temp IS NULL OR HR IS NULL
ORDER BY Severity_Level DESC;

-- Verify age-appropriate medicines
SELECT p.Patient_ID, p.Age, p.Medicine_Prescribed, m.Age_Group
FROM patients p
JOIN medicines_database m ON p.Medicine_Prescribed = m.Medicine_ID
WHERE p.Age < 2 AND m.Age_Group = 'Adult'
LIMIT 10;

-- Find referral mismatches
SELECT Patient_ID, Severity_Level, Referral_Status, OPD_Visit_Outcome
FROM patients
WHERE Severity_Level IN ('Severe','Critical') AND Referral_Status = 'No';

-- Disease distribution check
SELECT Disease_Category, COUNT(*) as Count,
  ROUND(COUNT(*)*100.0/(SELECT COUNT(*) FROM patients),1) as Percentage
FROM patients
GROUP BY Disease_Category
ORDER BY Percentage DESC;
```

---

**Version**: 1.0  
**Last Updated**: February 2026  
**Compliance**: Pakistani Hospital Standards, OPD Best Practices

