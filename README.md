# Yelp Ratings Analysis

> Explore restaurant ratings across U.S. cities using Yelp business data.

## Overview
This project analyzes Yelp data to uncover patterns in restaurant ratings by city, price level, and restaurant type.

## Visualizations

### 1. Top 10 Cities by Average Rating
![Top Cities by Rating](images/top_cities_by_rating.jpg)

### 2. Rating Distribution by Price Level (Boxplot)
![Price vs Rating Boxplot](images/price_vs_rating_boxplot.jpg)

### 3. Rating vs Price Level (Linear Fit)
![Price vs Rating Regression](images/price_vs_rating_regression.jpg)

### 4. Top 10 Restaurant Types
![Top Restaurant Types](images/top_restaurant_types.jpg)

### 5. Average Rating by State and Price Level (Heatmap)
![Heatmap State Price](images/heatmap_state_price.jpg)


## Project Objectives
- Identify top-rated cities
- Analyze price vs rating correlation
- Examine restaurant type distribution

## Files in This Repository
| File | Description |
|------|-------------|
| `analysis.ipynb` | Main notebook with all visualizations |
| `clean_business.py` | Script to preprocess Yelp data |
| `yelp_academic_dataset_business.json.zip` | Raw dataset (compressed) |
| `yelp_cleaned.csv.zip` | Cleaned dataset (compressed) |

## How to Run
1. Clone the repository
2. Unzip datasets
3. Run `analysis.ipynb` in Jupyter or VSCode

## Environment
- Python 3.10+
- pandas, seaborn, matplotlib, folium

