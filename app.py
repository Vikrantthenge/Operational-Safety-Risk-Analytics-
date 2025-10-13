import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# --- Page Setup ---
st.set_page_config(page_title="🛡️ Operational Safety & Risk Analytics", layout="centered")
custom_blues = ["#003366", "#004080", "#0059b3", "#0073e6", "#3399ff"]

# --- Header Bar ---
st.markdown("""
<div style='background-color:#004080; padding:6px; text-align:center; border-radius:5px;'>
    <span style='color:white; font-size:16px;'> RISK SENTINEL </span>
</div>
""", unsafe_allow_html=True)

# --- Title Block ---
st.markdown("""
<div style='text-align: center; padding: 10px 0;'>
    <h1 style='color: #003366;'>🛡️ Operational Safety & Risk Analytics</h1>
    <h3 style='color: gray;'>Predict and visualize operational risks with recruiter-grade clarity</h3>
</div>
""", unsafe_allow_html=True)

# --- Load Data ---
df = pd.read_csv("data/safety_data.csv")

# --- Sidebar Filter ---
st.sidebar.header("🔎 Filter")
selected_site = st.sidebar.selectbox("Site", df["Site"].unique())
filtered_df = df[df["Site"] == selected_site]

# --- Risk Trends ---
st.subheader("📈 RISK TRENDS")
fig_trend = px.line(
    filtered_df,
    x="Date",
    y="RiskScore",
    color="Department",
    markers=True,
    title="Risk Score Over Time"
)
st.plotly_chart(fig_trend, use_container_width=True)

# --- Incident Distribution ---
st.subheader("📊 INCIDENT DISTRIBUTION")
incident_counts = filtered_df.groupby("Department")["IncidentFlag"].sum().reset_index()
fig_bar = px.bar(
    incident_counts,
    x="Department",
    y="IncidentFlag",
    color="Department",
    title="Incident Count by Department"
)
st.plotly_chart(fig_bar, use_container_width=True)

# --- Model Performance ---
st.subheader("🧠 MODEL PERFORMANCE")
X = filtered_df[["Temperature", "Humidity", "EquipmentAge"]]
y = filtered_df["IncidentFlag"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

report = classification_report(y_test, y_pred)
st.text(report)

# --- Download Button ---
st.download_button(
    label="📥 DOWNLOAD RISK REPORT",
    data=filtered_df.to_csv(index=False),
    file_name="risk_report.csv",
    mime="text/csv"
)
