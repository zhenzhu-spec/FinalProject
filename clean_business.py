import os
import json
import pandas as pd
import zipfile

# Unzip dataset if needed
zip_path = "yelp_academic_dataset_business.json.zip"
json_path = "yelp_academic_dataset_business.json"
if not os.path.exists(json_path) and os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()
    print(f"Unzipped {zip_path}")

# Load data
data = []
with open(json_path, 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))

# Convert to DataFrame
df = pd.DataFrame(data)

# Filter only restaurants
df = df[df['categories'].str.contains("Restaurant", na=False)]

# Extract price range from attributes
def get_price(attr):
    try:
        return int(eval(attr).get("RestaurantsPriceRange2"))
    except:
        return None

df['price'] = df['attributes'].apply(get_price)
df['restaurant_type'] = df['categories'].apply(lambda x: x.split(",")[0] if isinstance(x, str) else None)

# Only drop rows without stars (price 可以为空)
df_cleaned = df[["name", "stars", "attributes", "categories", "city", "state", "price", "restaurant_type"]]
df_cleaned = df_cleaned.dropna(subset=['stars'])

# Save cleaned data
df_cleaned.to_csv("yelp_cleaned.csv", index=False)
print("Saved cleaned data to yelp_cleaned.csv")
