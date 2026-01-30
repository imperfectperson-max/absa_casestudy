# CZR Insurance Group - Flood Prediction Analysis

## 🎯 Project Overview

This repository contains a comprehensive **climate risk assessment** for CZR Insurance Group, focusing on **flood prediction in the Western Cape region** (2017-2026). The analysis uses historical climate data and dam levels to predict flood frequency, severity, and associated risks to help optimize insurance pricing and capital allocation strategies.

**Analysis Period:** 2017-2021 (60 months historical data)  
**Forecast Period:** 2026 (12-month predictions)  
**Location:** Western Cape, South Africa

---

## 📊 Key Insights

### Critical Risk Factors Identified

1. **Precipitation** (Coefficient: 7.11)
   - Most significant predictor of flood events
   - Higher precipitation correlates strongly with flood risk
   - Historical range: ~10-90mm monthly

2. **Dam Levels** (Coefficient: 2.54)
   - Second-most important predictor
   - High dam capacity utilization increases flood spillover risk
   - Critical threshold: >70% capacity

3. **Humidity** (Coefficient: 1.52)
   - Moderate positive correlation with flood risk
   - Indicator of saturated atmospheric conditions

4. **Temperature Range** (Coefficient: -0.89 to -1.24)
   - Negative correlation suggests cooler, wetter conditions increase risk
   - Lower temperatures associated with flood events

### Flood Risk Definition

**Flood events are defined as periods when:**
- Precipitation is in the top 25% of observations, AND
- Dam levels are in the top 25% of observations

**Flood Severity Formula:**
```
Flood Severity = (Precipitation × Dam Level) / 100
```

---

## 📈 Visualizations Explained

### 1. **Time Series Analysis**
- **Purpose:** Track climate variables over 60 months
- **Key Variables:** Precipitation, temperature, humidity, dam levels
- **Insight:** Identifies seasonal patterns and anomalies

### 2. **Correlation Heatmap**
- **Purpose:** Reveal relationships between climate variables
- **Key Finding:** Precipitation and dam levels show strongest correlation with flood risk
- **Application:** Feature selection for predictive models

### 3. **Multicollinearity Analysis (VIF)**
- **Purpose:** Detect redundant features that could distort model coefficients
- **Threshold:** VIF > 10 indicates problematic multicollinearity
- **Outcome:** Ensures model interpretability and reliability

### 4. **Feature Importance Chart**
- **Purpose:** Rank predictive power of climate variables
- **Visualization:** Bar chart showing coefficient magnitudes
- **Top Features:**
  1. Precipitation: 7.11
  2. Avg Dam Level: 2.54
  3. Dam Level MA3: -0.91

### 5. **Outlier Detection Plots**
- **Purpose:** Identify anomalous data points that could skew predictions
- **Method:** Statistical analysis (Z-scores, IQR)
- **Action:** Document outliers for data quality assessment

### 6. **Predicted vs Actual Flood Risk**
- **Purpose:** Validate model performance
- **Metrics:** R² score, RMSE, MAE
- **Interpretation:** Close alignment indicates reliable predictions

### 7. **2026 Flood Severity Distribution**
- **Purpose:** Forecast future flood patterns
- **Categories:** Low, Moderate, High risk levels
- **Application:** Strategic planning for insurance coverage

---

## 🤖 Model Comparison

The analysis evaluates five machine learning models:

| Model | Train RMSE | Test RMSE | Test R² | Test MAE | Overfitting |
|-------|-----------|-----------|---------|----------|-------------|
| **Linear Regression** | 0.543 | 2.257 | **0.9685** | 1.751 | 0.026 |
| **Ridge Regression** | 0.642 | 2.338 | 0.9662 | 1.842 | 0.026 |
| **Lasso Regression** | 0.670 | 2.348 | 0.9659 | 1.870 | 0.026 |
| **Random Forest** | - | - | - | - | - |
| **Gradient Boosting** | 0.0002 | 4.941 | 0.8491 | 3.631 | 0.151 |

### Model Selection Rationale

**✅ Recommended Model: Linear Regression**
- **Best Test R²:** 0.9685 (explains 96.85% of variance)
- **Low Overfitting:** Gap of only 2.6%
- **Interpretable Coefficients:** Clear feature importance
- **Stable Performance:** Consistent across train/test sets

**⚠️ Gradient Boosting:** Despite perfect training performance, high test RMSE (4.941) and significant overfitting (15.1%) make it unsuitable for production use.

---

## 🔮 2026 Flood Predictions

### Monthly Forecast Summary

| Month | Precipitation (mm) | Dam Level (%) | Flood Severity | Risk Level |
|-------|-------------------|---------------|----------------|------------|
| January | 26.6 | 63.2 | 16.5 | Moderate |
| February | 16.3 | 64.1 | 10.2 | Low |
| March | 24.1 | 63.2 | 15.1 | Moderate |
| April | 17.5 | 62.2 | 10.6 | Low |
| May | 23.9 | 66.7 | 15.8 | Moderate |
| June | 36.8 | 71.6 | 24.6 | High |
| July | 31.0 | 68.5 | 21.0 | High |
| August | 28.4 | 65.9 | 18.4 | Moderate |
| September | 22.7 | 64.1 | 14.3 | Moderate |
| October | 20.5 | 62.5 | 12.6 | Low |
| November | 19.8 | 61.7 | 12.0 | Low |
| December | 25.2 | 63.8 | 15.8 | Moderate |

### Risk Alert: High-Risk Months

