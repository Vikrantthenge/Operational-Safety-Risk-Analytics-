# ✈️ Operational Safety & Risk Analytics  
**Production-Style Analytics System for Leadership Risk Decisions**

A real-world operational analytics system built to detect risk patterns, automate ETL pipelines, and deliver **decision-ready insights** for leadership teams.

This project demonstrates how operational data moves from  
**raw ingestion → governed transformation → risk indicators → executive dashboards**,  
using enterprise-grade tools and design patterns.

**What this project proves**
- Ownership of **end-to-end analytics delivery**, not isolated modeling
- Design of **KPI frameworks and risk indicators** used in leadership reviews
- Automation that replaces **manual MIS and reactive reporting**
- Comfort with **enterprise platforms and data governance**

🚀 **Live Interactive Dashboard (Hugging Face):**  
[![Live App – Hugging Face](https://img.shields.io/badge/Live_App-HuggingFace-yellow?logo=huggingface&logoColor=black)](https://huggingface.co/spaces/vthenge/risk-analytics)

> ⚠️ If the app shows a sleep screen, click **“Yes, get this app back up!”** — it takes only a few seconds.

---

## 🔧 Technology Stack

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-003B57?logo=postgresql&logoColor=white&style=for-the-badge)](https://www.postgresql.org/)
[![PySpark](https://img.shields.io/badge/PySpark-FDEE21?logo=apache-spark&logoColor=black&style=for-the-badge)](https://spark.apache.org/)
[![Databricks](https://img.shields.io/badge/Databricks-EA4E3D?logo=databricks&logoColor=white&style=for-the-badge)](https://www.databricks.com/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-00B4F0?logo=databricks&logoColor=white&style=for-the-badge)](https://delta.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge)](https://streamlit.io/)

---

## 📌 Project Context

Operational safety data is often:
- fragmented across systems  
- reviewed reactively  
- reported manually with limited foresight  

This project restructures that reality by creating a **single analytics flow** that:
- standardizes operational data  
- surfaces risk early  
- supports structured leadership reviews  

The outcome is **faster decisions, better prioritization, and reduced operational risk**.

---

## 🧩 End-to-End Analytics Flow

**CSV Source Data (5+ years)**  
⬇️  
**PySpark ETL on Databricks**  
⬇️  
**Delta Lake (governed, query-ready tables)**  
⬇️  
**Risk Indicators & ML-based risk flags**  
⬇️  
**Interactive Streamlit Dashboard for leadership review**

---

## 🧱 Data Platform Design

| Layer | Purpose |
|------|--------|
| **Databricks** | Unified workspace for ETL, analytics, and modeling |
| **Unity Catalog** | Data governance, table access, and volume management |
| **Delta Lake** | Reliable, scalable storage with ACID guarantees |
| **PySpark** | Transformation logic and feature engineering |
| **scikit-learn** | Risk flag modeling and evaluation |
| **Streamlit** | Decision-ready dashboard delivery |

---

## 🔄 ETL Pipeline – Operational Data

**Source**
- `sample_ops_data.csv` (50,000+ rows, multi-year operational records)

**Key Transformations**
- Standardized incident types
- Derived delay and risk flags
- Cleaned nulls and inconsistent values
- Converted to governed Delta tables

**Output**
- Managed Delta table registered for analytics and dashboards

**Incident Distribution Snapshot**
- Crew Shortage: ~8.4k  
- Technical Fault: ~8.3k  
- ATC Delay: ~8.2k  
- Weather: ~8.2k  
- Bird Strike: ~8.4k  
- None: ~8.1k  

---

## 🧠 Risk Detection Module (Analytics-Driven)

This project uses modeling **as an enabler**, not the centerpiece.

**Purpose**
- Identify operational risk patterns earlier
- Support prioritization and review, not academic accuracy contests

**Summary**
- Model: Random Forest (balanced classes)
- Inputs: delay minutes, incident type, location, aircraft, crew
- Output: risk flags for operational review
- Recall (risk detection): ~92%

📊 **Classification Report**  
[View snapshot](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/classification_report.png?raw=true)

---

## 📊 Decision Dashboard (Streamlit)

🚀 **Live Dashboard:**  
[![Launch Dashboard](https://img.shields.io/badge/Launch_Dashboard-Risk_Analytics-green)](https://huggingface.co/spaces/vthenge/risk-analytics)

**What leadership sees**
- Incident distribution by site and category  
- Risk score trends over time  
- Performance gaps and hotspots  
- Downloadable reports for review meetings  

This dashboard is built for **weekly and monthly performance discussions**, not exploratory tinkering.

---

## 📁 Key Assets

| Asset | Link |
|-----|-----|
| 🚀 Live Dashboard | https://huggingface.co/spaces/vthenge/risk-analytics |
| 📂 Full Repository | https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics- |
| ⚙️ ETL Notebook | https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/ETL_Ops.ipynb |
| 🧠 ML Notebook | https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/Operational_Safety_ML_Module.ipynb |

---

## 📊 Business Impact Demonstrated

- Enabled **earlier risk visibility** through standardized indicators  
- Replaced manual reporting with **automated analytics pipelines**  
- Improved consistency and trust in operational data  
- Delivered **decision-ready views** for leadership reviews  

---

## 🎯 Who This Project Is For

This project is intentionally built for:
- **Senior Analytics / Analytics Manager roles**
- **Decision Analytics & Planning**
- **Operations, Supply Chain, Safety, or Delivery Analytics**

It is **not** optimized for:
- Kaggle-style experimentation  
- Pure research or algorithm benchmarking  

---

## 📄 Resume

📥 **Download Resume (PDF)**  
https://github.com/Vikrantthenge/vikrant-portfolio/blob/main/Vikrant_Thenge_Analytics_Manager.pdf

---

> *“Where operational data stops being reactive and starts driving decisions.”*
