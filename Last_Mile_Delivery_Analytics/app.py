import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Last Mile Delivery Analytics",
    page_icon="🚚",
    layout="wide"
)

# Title
st.title("🚚 Last Mile Delivery Analytics Dashboard")

# Project Overview
st.markdown("""
## 📌 Project Overview

This project analyzes **last-mile delivery operations** using **Python, SQL, Excel, and Power BI**.

### 🛠️ Tools Used
- 🐍 Python
- 🗄️ SQL
- 📊 Power BI
- 📑 Excel

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

# Dashboard
st.header("📊 Power BI Dashboard")

try:
    st.image(
        "Screenshots/Power bi/dashboard.png",
        use_container_width=True
    )
except:
    st.error("Dashboard image not found. Please check the image path.")

st.divider()

# About Project
st.header("📖 About Project")

st.write("""
This project focuses on analyzing last-mile delivery performance across multiple cities.

The dashboard helps identify:

- 📦 Total Orders
- ⏱️ Average Delivery Time
- 🚚 Vendor Performance
- 📍 City-wise Orders
- 💰 Revenue by Product Category
- ⚠️ SLA Breaches
- 📈 Monthly Order Trends

The project was built using Python, SQL, Excel and Power BI to demonstrate end-to-end data analytics skills.
""")

st.divider()

st.success("✅ Project Developed by Rachit Bajpai")
