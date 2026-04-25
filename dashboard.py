import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Laptop Analytics Dashboard",
    layout="wide"
)

st.title("Laptop Distribution Intelligence Dashboard")
st.caption("Operational Analytics for Inventory, Repairs, and Vendor Performance")




# =========================
# DATABASE CONNECTION
# =========================

raw_password = "Realwealthyandtea"
encoded_password = quote_plus(raw_password)

DATABASE_URL = f"postgresql://postgres.jcydwwkohqpmfepgztzq:{encoded_password}@aws-0-eu-west-1.pooler.supabase.com:6543/postgres"

engine = create_engine(DATABASE_URL)



# =========================
# LOAD DATA
# =========================

laptops = pd.read_sql("SELECT * FROM laptops", engine)
distributions = pd.read_sql("SELECT * FROM distributions", engine)
repairs = pd.read_sql("SELECT * FROM repairs", engine)
vendors = pd.read_sql("SELECT * FROM vendors", engine)

# =========================
# KPI SECTION
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Laptops", len(laptops))

with col2:
    avg_cost = int(laptops["purchase_cost"].mean())
    st.metric("Avg Purchase Cost", f"₦{avg_cost:,}")

with col3:
    total_repairs = len(repairs)
    st.metric("Repair Cases", total_repairs)

with col4:
    total_repair_cost = int(repairs["repair_cost"].sum())
    st.metric("Total Repair Cost", f"₦{total_repair_cost:,}")

# =========================
# CHART 1 — DEPARTMENT USAGE
# =========================

st.subheader("Laptop Allocation by Department")

dept_chart = px.bar(
    distributions,
    x="department",
    title="Department Distribution of Assigned Laptops"
)

st.plotly_chart(dept_chart, use_container_width=True)

# =========================
# CHART 2 — REPAIR ISSUES
# =========================

st.subheader("Most Common Repair Issues")

issue_chart = px.pie(
    repairs,
    names="issue_type",
    title="Repair Issue Breakdown"
)

st.plotly_chart(issue_chart, use_container_width=True)

# =========================
# CHART 3 — VENDOR RISK
# =========================

st.subheader("Vendor Defect Rate")

vendor_chart = px.bar(
    vendors,
    x="vendor_name",
    y="defect_rate",
    title="Vendor Defect Rate Comparison"
)

st.plotly_chart(vendor_chart, use_container_width=True)

# =========================
# TABLE PREVIEW
# =========================

st.subheader("Inventory Preview")

st.dataframe(laptops.head(20))