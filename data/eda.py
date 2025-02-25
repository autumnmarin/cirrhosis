import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from scipy.stats import zscore
from sklearn.preprocessing import LabelEncoder
import os

seed = 87
script_dir = os.path.dirname(os.path.abspath(__file__))
train_path = os.path.join(script_dir,  "train.csv")

df = pd.read_csv(train_path)



# ==========================
# Step 1: Basic Exploration
# ==========================
print("\nBasic Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Check first few rows
print("\nFirst few rows:")
print(df.head())

# ==========================
# Step 2: Missing Values & Duplicates
# ==========================
print("\nMissing Values Count:")
print(df.isnull().sum()[df.isnull().sum() > 0].sort_values(ascending=False))

# Visualizing Missing Data
plt.figure(figsize=(10, 5))
msno.matrix(df)
plt.title("Missing Values Heatmap")
plt.show()

# Check for Duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# ==========================
# Step 3: Outliers Detection
# ==========================
# Calculate Z-score for numerical columns
numerical_features = df.select_dtypes(include=[np.number]).columns
z_scores = np.abs(zscore(df[numerical_features].dropna()))
outliers = (z_scores > 3).sum()
print("\nOutliers per column (Z-score > 3):")
print(outliers[outliers > 0].sort_values(ascending=False))

# Boxplot for Key Features
plt.figure(figsize=(15, 5))
sns.boxplot(data=df[numerical_features])
plt.xticks(rotation=90)
plt.title("Boxplot of Numerical Features")
plt.show()

# ==========================
# Step 4: Univariate & Bivariate Analysis
# ==========================
# Histogram of SalePrice
plt.figure(figsize=(8, 5))
sns.histplot(df['SalePrice'], bins=30, kde=True)
plt.title("Distribution of Sale Price")
plt.show()

# Pairplot of Key Features
selected_features = ['SalePrice', 'GrLivArea', 'TotalBsmtSF', 'GarageArea', 'YearBuilt']
sns.pairplot(df[selected_features])
plt.show()

# ==========================
# Step 5: Feature Correlations
# ==========================
# Compute Correlation Matrix
corr_matrix = df.corr()

# Visualizing Correlations
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, cmap="coolwarm", annot=False)
plt.title("Feature Correlation Heatmap")
plt.show()

# Top 10 Correlated Features with SalePrice
print("\nTop 10 features most correlated with SalePrice:")
print(corr_matrix['SalePrice'].abs().sort_values(ascending=False)[1:11])

# ==========================
# Step 6: Visualizing Key Features
# ==========================
# Categorical Feature Countplots
categorical_features = df.select_dtypes(include=['object']).columns
for cat in categorical_features[:5]:  # Limiting to first 5 for readability
    plt.figure(figsize=(10, 5))
    sns.countplot(y=df[cat], order=df[cat].value_counts().index, palette="viridis")
    plt.title(f"Distribution of {cat}")
    plt.show()

# ==========================
# Step 7: Categorical Data Encoding & Checks
# ==========================
# Encode categorical variables for quick analysis
le = LabelEncoder()
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = le.fit_transform(df[col].astype(str))

print("\nSample Encoded Data:")
print(df.head())

print("\nEDA Completed Successfully!")
