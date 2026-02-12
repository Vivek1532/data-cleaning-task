import pandas as pd

# Load dataset
df = pd.read_csv("mall_customer_segmentation_raw.csv")

print("Original Data:")
print(df.head())

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Gender'] = df['Gender'].fillna("unknown")

# Remove duplicates
df = df.drop_duplicates()

# Clean text
df['Gender'] = df['Gender'].str.lower().str.strip()

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Fix data types
df['age'] = df['age'].astype(int)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaning completed. Cleaned file saved!")
