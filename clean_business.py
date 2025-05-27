import pandas as pd
import json
import zipfile
import os

# Unzip the dataset if it's a zip file
zip_filename = "yelp_academic_dataset_business.json.zip"
json_filename = "yelp_academic_dataset_business.json"

if not os.path.exists(json_filename):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall()
    print(f"Unzipped {zip_filename}")

# Load the JSON data
data = []
with open(json_filename, 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))

# Convert to DataFrame and filter restaurants
df = pd.DataFrame(data)
df = df[df['categories'].str.contains("Restaurant", na=False)]

# Helper function to extract price from attributes
def get_price(attr):
    try:
        return int(eval(attr).get("RestaurantsPriceRange2"))
    except:
        return None

# Extract fields
df_cleaned = df[["name", "stars", "attributes", "categories", "city", "state"]].copy()
df_cleaned["price"] = df_cleaned["attributes"].apply(get_price)
df_cleaned["restaurant_type"] = df_cleaned["categories"].apply(
    lambda x: x.split(",")[0] if isinstance(x, str) else None
)

# Optionally keep all rows even with missing price, but keep only rows with stars
df_cleaned = df_cleaned.dropna(subset=["stars"])

# Save the cleaned data
df_cleaned.to_csv("yelp_cleaned.csv", index=False)
print("Saved cleaned data to yelp_cleaned.csv")
