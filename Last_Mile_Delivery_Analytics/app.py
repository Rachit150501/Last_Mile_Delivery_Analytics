import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

# -------------------------------
# Base Path
# -------------------------------
base_path = Path(__file__).parent

# -------------------------------
# Dataset Load
# -------------------------------
data_path = base_path / "Dataset" / "Last_Mile_Delivery_Dataset.csv"
df = pd.read_csv(data_path)


st.sidebar.header(" Filters")

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["City"].unique().tolist())
)

selected_vendor = st.sidebar.selectbox(
    "Select Vendor",
    ["All"] + sorted(df["Vendor"].unique().tolist())
)

# Apply Filters
filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[filtered_df["City"] == selected_city]

if selected_vendor != "All":
    filtered_df = filtered_df[filtered_df["Vendor"] == selected_vendor]



# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Last Mile Delivery Analytics",
    page_icon="",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title(" Last Mile Delivery Analytics Dashboard")

st.markdown("""
##  Project Overview

This project analyzes **Last Mile Delivery Operations** using **Python, SQL, Excel, and Power BI**.

###  Tools Used
-  Python
-  SQL
-  Power BI
-  Excel

### 📈 Key KPIs
- Total Orders
- Delayed Orders
- SLA Breaches
- Revenue
- Vendor Performance
- City-wise Orders
- Monthly Order Trends
""")

st.divider()

# -------------------------------
# Dashboard Image
# -------------------------------

st.header("📊 Power BI Dashboard")


image_path = base_path / "Screenshots" / "Power_Bi" / "dashboard.png"

if image_path.exists():
    st.image(str(image_path), use_container_width=True)
else:
    st.error("❌ Dashboard image not found.")
    st.write("Expected path:")
    st.code(str(image_path))

st.divider()


# -------------------------------
# KPI Dashboard
# -------------------------------

st.header("📊 Live KPI Dashboard")

total_orders = len(filtered_df)
total_revenue = df["Order_Value_INR"].sum()
delayed_orders = (df["Is_Delayed"] == "Yes").sum()
sla_breaches = (df["SLA_Breached"] == "Yes").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Total Orders", f"{total_orders:,}")
col2.metric("💰 Total Revenue", f"₹{total_revenue:,.2f}")
col3.metric("🚚 Delayed Orders", f"{delayed_orders:,}")
col4.metric("⚠️ SLA Breaches", f"{sla_breaches:,}")




# -------------------------------
# Python Analysis
# -------------------------------

st.divider()

st.header(" Python Analysis")

python_path = base_path / "Screenshots" / "Python"

col1, col2 = st.columns(2)

with col1:
    st.image(str(python_path / "01_dataset_preview.png"), caption="Dataset Preview")
    st.image(str(python_path / "03_dataset_shape.png"), caption="Dataset Shape")
    st.image(str(python_path / "05_city_orders_table.png"), caption="City Orders")

with col2:
    st.image(str(python_path / "02_missing_values.png"), caption="Missing Values")
    st.image(str(python_path / "04_columns_list.png"), caption="Columns")
    st.image(str(python_path / "06_vendor_orders_table.png"), caption="Vendor Orders")

st.image(str(python_path / "07_delay_reasons_table.png"), caption="Delay Reasons")

# -------------------------------
# SQL
# -------------------------------

st.divider()

st.header("🗄️ SQL Analysis")

sql_path = base_path / "Screenshots" / "SQL"

col1, col2 = st.columns(2)

with col1:
    st.image(str(sql_path / "01_kpi_summary.png"), caption="KPI Summary")
    st.image(str(sql_path / "03_city_avg_delay.png"), caption="City Average Delay")
    st.image(str(sql_path / "05_delay_root_causes.png"), caption="Delay Root Causes")

with col2:
    st.image(str(sql_path / "02_city_wise_orders.png"), caption="City Wise Orders")
    st.image(str(sql_path / "04_vendor_performance.png"), caption="Vendor Performance")
    st.image(str(sql_path / "06_revenue_by_category.png"), caption="Revenue by Category")


st.divider()

st.header(" Revenue by Product Category")

category_revenue = (
    filtered_df.groupby("Product_Category")["Order_Value_INR"]
    .sum()
    .reset_index()
)

