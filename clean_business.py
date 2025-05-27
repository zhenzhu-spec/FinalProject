import json
import pandas as pd
import zipfile
import os

# Unzip the Yelp data if the JSON file does not exist
zip_path = "yelp_academic_dataset_business.json.zip"
json_path = "yelp_academic_dataset_business.json"

if not os.path.exists(json_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()
    print(f"Unzipped {zip_path}")

# Load data from the JSON file
data = []
with open(json_path, 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))

# Keep only businesses categorized as "Restaurant"
df = pd.DataFrame(data)
df = df[df['categories'].str.contains("Restaurant", na=False)]

# Function to extract price level
def get_price(attr):
    try:
        return int(eval(attr).get("RestaurantsPriceRange2"))
    except:
        return None

# Select relevant columns and process them
df_cleaned = df[["name", "stars", "attributes", "categories", "city", "state"]].copy()
df_cleaned['price'] = df_cleaned['attributes'].apply(get_price)
df_cleaned['restaurant_type'] = df_cleaned['categories'].apply(
    lambda x: x.split(",")[0] if isinstance(x, str) else None
)

# Drop rows with missing values in key columns
df_cleaned = df_cleaned.dropna(subset=['price', 'stars'])

# Save the cleaned DataFrame to CSV
df_cleaned.to_csv("yelp_cleaned.csv", index=False)
print("Saved cleaned data to yelp_cleaned.csv")
