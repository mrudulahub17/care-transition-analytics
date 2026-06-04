import streamlit as st
import pandas as pd

st.set_page_config(page_title="Care Transition Analytics", layout="wide")

st.title("Care Transition Efficiency & Placement Outcome Analytics")

# Load dataset
df = pd.read_csv("HHS_Unaccompanied_Alien_Children_Program.csv")

# Fix Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Fix numeric columns
num_cols = [
    "Children apprehended and placed in CBP custody*",
    "Children in CBP custody",
    "Children transferred out of CBP custody",
    "Children in HHS Care",
    "Children discharged from HHS Care"
]

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing values (important)
df = df.fillna(0)

st.success("Dataset cleaned successfully!")

st.dataframe(df.head())
# ---------------- KPI CALCULATIONS ---------------- #

df["Transfer Efficiency Ratio"] = (
    df["Children transferred out of CBP custody"]
    / df["Children in CBP custody"]
)

df["Discharge Effectiveness"] = (
    df["Children discharged from HHS Care"]
    / df["Children in HHS Care"]
)

df["Pipeline Throughput"] = (
    df["Children discharged from HHS Care"]
    / df["Children apprehended and placed in CBP custody*"]
)

# ---------------- KPI CARDS ---------------- #

st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Transfer Efficiency", f"{df['Transfer Efficiency Ratio'].mean():.2f}")
col2.metric("Avg Discharge Effectiveness", f"{df['Discharge Effectiveness'].mean():.2f}")
col3.metric("Avg Throughput", f"{df['Pipeline Throughput'].mean():.2f}")

# ---------------- CHARTS ---------------- #

st.subheader("Trend Analysis")

st.line_chart(df.set_index("Date")[[
    "Children in CBP custody",
    "Children in HHS Care"
]])

st.subheader("Transfer Efficiency Over Time")
st.line_chart(df.set_index("Date")["Transfer Efficiency Ratio"])

st.subheader("Discharge Effectiveness Over Time")
st.line_chart(df.set_index("Date")["Discharge Effectiveness"])

# ---------------- BACKLOG ANALYSIS ---------------- #

df["Backlog"] = (
    df["Children in CBP custody"]
    - df["Children in HHS Care"]
)

st.subheader("Pipeline Backlog (Bottleneck Detection)")
st.line_chart(df.set_index("Date")["Backlog"])

st.success("Dashboard Fully Generated 🚀")