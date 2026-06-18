import pandas as pd
import plotly.express as px
import streamlit as st

# ── Page Config ───────────────────────────────────────────
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")

# ── Load Data ─────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month-Year'] = df['Order Date'].dt.to_period('M').astype(str)
    df['Year'] = df['Order Date'].dt.year
    return df

df = load_data()

# ── Sidebar Filters ───────────────────────────────────────
st.sidebar.title("🔍 Filters")
st.sidebar.caption("Select at least one option in each filter to see results.")

year = st.sidebar.multiselect(
    "Select Year:",
    options=sorted(df['Year'].unique())
    # no default → starts empty
)

region = st.sidebar.multiselect(
    "Select Region:",
    options=df['Region'].unique()
    # no default → starts empty
)

category = st.sidebar.multiselect(
    "Select Category:",
    options=df['Category'].unique()
    # no default → starts empty
)

# ── Title ─────────────────────────────────────────────────
st.title("📊 Sales Dashboard — Superstore")
st.markdown("---")

# ── Stop here and show a message if filters are empty ─────
if not year or not region or not category:
    st.info("👈 Please select at least one **Year**, **Region**, and **Category** from the sidebar to view the dashboard.")
    st.stop()

# ── Filter Data ───────────────────────────────────────────
df_filtered = df[
    (df['Year'].isin(year)) &
    (df['Region'].isin(region)) &
    (df['Category'].isin(category))
]

# ── KPI Cards ─────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Sales",    f"${df_filtered['Sales'].sum():,.0f}")
col2.metric("📈 Total Profit",   f"${df_filtered['Profit'].sum():,.0f}")
col3.metric("📦 Total Orders",   f"{df_filtered['Order ID'].nunique():,}")
col4.metric("👥 Customers",      f"{df_filtered['Customer ID'].nunique():,}")

st.markdown("---")

# ── Row 1: Region & Category Charts ───────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("🗺️ Sales by Region")
    region_sales = df_filtered.groupby('Region')['Sales'].sum().reset_index()
    fig = px.bar(region_sales, x='Region', y='Sales',
                 color='Region', text_auto='.2s')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📦 Sales by Category")
    cat_sales = df_filtered.groupby('Category')['Sales'].sum().reset_index()
    fig = px.pie(cat_sales, names='Category', values='Sales', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

# ── Row 2: Monthly Trend ───────────────────────────────────
st.subheader("📅 Monthly Sales Trend")
monthly = df_filtered.groupby('Month-Year')['Sales'].sum().reset_index()
monthly = monthly.sort_values('Month-Year')
fig = px.line(monthly, x='Month-Year', y='Sales', markers=True)
st.plotly_chart(fig, use_container_width=True)

# ── Row 3: Sub-Category & Segment ─────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 Sub-Categories")
    sub_sales = df_filtered.groupby('Sub-Category')['Sales'].sum()\
                .sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(sub_sales, x='Sales', y='Sub-Category',
                 orientation='h', color='Sales')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("👥 Sales by Segment")
    seg_sales = df_filtered.groupby('Segment')['Sales'].sum().reset_index()
    fig = px.pie(seg_sales, names='Segment', values='Sales', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

# ── Row 4: Profit by Category ──────────────────────────────
st.subheader("💰 Profit by Category")
profit_cat = df_filtered.groupby('Category')['Profit'].sum().reset_index()
fig = px.bar(profit_cat, x='Category', y='Profit',
             color='Category', text_auto='.2s')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Python, Pandas, Plotly & Streamlit")