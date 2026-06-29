import streamlit as st

st.set_page_config(
    page_title="Last Mile Delivery Analytics",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Last Mile Delivery Analytics Dashboard")

st.markdown("""
### Project Overview

This project analyzes last-mile delivery operations using Python, SQL, Excel, and Power BI.

**Tools Used:**
- 🐍 Python
- 🗄️ SQL
- 📊 Power BI
- 📑 Excel

The dashboard helps analyze:
- Total Orders
- Delayed Orders
- SLA Breaches
- Revenue
- Vendor Performance
- City-wise Orders
- Monthly Order Trends
""")
st.subheader("📊 Power BI Dashboard")

st.image(
    "Last_Mile_Delivery_Analytics/Screenshots/Power bi/dashboard.png",
    use_container_width=True
)
