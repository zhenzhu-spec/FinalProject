import os
import json
import pandas as pd
import zipfile
import ast

# Step 1: Unzip dataset if needed
zip_path = "yelp_academic_dataset_business.json.zip"
json_path = "yelp_academic_dataset_business.json"

if not os.path.exists(json_path) and os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()
    print(f"✅ Unzipped {zip_path}")

# Step 2: Load raw JSON lines into a list of dicts
data = []
with open(json_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"❌ JSON parsing error: {e}")

# Step 3: Create a DataFrame from the raw data
df = pd.DataFrame(data)

# Step 4: Filter to only rows with "restaurant" in categories (case-insensitive)
df = df[df['categories'].str.contains("restaurant", case=False, na=False)]

# Step 5: Safely extract price range from attributes
def extract_price(attributes):
    if isinstance(attributes, str):
        try:
            parsed = ast.literal_eval(attributes)
        except (ValueError, SyntaxError):
            return None
    elif isinstance(attributes, dict):
        parsed = attributes
    else:
        return None

    price = parsed.get("RestaurantsPriceRange2")
    return int(price) if str(price).isdigit() else None

df['price'] = df['attributes'].apply(extract_price)

# Step 6: Extract primary restaurant type (first tag in categories)
df['restaurant_type'] = df['categories'].apply(
    lambda x: x.split(",")[0].strip() if isinstance(x, str) else None
)

# Step 7: Select relevant columns
selected_cols = [
    "name", "stars", "attributes", "categories", "city", "state", "price", "restaurant_type"
]
df_cleaned = df[selected_cols]

# Step 8: Drop rows without star ratings
df_cleaned = df_cleaned.dropna(subset=["stars"])

# Step 9: Save the cleaned DataFrame to CSV
output_file = "yelp_cleaned.csv"
df_cleaned.to_csv(output_file, index=False)
print(f"✅ Saved cleaned data to {output_file}")
