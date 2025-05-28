# Yelp Ratings Analysis

This project analyzes Yelp business data to uncover patterns in restaurant ratings across different cities, price levels, and restaurant types.

## Project Objectives
- Identify the top cities by average Yelp rating
- Explore the relationship between price level and rating
- Highlight the most common restaurant types
- Visualize regional rating patterns using heatmaps

## Files in This Repository
| File | Description |
|------|-------------|
| `analysis.ipynb` | Main Jupyter Notebook for analysis and visualizations |
| `clean_business.py` | Script to preprocess raw Yelp business data |
| `yelp_academic_dataset_business.json.zip` | Compressed version of the raw Yelp business dataset |
| `yelp_cleaned.csv.zip` | Compressed version of the cleaned dataset |

## Visualizations Included
- Top 10 cities by average star rating
- Boxplot and regression: price level vs rating
- Most frequent restaurant types
- Heatmap of average rating by state and price level

## Tools and Libraries
- Python (pandas, seaborn, matplotlib, numpy)
- Jupyter Notebook

## How to Use
1. Run `clean_business.py` to generate the cleaned dataset.
2. Open `analysis.ipynb` in Jupyter Notebook and run all cells.

## Notes
The dataset used is part of Yelp’s academic dataset. This analysis focuses on businesses in the food and restaurant category only.
