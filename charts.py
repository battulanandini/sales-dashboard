import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month-Year'] = df['Order Date'].dt.to_period('M')
df['Year'] = df['Order Date'].dt.year

# ── 1. Sales by Region (Bar Chart) ───────────────────────
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(region_sales.index, region_sales.values, color=['#4C72B0','#DD8452','#55A868','#C44E52'])
plt.title('Sales by Region', fontsize=16)
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('chart1_region_sales.png')
plt.show()
print("✅ Chart 1 saved!")

# ── 2. Sales by Category (Horizontal Bar) ────────────────
category_sales = df.groupby('Category')['Sales'].sum().sort_values()

plt.figure(figsize=(8, 4))
plt.barh(category_sales.index, category_sales.values, color=['#55A868','#4C72B0','#DD8452'])
plt.title('Sales by Category', fontsize=16)
plt.xlabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('chart2_category_sales.png')
plt.show()
print("✅ Chart 2 saved!")

# ── 3. Monthly Sales Trend (Line Chart) ──────────────────
df_2017 = df[df['Year'] == 2017]
monthly = df_2017.groupby('Month-Year')['Sales'].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly.index.astype(str), monthly.values, marker='o', color='#4C72B0', linewidth=2)
plt.title('Monthly Sales Trend (2017)', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart3_monthly_trend.png')
plt.show()
print("✅ Chart 3 saved!")

# ── 4. Sales by Segment (Pie Chart) ──────────────────────
segment_sales = df.groupby('Segment')['Sales'].sum()

plt.figure(figsize=(7, 7))
plt.pie(segment_sales.values, labels=segment_sales.index,
        autopct='%1.1f%%', colors=['#4C72B0','#DD8452','#55A868'],
        startangle=140)
plt.title('Sales by Customer Segment', fontsize=16)
plt.tight_layout()
plt.savefig('chart4_segment_pie.png')
plt.show()
print("✅ Chart 4 saved!")

# ── 5. Profit by Category (Bar Chart) ────────────────────
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(category_profit.index, category_profit.values, color=['#4C72B0','#55A868','#DD8452'])
plt.title('Profit by Category', fontsize=16)
plt.xlabel('Category')
plt.ylabel('Total Profit ($)')
plt.tight_layout()
plt.savefig('chart5_profit_category.png')
plt.show()
print("✅ Chart 5 saved!")

print("\n🎉 All 5 charts created and saved!")