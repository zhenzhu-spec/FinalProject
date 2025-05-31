# Yelp Cleaned Data Analysis

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set consistent visual style
sns.set_theme(style="whitegrid")

# Load and clean the dataset
df = pd.read_csv("yelp_cleaned.csv")
df = df.dropna(subset=['stars', 'price', 'restaurant_type', 'city'])

# Quick data validation
print("✅ Loaded Yelp dataset")
print("🔢 Total records after cleaning:", len(df))
print("📍 Unique cities:", df['city'].nunique())
print("🍽️ Unique restaurant types:", df['restaurant_type'].nunique())

# --- 1. Top 10 Cities by Average Star Rating ---
avg_stars_by_city = df.groupby('city')['stars'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_stars_by_city.values, y=avg_stars_by_city.index, palette='viridis')
plt.title('Top 10 Cities by Average Rating')
plt.xlabel('Average Stars')
plt.ylabel('City')
plt.tight_layout()
plt.show()

# --- 2. Price Level vs Rating: Boxplot and Regression ---
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='price', y='stars', palette='pastel')
plt.title('Rating Distribution by Price Level')
plt.xlabel('Price Level')
plt.ylabel('Stars')
plt.tight_layout()
plt.show()

sns.lmplot(data=df, x='price', y='stars', aspect=1.5, scatter_kws={"alpha": 0.5})
plt.title('Price vs Rating (Linear Fit)')
plt.xlabel('Price Level')
plt.ylabel('Stars')
plt.tight_layout()
plt.show()

# --- 3. Top 10 Restaurant Types by Count ---
top_types = df['restaurant_type'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_types.values, y=top_types.index, order=top_types.index, palette='magma')
plt.title('Top 10 Restaurant Types')
plt.xlabel('Count')
plt.ylabel('Restaurant Type')
plt.tight_layout()
plt.show()

# --- 4. Heatmap: Average Rating by State and Price ---
pivot = df.pivot_table(index='state', columns='price', values='stars', aggfunc='mean')
pivot = pivot.sort_index()

plt.figure(figsize=(10, 8))
sns.heatmap(pivot, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5, linecolor='gray')
plt.title('Average Rating by State and Price Level')
plt.xlabel('Price Level')
plt.ylabel('State')
plt.tight_layout()
plt.show()
