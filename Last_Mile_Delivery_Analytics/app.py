import streamlit as st
from pathlib import Path

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Last Mile Delivery Analytics",
    page_icon="🚚",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title("🚚 Last Mile Delivery Analytics Dashboard")

st.markdown("""
## 📌 Project Overview

This project analyzes **Last Mile Delivery Operations** using **Python, SQL, Excel, and Power BI**.

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

# -------------------------------
# Dashboard Image
# -------------------------------

st.header("📊 Power BI Dashboard")

base_path = Path(__file__).parent

image_path = base_path / "Screenshots" / "Power_Bi" / "dashboard.png"

if image_path.exists():
    st.image(str(image_path), use_container_width=True)
else:
    st.error("❌ Dashboard image not found.")
    st.write("Expected path:")
    st.code(str(image_path))

st.divider()

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