**🔴 June & July 2026**
- Highest precipitation levels (36.8mm and 31.0mm)
- Elevated dam levels (71.6% and 68.5%)
- Flood severity scores: 24.6 and 21.0
- **Recommendation:** Increase capital reserves and monitor closely

---

## 💡 Business Recommendations

### 1. **Dynamic Pricing Strategy**
- **Low Risk Months** (Feb, Apr, Oct, Nov): Standard pricing
- **Moderate Risk Months** (Jan, Mar, May, Aug, Sep, Dec): 10-15% premium increase
- **High Risk Months** (Jun, Jul): 25-35% premium increase or coverage restrictions

### 2. **Capital Allocation**
- **Reserve Requirement:** Allocate 40% more capital for Q2/Q3 2026
- **Geographic Focus:** Prioritize Western Cape exposure management
- **Reinsurance:** Consider excess-of-loss treaties for June-July period

### 3. **Risk Mitigation Actions**
- **Customer Communication:** Alert high-risk policyholders 30 days in advance
- **Claims Preparation:** Pre-position adjusters and resources for winter months
- **Data Enhancement:** Install additional rain gauges and dam sensors

### 4. **Model Improvement Roadmap**
- **Short-term (3 months):**
  - Integrate real-time weather forecasts
  - Add soil saturation data
  - Incorporate geographic clustering

- **Medium-term (6-12 months):**
  - Expand to 10-year historical dataset
  - Include socioeconomic vulnerability indices
  - Develop early warning system (7-14 day horizon)

- **Long-term (1-2 years):**
  - Machine learning ensemble models
  - Satellite imagery for flood extent mapping
  - Climate change scenario modeling (2030-2050)

---

## 📁 Repository Structure

```
absa_casestudy/
├── 📓 Absa_CZR_Insurance_Flood_Prediction_Analysis.ipynb  # Main analysis notebook
├── 📊 CZR_2026_Flood_Forecast.csv                         # Monthly predictions for 2026
├── 📊 CZR_Model_Coefficients.csv                          # Feature importance rankings
├── 📊 CZR_Model_Comparison.csv                            # Model performance metrics
├── 📖 README.md                                            # Project overview (this file)
├── 📖 QUICKSTART.md                                        # Quick start guide (⚡ Start here!)
├── 📖 INSIGHTS.md                                          # Detailed analysis findings
├── 📖 DATA_DICTIONARY.md                                   # CSV field descriptions
├── 📖 CONTRIBUTING.md                                      # Contribution guidelines
└── 🔧 .gitignore                                           # Git ignore rules
```

---

## 🚀 Getting Started

### ⚡ New Users Start Here!

**👉 Read [QUICKSTART.md](QUICKSTART.md) for a step-by-step guide to running the analysis in 5 minutes!**

### Prerequisites

```bash
# Required Python packages
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

### Running the Analysis

1. **Clone the repository:**
   ```bash
   git clone https://github.com/imperfectperson-max/absa_casestudy.git
   cd absa_casestudy
   ```

2. **Open the notebook:**
   - Upload `Absa_CZR_Insurance_Flood_Prediction_Analysis.ipynb` to Google Colab or Jupyter
   - Upload the required data file: `Copy_of_Absa_QYF_Climate_Risk_Data_2026.xlsx`

3. **Execute all cells:**
   - The notebook will automatically generate visualizations and CSV outputs
   - Review model comparisons and select the best-performing model
   - Export 2026 predictions for business use

### Output Files

After running the notebook, you'll generate:
- **CZR_2026_Flood_Forecast.csv:** Monthly flood predictions
- **CZR_Model_Coefficients.csv:** Feature importance analysis
- **CZR_Model_Comparison.csv:** Model performance comparison

**💡 For detailed field descriptions and usage examples, see [DATA_DICTIONARY.md](DATA_DICTIONARY.md)**

---

## 📚 Documentation Guide

### 🎯 Which Document Should I Read?

| Document | When to Use It | Reading Time |
|----------|----------------|--------------|
| **[QUICKSTART.md](QUICKSTART.md)** | First-time setup and running the analysis | 5 min |
| **[README.md](README.md)** | Project overview and key insights (you are here) | 10 min |
| **[INSIGHTS.md](INSIGHTS.md)** | Deep dive into findings and recommendations | 20 min |
| **[DATA_DICTIONARY.md](DATA_DICTIONARY.md)** | Understanding CSV outputs and fields | 10 min |
| **[CONTRIBUTING.md](CONTRIBUTING.md)** | Contributing to the project | 10 min |

### 📖 Documentation Summary

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes with step-by-step instructions
- **[INSIGHTS.md](INSIGHTS.md)** - Detailed analysis findings, model evaluation, and business recommendations
- **[DATA_DICTIONARY.md](DATA_DICTIONARY.md)** - Complete field definitions, formulas, and usage examples for all CSV files
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guidelines for contributing code, models, or documentation

---

## 👥 Contributors

**Climate Risk Analytics Team - QYF Group 1**  
**Organization:** CZR Insurance Group  
**Date:** January 30, 2026

**Want to contribute?** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines!

---

## 📄 License

This analysis is proprietary to CZR Insurance Group. For questions or access requests, contact the Climate Risk Analytics Team.

---

## 🔗 Quick Links

- [View Full Analysis Notebook](Absa_CZR_Insurance_Flood_Prediction_Analysis.ipynb)
- [2026 Forecast Data](CZR_2026_Flood_Forecast.csv)
- [Model Performance Comparison](CZR_Model_Comparison.csv)
- [Feature Importance Rankings](CZR_Model_Coefficients.csv)
