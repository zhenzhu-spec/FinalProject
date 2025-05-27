import os
import json
import pandas as pd
import zipfile

# Step 1: Unzip dataset if needed
zip_path = "yelp_academic_dataset_business.json.zip"
json_path = "yelp_academic_dataset_business.json"
if not os.path.exists(json_path) and os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()
    print(f"Unzipped {zip_path}")

# Step 2: Load raw JSON lines
data = []
with open(json_path, 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))

# Step 3: Create DataFrame
df = pd.DataFrame(data)

# Step 4: Keep rows where categories include "Restaurant" (case-insensitive)
df = df[df['categories'].str.contains("restaurant", case=False, na=False)]

# Step 5: Extract price from attributes
def get_price(attr):
    try:
        parsed = eval(attr) if isinstance(attr, str) else attr
        price = parsed.get("RestaurantsPriceRange2")
        return int(price) if price and str(price).isdigit() else None
    except:
        return None

df['price'] = df['attributes'].apply(get_price)

# Step 6: Extract first tag from categories
df['restaurant_type'] = df['categories'].apply(lambda x: x.split(",")[0].strip() if isinstance(x, str) else None)

# Step 7: Select relevant columns
df_cleaned = df[["name", "stars", "attributes", "categories", "city", "state", "price", "restaurant_type"]]

# Step 8: Drop rows without stars (keep price even if missing)
df_cleaned = df_cleaned.dropna(subset=["stars"])

# Step 9: Save cleaned data
df_cleaned.to_csv("yelp_cleaned.csv", index=False)
print("✅ Saved cleaned data to yelp_cleaned.csv")
