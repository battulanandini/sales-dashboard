import pandas as pd

# Load data
df = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')

# Fix date format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month-Year'] = df['Order Date'].dt.to_period('M')
df['Year'] = df['Order Date'].dt.year

# ── 1. Total Sales & Profit ──────────────────────────────
print("=== Overall Summary ===")
print(f"Total Sales  : ${df['Sales'].sum():,.2f}")
print(f"Total Profit : ${df['Profit'].sum():,.2f}")
print(f"Total Orders : {df['Order ID'].nunique()}")

# ── 2. Sales by Region ───────────────────────────────────
print("\n=== Sales by Region ===")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

# ── 3. Sales by Category ─────────────────────────────────
print("\n=== Sales by Category ===")
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

# ── 4. Top 5 Best-Selling Sub-Categories ─────────────────
print("\n=== Top 5 Sub-Categories by Sales ===")
top_sub = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(5)
print(top_sub)

# ── 5. Monthly Sales Trend ───────────────────────────────
print("\n=== Monthly Sales (2017) ===")
df_2017 = df[df['Year'] == 2017]
monthly = df_2017.groupby('Month-Year')['Sales'].sum()
print(monthly)

# ── 6. Profit by Category ────────────────────────────────
print("\n=== Profit by Category ===")
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print(category_profit)

# ── 7. Sales by Customer Segment ─────────────────────────
print("\n=== Sales by Segment ===")
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
print(segment_sales)