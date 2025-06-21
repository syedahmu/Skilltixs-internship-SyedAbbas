import pandas as pd

# Load the dataset
df = pd.read_csv("customer_personality.csv")

# Step 1: Handle missing values
missing_values = df.isnull().sum()
print("Missing values before handling:\n", missing_values)

# Example handling: drop rows with missing 'Income'
df = df.dropna(subset=['Income'])

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Standardize text values (example: Education, Marital_Status)
df['Education'] = df['Education'].str.strip().str.lower()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.lower()

# Step 4: Convert date formats
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True)

# Step 5: Rename column headers (lowercase, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 6: Fix data types
df['year_birth'] = df['year_birth'].astype(int)
df['income'] = df['income'].astype(float)

# Create a new column: Age (from year of birth)
df['age'] = 2025 - df['year_birth']

# Show the cleaned data preview
print("\nCleaned Data Preview:\n", df.head())

# Save the cleaned data (optional)
df.to_csv("cleaned_dataset.csv", index=False)