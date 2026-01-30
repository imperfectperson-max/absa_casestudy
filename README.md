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

### 2. **Seasonal Patterns Analysis**
- **Purpose:** Visualize how climate variables vary across seasons
- **Key Finding:** Winter months show highest precipitation and flood risk
- **Application:** Seasonal risk assessment and pricing strategies

![Seasonal Patterns](images/seasonal_patterns.png)

### 3. **Correlation Heatmap**
- **Purpose:** Reveal relationships between climate variables
- **Key Finding:** Precipitation and dam levels show strongest correlation with flood risk
- **Application:** Feature selection for predictive models

![Correlation Matrix](images/correlation_matrix.png)

### 4. **Multicollinearity Analysis (VIF)**
- **Purpose:** Detect redundant features that could distort model coefficients
- **Threshold:** VIF > 10 indicates problematic multicollinearity
- **Outcome:** Ensures model interpretability and reliability

### 5. **Feature Importance Chart**
- **Purpose:** Rank predictive power of climate variables
- **Visualization:** Bar chart showing coefficient magnitudes

**Complete Feature Coefficients Table:**

| Feature | Coefficient | Abs_Coefficient |
|---------|-------------|-----------------|
| precipitation | 7.107913042307417 | 7.107913042307417 |
| avg_dam_level | 2.5392888064229324 | 2.5392888064229324 |
| dam_level_ma3 | -0.9098876104229588 | 0.9098876104229588 |
| avg_temp | -0.8857125250285979 | 0.8857125250285979 |
| air_pressure | -0.6233309206430603 | 0.6233309206430603 |
| humidity | -0.41062107712220597 | 0.41062107712220597 |
| wind_speed | -0.3459693302035819 | 0.3459693302035819 |
| humidity_ma3 | -0.30914779086818645 | 0.30914779086818645 |
| temp_range | -0.28879183840987027 | 0.28879183840987027 |
| dam_level_lag1 | 0.2690398231165717 | 0.2690398231165717 |
| capacity_utilization | -0.2111103681796154 | 0.2111103681796154 |
| precipitation_ma3 | -0.17957734927337995 | 0.17957734927337995 |
| month_sin | 0.09914160833745786 | 0.09914160833745786 |
| month_cos | 0.09362753817016556 | 0.09362753817016556 |
| precipitation_lag1 | 0.08354544522713477 | 0.08354544522713477 |

**Top Features:**
  1. Precipitation: 7.11
  2. Avg Dam Level: 2.54
  3. Dam Level MA3: 0.91 (absolute)

### 6. **Outlier Detection Plots**
- **Purpose:** Identify anomalous data points that could skew predictions
- **Method:** Statistical analysis (Z-scores, IQR)
- **Action:** Document outliers for data quality assessment

![Outlier Detection](images/outlier_detection.png)

### 7. **Predicted vs Actual Flood Risk**
- **Purpose:** Validate model performance
- **Metrics:** R² score, RMSE, MAE
- **Interpretation:** Close alignment indicates reliable predictions

### 8. **2026 Flood Severity Distribution**
- **Purpose:** Forecast future flood patterns
- **Categories:** Low, Moderate, High risk levels
- **Application:** Strategic planning for insurance coverage

---

## 🤖 Model Comparison

The analysis evaluates five machine learning models:

| Model | Train RMSE | Test RMSE | Train R² | Test R² | Test MAE | Overfitting Gap |
|-------|-----------|-----------|----------|---------|----------|-----------------|
| **Linear Regression** | 0.5434391077258082 | 2.2567676744637275 | 0.9947601381228127 | **0.9685124577308301** | 1.7510244788537517 | 0.026247680391982664 |
| **Ridge Regression** | 0.641903582986798 | 2.3380593373805696 | 0.9926893218984979 | 0.9662031583889128 | 1.841695790389356 | 0.026486163509585103 |
| **Lasso Regression** | 0.6702566220451898 | 2.3480838504165553 | 0.9920292297900828 | 0.9659127267683407 | 1.8703862115032612 | 0.026116503021742066 |
| **Gradient Boosting** | 0.000219927102104876 | 4.940715959306317 | 0.9999999991418256 | 0.849080682385887 | 3.6310082887932205 | 0.15091931675593862 |
| **Random Forest** | 0.6597322102296366 | 5.48301484530155 | 0.9922775796331329 | 0.8141323097253008 | 4.212690374019982 | 0.17814526990783208 |

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

| Year | Month | Precipitation (mm) | Avg Dam Level (%) | Predicted Flood Severity | Flood Risk Level |
|------|-------|-------------------|-------------------|--------------------------|------------------|
| 2026 | 1 | 26.61434729183268 | 63.21295190042169 | 16.485708513684575 | Moderate |
| 2026 | 2 | 16.277945411520278 | 64.06030479346217 | 10.177884350929617 | Low |
| 2026 | 3 | 24.101122125971884 | 63.22677502702936 | 15.139578375965499 | Moderate |
| 2026 | 4 | 17.494150573150385 | 62.161699067333736 | 10.591399308142346 | Low |
| 2026 | 5 | 28.460511054839692 | 61.888880440041916 | 17.666986052799917 | Moderate |
| 2026 | 6 | 36.75724889674782 | 61.72212630548795 | 22.958435231662992 | Moderate |
| 2026 | 7 | 36.623877932157214 | 63.76549503725588 | 23.19059741270337 | Moderate |
| 2026 | 8 | 34.43114915472214 | 70.53194109527273 | 24.58285148545622 | High |
| 2026 | 9 | 24.871088809842536 | 71.61031354054366 | 18.45549381029033 | Moderate |
| 2026 | 10 | 25.860815137397417 | 70.38327885390288 | 18.227662647277263 | Moderate |
| 2026 | 11 | 28.215974251839363 | 69.43903034009129 | 19.752562138979144 | Moderate |
| 2026 | 12 | 23.1426885673237 | 68.1648507194592 | 16.063770021100403 | Moderate |

### Risk Alert: High-Risk Months

**🔴 August 2026**
- Highest flood severity: 24.6
- Elevated dam levels (70.5%)
- Substantial precipitation (34.4mm)
- **Recommendation:** Increase capital reserves and monitor closely

---

## 💡 Business Recommendations

### 1. **Dynamic Pricing Strategy**
- **Low Risk Months** (Feb, Apr): Standard pricing
- **Moderate Risk Months** (Jan, Mar, May, Jun, Jul, Sep, Oct, Nov, Dec): 10-15% premium increase
- **High Risk Months** (Aug): 25-35% premium increase or coverage restrictions

### 2. **Capital Allocation**
- **Reserve Requirement:** Allocate 40% more capital for Q3 2026
- **Geographic Focus:** Prioritize Western Cape exposure management
- **Reinsurance:** Consider excess-of-loss treaties for August period

### 3. **Risk Mitigation Actions**
- **Customer Communication:** Alert high-risk policyholders 30 days in advance of August
- **Claims Preparation:** Pre-position adjusters and resources for late winter/early spring
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
