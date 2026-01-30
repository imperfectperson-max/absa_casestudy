#!/usr/bin/env python3
"""
Generate missing visualization images from the CSV data files.
This script creates images that should be referenced in the documentation.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import sys

# Constants
TOP_N_FEATURES = 10  # Number of top features to display in charts
OUTPUT_DPI = 150  # Resolution for output images (150 DPI provides good quality for documentation)

# Color palette for risk levels (consistent across all visualizations)
RISK_COLORS = {
    'High': '#d62728',      # Red
    'Moderate': '#ff7f0e',  # Orange
    'Low': '#2ca02c'        # Green
}

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Ensure images directory exists
os.makedirs('images', exist_ok=True)

print("Loading data...")

# Check if required CSV files exist
required_files = ['CZR_Model_Coefficients.csv', 'CZR_2026_Flood_Forecast.csv']
for filename in required_files:
    if not os.path.exists(filename):
        print(f"Error: Required file '{filename}' not found!")
        print("Please ensure the CSV files are in the current directory.")
        sys.exit(1)

# Load the CSV files
try:
    df_coefficients = pd.read_csv('CZR_Model_Coefficients.csv')
    df_forecast = pd.read_csv('CZR_2026_Flood_Forecast.csv')
except Exception as e:
    print(f"Error loading CSV files: {e}")
    sys.exit(1)

# 1. Feature Importance Chart (Top N)
print("Generating feature importance chart...")
fig, ax = plt.subplots(figsize=(12, 8))
top_n = df_coefficients.nlargest(TOP_N_FEATURES, 'Abs_Coefficient')
colors = ['#d62728' if c > 0 else '#1f77b4' for c in top_n['Coefficient']]
ax.barh(range(len(top_n)), top_n['Abs_Coefficient'], color=colors)
ax.set_yticks(range(len(top_n)))
ax.set_yticklabels(top_n['Feature'])
ax.set_xlabel('Absolute Coefficient Value', fontsize=12, fontweight='bold')
ax.set_title(f'Top {TOP_N_FEATURES} Feature Importance (Linear Regression Model)', fontsize=14, fontweight='bold')
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('images/feature_importance.png', dpi=OUTPUT_DPI, bbox_inches='tight')
plt.close()
print("✓ Saved: images/feature_importance.png")

# 2. Feature Coefficients Chart (showing positive/negative with colors)
print("Generating feature coefficients chart...")
fig, ax = plt.subplots(figsize=(12, 8))
top_features = df_coefficients.nlargest(TOP_N_FEATURES, 'Abs_Coefficient')
colors = ['#2ca02c' if c > 0 else '#d62728' for c in top_features['Coefficient']]
ax.barh(range(len(top_features)), top_features['Coefficient'], color=colors)
ax.set_yticks(range(len(top_features)))
ax.set_yticklabels(top_features['Feature'])
ax.set_xlabel('Coefficient Value', fontsize=12, fontweight='bold')
ax.set_title(f'Top {TOP_N_FEATURES} Feature Coefficients (Linear Regression Model)', fontsize=14, fontweight='bold')
ax.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)
# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#2ca02c', label='Positive Impact'),
                   Patch(facecolor='#d62728', label='Negative Impact')]
ax.legend(handles=legend_elements, loc='lower right')
plt.tight_layout()
plt.savefig('images/feature_coefficients.png', dpi=OUTPUT_DPI, bbox_inches='tight')
plt.close()
print("✓ Saved: images/feature_coefficients.png")

# 3. 2026 Flood Severity Forecast (Monthly)
print("Generating 2026 flood severity forecast...")
fig, ax = plt.subplots(figsize=(14, 6))
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
colors = [RISK_COLORS[row['flood_risk_level']] for _, row in df_forecast.iterrows()]

bars = ax.bar(months, df_forecast['predicted_flood_severity'], color=colors, alpha=0.8, edgecolor='black')
ax.set_xlabel('Month (2026)', fontsize=12, fontweight='bold')
ax.set_ylabel('Predicted Flood Severity', fontsize=12, fontweight='bold')
ax.set_title('2026 Monthly Flood Severity Forecast', fontsize=14, fontweight='bold')
ax.axhline(y=20, color='red', linestyle='--', linewidth=1, alpha=0.5, label='High Risk Threshold')
ax.grid(axis='y', alpha=0.3)

# Add risk level labels
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=RISK_COLORS['High'], label='High Risk'),
                   Patch(facecolor=RISK_COLORS['Moderate'], label='Moderate Risk'),
                   Patch(facecolor=RISK_COLORS['Low'], label='Low Risk')]
ax.legend(handles=legend_elements, loc='upper left')

plt.tight_layout()
plt.savefig('images/forecast_2026_severity.png', dpi=OUTPUT_DPI, bbox_inches='tight')
plt.close()
print("✓ Saved: images/forecast_2026_severity.png")

# 4. 2026 Precipitation and Dam Level Forecast
print("Generating 2026 precipitation and dam level forecast...")
fig, ax1 = plt.subplots(figsize=(14, 6))

# Precipitation on left y-axis
color = '#1f77b4'
ax1.set_xlabel('Month (2026)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Precipitation (mm)', color=color, fontsize=12, fontweight='bold')
line1 = ax1.plot(months, df_forecast['precipitation'], color=color, marker='o', linewidth=2, markersize=8, label='Precipitation')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(axis='y', alpha=0.3)

# Dam level on right y-axis
ax2 = ax1.twinx()
color = '#ff7f0e'
ax2.set_ylabel('Avg Dam Level (%)', color=color, fontsize=12, fontweight='bold')
line2 = ax2.plot(months, df_forecast['avg_dam_level'], color=color, marker='s', linewidth=2, markersize=8, label='Avg Dam Level')
ax2.tick_params(axis='y', labelcolor=color)

# Title and legend
plt.title('2026 Precipitation and Dam Level Forecast', fontsize=14, fontweight='bold', pad=20)
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

plt.tight_layout()
plt.savefig('images/forecast_2026_climate.png', dpi=OUTPUT_DPI, bbox_inches='tight')
plt.close()
print("✓ Saved: images/forecast_2026_climate.png")

# 5. Risk Distribution Chart
print("Generating risk distribution chart...")
fig, ax = plt.subplots(figsize=(10, 6))
risk_counts = df_forecast['flood_risk_level'].value_counts()
colors = [RISK_COLORS[level] for level in risk_counts.index]
wedges, texts, autotexts = ax.pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%',
                                    colors=colors, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax.set_title('2026 Flood Risk Distribution', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/risk_distribution_2026.png', dpi=OUTPUT_DPI, bbox_inches='tight')
plt.close()
print("✓ Saved: images/risk_distribution_2026.png")

print("\n" + "="*60)
print("✓ All images generated successfully!")
print("="*60)
print("\nGenerated images:")
print("  1. images/feature_importance.png")
print("  2. images/feature_coefficients.png")
print("  3. images/forecast_2026_severity.png")
print("  4. images/forecast_2026_climate.png")
print("  5. images/risk_distribution_2026.png")
print("\nExisting images:")
print("  • images/correlation_matrix.png")
print("  • images/outlier_detection.png")
print("  • images/seasonal_patterns.png")
