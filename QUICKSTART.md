# Quick Start Guide

Get up and running with the CZR Insurance Flood Prediction Analysis in minutes!

---

## ⚡ Quick Setup (5 minutes)

### Step 1: Access the Notebook

**Option A: Google Colab (Recommended)**
1. Open [Google Colab](https://colab.research.google.com)
2. Upload `Absa_CZR_Insurance_Flood_Prediction_Analysis.ipynb`
3. Click "Runtime" → "Run all"

**Option B: Local Jupyter**
```bash
# Install Jupyter
pip install jupyter pandas numpy matplotlib seaborn scikit-learn openpyxl

# Launch notebook
jupyter notebook Absa_CZR_Insurance_Flood_Prediction_Analysis.ipynb
```

### Step 2: Upload Required Data

When prompted, upload:
- `Copy_of_Absa_QYF_Climate_Risk_Data_2026.xlsx` (Required)

### Step 3: Execute and Review

The notebook will automatically:
1. ✅ Load and clean data
2. ✅ Generate visualizations
3. ✅ Train and compare models
4. ✅ Create 2026 predictions
5. ✅ Export CSV files

**Expected Runtime:** 2-3 minutes

---

## 📂 Output Files Explained

After execution, you'll have three CSV files:

### 1. CZR_2026_Flood_Forecast.csv
**What it contains:** Monthly flood predictions for 2026  
**Use it for:** Pricing decisions, capital planning, risk communication  
**Key column:** `flood_risk_level` (Low/Moderate/High)

**Quick view:**
```bash
head -5 CZR_2026_Flood_Forecast.csv
```

### 2. CZR_Model_Coefficients.csv
**What it contains:** Feature importance rankings  
**Use it for:** Understanding what drives flood risk  
**Key column:** `Coefficient` (positive = increases risk)

**Quick insight:**
```python
import pandas as pd
df = pd.read_csv('CZR_Model_Coefficients.csv')
print(df.nlargest(3, 'Abs_Coefficient'))
# Shows: precipitation, avg_dam_level, dam_level_ma3
```

### 3. CZR_Model_Comparison.csv
**What it contains:** Performance of different ML models  
**Use it for:** Validating model selection  
**Key column:** `Test R²` (higher = better)

**Quick check:**
```python
df = pd.read_csv('CZR_Model_Comparison.csv')
best = df.loc[df['Test R²'].idxmax(), 'Model']
print(f"Best model: {best}")
# Shows: Linear Regression
```

---

## 🎯 Common Use Cases

### Use Case 1: Identify High-Risk Months

```python
import pandas as pd

# Load forecast
df = pd.read_csv('CZR_2026_Flood_Forecast.csv')

# Filter high-risk months
high_risk = df[df['flood_risk_level'] == 'High']
print("Alert: High risk in months:", high_risk['month'].tolist())

# Output: [8] (August)
```

### Use Case 2: Calculate Premium Adjustments

```python
# Define multipliers
multipliers = {'Low': 1.0, 'Moderate': 1.15, 'High': 1.30}

# Apply to forecast
df['premium_multiplier'] = df['flood_risk_level'].map(multipliers)
df['adjusted_premium'] = 1000 * df['premium_multiplier']  # Base: R1000

# View results
print(df[['month', 'flood_risk_level', 'adjusted_premium']])
```

### Use Case 3: Estimate Capital Requirements

```python
# Assumptions
policy_count = 10000
avg_claim = 50000
base_claim_rate = 0.01  # 1%

# Calculate by risk level
risk_multipliers = {'Low': 1.0, 'Moderate': 2.5, 'High': 7.5}

df['claim_rate'] = df['flood_risk_level'].map(risk_multipliers) * base_claim_rate
df['expected_claims'] = policy_count * df['claim_rate']
df['capital_needed'] = df['expected_claims'] * avg_claim

# Quarterly totals
df['quarter'] = (df['month'] - 1) // 3 + 1
quarterly = df.groupby('quarter')['capital_needed'].sum()
print("Capital by quarter:\n", quarterly)
```

### Use Case 4: Visualize Risk Timeline

```python
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('CZR_2026_Flood_Forecast.csv')

# Create visualization
plt.figure(figsize=(12, 6))
colors = {'Low': 'green', 'Moderate': 'orange', 'High': 'red'}
bar_colors = [colors[level] for level in df['flood_risk_level']]

plt.bar(df['month'], df['predicted_flood_severity'], color=bar_colors)
plt.xlabel('Month')
plt.ylabel('Flood Severity')
plt.title('2026 Flood Risk Timeline')
plt.xticks(range(1, 13))
plt.axhline(y=20, color='red', linestyle='--', label='High Risk Threshold')
plt.legend()
plt.tight_layout()
plt.savefig('flood_risk_timeline.png')
plt.show()
```

---

## 🔍 Understanding the Analysis

### What the Model Does

1. **Inputs:** Climate variables (precipitation, temperature, humidity, etc.) + Dam levels
2. **Processing:** Linear regression model trained on 2017-2021 data
3. **Outputs:** Flood severity scores and risk levels for 2026

### Why Linear Regression?

✅ **96.85% accuracy** on test data  
✅ **Interpretable** coefficients  
✅ **Minimal overfitting** (2.6% gap)  
✅ **Fast predictions** for real-time use

### Key Predictors (in order)

1. **Precipitation** (7.11) - Most important
2. **Dam Level** (2.54) - Second most important
3. **Humidity** (1.52) - Moderate importance
4. **Temperature** (-0.89) - Inverse relationship

---

## 📊 Interpreting Visualizations

### 1. Time Series Plots
**Shows:** Historical trends over 60 months  
**Look for:** Seasonal patterns, outliers, trends

### 2. Correlation Heatmap
**Shows:** Relationships between variables  
**Look for:** Strong correlations (|r| > 0.5) with flood risk

### 3. Feature Importance Bar Chart
**Shows:** Coefficient magnitudes  
**Look for:** Longest bars = most important predictors

### 4. Predicted vs Actual
**Shows:** Model accuracy  
**Look for:** Points close to diagonal line = good predictions

### 5. Residual Plots
**Shows:** Prediction errors  
**Look for:** Random scatter = model assumptions satisfied

### 6. 2026 Forecast Bar Chart
**Shows:** Monthly severity scores  
**Look for:** Peaks in June-July (high risk period)

---

## ⚠️ Important Caveats

### Model Limitations

1. **Historical Data:** Only 5 years (2017-2021) - may not capture rare extreme events
2. **Geographic Scope:** Western Cape only - not applicable to other regions
3. **Linear Assumptions:** May underestimate extreme severity
4. **Future Uncertainty:** Climate change could alter patterns

### What to Do

- **Don't:** Rely solely on model predictions for major decisions
- **Do:** Use as one input alongside expert judgment, historical claims, and real-time monitoring
- **Best Practice:** Monthly model updates with new observed data

---

## 🆘 Troubleshooting

### Problem: Notebook won't run

**Solution:**
```python
# Install missing packages
!pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

### Problem: Data file not found

**Solution:**
1. Ensure file is named exactly: `Copy_of_Absa_QYF_Climate_Risk_Data_2026.xlsx`
2. Upload to same directory as notebook
3. Check file hasn't been corrupted during upload

### Problem: CSV files not generated

**Solution:**
1. Run all cells completely (don't interrupt)
2. Check for error messages in output
3. Verify model training completed successfully

### Problem: Plots not displaying

**Solution (Colab):**
```python
# Run this in a cell
%matplotlib inline
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12, 6)
```

**Solution (Jupyter):**
```python
%matplotlib notebook
```

---

## 📚 Next Steps

### Immediate Actions

1. **Review the forecasts:** Identify high-risk month (August)
2. **Calculate financial impact:** Use capital requirement formula
3. **Communicate with stakeholders:** Share insights with underwriting team

### Deep Dive

1. **Read INSIGHTS.md:** Detailed analysis and business recommendations
2. **Read DATA_DICTIONARY.md:** Field definitions and usage examples
3. **Review the notebook:** Understand each analysis step

### Advanced Usage

1. **Customize the model:** Adjust parameters or try different algorithms
2. **Add new features:** Incorporate additional climate variables
3. **Extend predictions:** Forecast beyond 2026 with updated data

---

## 📞 Getting Help

### Documentation

- **README.md:** Project overview and high-level insights
- **INSIGHTS.md:** Detailed findings and business recommendations
- **DATA_DICTIONARY.md:** CSV field definitions and usage
- **This file:** Quick start and common tasks

### Support

- **Technical Issues:** Review troubleshooting section above
- **Business Questions:** Consult INSIGHTS.md recommendations
- **Data Questions:** See DATA_DICTIONARY.md for field definitions

---

## ✅ Checklist for First-Time Users

- [ ] Uploaded notebook to Colab or Jupyter
- [ ] Uploaded data file (xlsx)
- [ ] Executed all cells successfully
- [ ] Generated three CSV output files
- [ ] Identified high-risk month (August)
- [ ] Reviewed feature importance (precipitation, dam level)
- [ ] Calculated premium adjustments for your use case
- [ ] Read README.md for project overview
- [ ] Bookmarked INSIGHTS.md for detailed analysis
- [ ] Saved DATA_DICTIONARY.md for reference

**Congratulations! You're now ready to use the flood prediction analysis for business decisions. 🎉**

---

**Last Updated:** January 30, 2026  
**Version:** 1.0  
**Estimated Reading Time:** 10 minutes
