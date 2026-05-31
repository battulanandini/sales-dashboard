import pandas as pd

# Load the dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')

# 1. See first 5 rows
print("=== First 5 Rows ===")
print(df.head())

# 2. See column names and data types
print("\n=== Column Info ===")
print(df.info())

# 3. See basic statistics
print("\n=== Basic Statistics ===")
print(df.describe())

# 4. See all column names
print("\n=== Column Names ===")
print(df.columns.tolist())