fig = px.pie(
    category_revenue,
    values="Order_Value_INR",
    names="Product_Category",
    hole=0.45,
    title="Revenue by Product Category"
)

st.plotly_chart(fig, use_container_width=True)




st.divider()

st.header("🏙️ Orders by City")

city_orders = (
    filtered_df.groupby("City")
    .size()
    .reset_index(name="Orders")
)

fig = px.bar(
    city_orders,
    x="City",
    y="Orders",
    color="Orders",
    text="Orders",
    title="Orders by City"
)

st.plotly_chart(fig, use_container_width=True)


st.divider()

st.header("🚚 Vendor Performance")

vendor_orders = (
    filtered_df.groupby("Vendor")
    .size()
    .reset_index(name="Orders")
)

fig = px.bar(
    vendor_orders,
    x="Vendor",
    y="Orders",
    color="Orders",
    text="Orders",
    title="Vendor Performance"
)

st.plotly_chart(fig, use_container_width=True)



st.divider()

st.header("📈 Monthly Order Trend")

monthly_orders = (
    filtered_df.groupby("Month")
    .size()
    .reset_index(name="Orders")
)

fig = px.line(
    monthly_orders,
    x="Month",
    y="Orders",
    markers=True,
    title="Monthly Orders"
)

st.plotly_chart(fig, use_container_width=True)


st.divider()

st.header("⚠ Delay Reasons")

delay = (
    filtered_df.groupby("Delay_Reason")
    .size()
    .reset_index(name="Orders")
)

fig = px.bar(
    delay,
    x="Delay_Reason",
    y="Orders",
    color="Orders"
)

st.plotly_chart(fig, use_container_width=True)



st.divider()

st.header(" Download Dataset")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="Last_Mile_Delivery.csv",
    mime="text/csv"
)

# -------------------------------
# Dataset Information
# -------------------------------

st.divider()

st.header(" Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("📦 Total Orders", "5,200")
col2.metric("🏙️ Cities", "15")
col3.metric("🚚 Vendors", "8")

col1.metric("⚠️ Delayed Orders", "2,236")
col2.metric("📉 SLA Breaches", "1,459")
col3.metric("💰 Revenue", "₹38.85M")



# -------------------------------
# Project Highlights
# -------------------------------

st.divider()

st.header("💡 Key Business Insights")

st.success("""
✔ 5,200 Orders Analyzed

✔ 15 Cities Covered

✔ 43% Orders Delayed

✔ 28% SLA Breaches

✔ Revenue ₹38.85 Million

✔ Delay Reasons Analysis

✔ Vendor Performance Comparison

✔ City-wise Delivery Analysis

✔ Product Category Revenue Analysis
""")



# -------------------------------
# Tech Stack
# -------------------------------

st.divider()

st.header("🛠 Tech Stack")

st.markdown("""
-  Python (Pandas)
-  SQL
-  Power BI
-  Excel
-  Streamlit
-  GitHub
""")

# -------------------------------
# GitHub Link
# -------------------------------

st.divider()

st.header("🔗 GitHub Repository")

st.markdown("[👉 View Complete Project on GitHub](https://github.com/Rachit150501/Last_Mile_Delivery_Analytics)")


# -------------------------------
# Footer
# -------------------------------

st.divider()

st.markdown("---")

st.markdown(
"""
###  Developed by Rachit Bajpai

📊 Data Analyst Portfolio Project

 Thank you for visiting!
"""
)

# -------------------------------
# About Project
# -------------------------------

st.header("📖 About Project")

st.markdown("""
This project focuses on analyzing last-mile delivery performance across multiple cities.

### Dashboard Insights

- 📦 Total Orders
- ⏱️ Average Delivery Time
- 🚚 Vendor Performance
- 📍 City-wise Orders
- 💰 Revenue by Product Category
- ⚠️ SLA Breaches
- 📈 Monthly Order Trends

### Technologies Used

- Python
- SQL
- Excel
- Power BI
- Streamlit

This project demonstrates an end-to-end Data Analytics workflow from data cleaning to dashboard development.
""")

st.divider()

st.success("✅ Developed by Rachit Bajpai")
