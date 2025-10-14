# ✈️ Operational Safety & Risk Analytics

[![View Project](https://img.shields.io/badge/View%20Project-Operational%20Safety%20%26%20Risk%20Analytics-blue)](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-)

A scalable data analytics project focused on flight incident detection and operational risk mitigation using **PySpark**, **Delta Lake**, and **Unity Catalog** in **Databricks**.

---

## 📌 Project Highlights

- 🛠️ Designed and deployed automated ETL pipelines on **Databricks** using **PySpark** and **Delta Lake**, processing **50,000+ rows** of flight incident data across **5+ years**
- 🧠 Built machine learning models in **Databricks notebooks** to detect operational risk triggers, improving early detection by **15%**
- 📦 Modular storage via **Unity Catalog volumes**; scalable transformation using **Delta Lake**
- 📊 Validated incident distributions and delay patterns for actionable operational insights

---

## 🧱 Platform Stack

| Component        | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| 🧠 **Databricks**       | Unified workspace for ETL, ML modeling, and Delta Lake transformations       |
| 📦 **Unity Catalog**    | Modular volume access, table registration, and data governance               |
| 🔄 **Delta Lake**       | Scalable data storage and transformation layer for managed tables            |
| ⚙️ **PySpark & pandas** | Data wrangling, feature engineering, and transformation logic                |
| 📊 **scikit-learn**     | ML model development, evaluation, and risk flag prediction                   |

![Platform](https://img.shields.io/badge/Built%20on-Databricks-navy)
![Storage](https://img.shields.io/badge/Data%20Layer-Delta%20Lake-gray)
![Governance](https://img.shields.io/badge/Volume%20Access-Unity%20Catalog-blue)

---

# 🧩 ETL Pipeline – Databricks

**[CSV: `sample_ops_data.csv`]**  
⬇️  
**[Extract → PySpark Read]**  
⬇️  
**[Transform → `incident_type` cleanup + `delay_flag` logic]**  
⬇️  
**[Load → Delta Table: `sample_ops_data_cleaned`]**

### ✈️ Sample Ops ETL Pipeline Summary

- 📁 **Source Volume:** `ops_data`
- 🧪 **Transformations:**
  - Null/blank `incident_type` → `"None"`
  - `delay_flag`: `"Delayed"` if `delay_minutes` > 0, else `"On time"`
- 🧠 **Format:** Delta Lake (Managed Table via `saveAsTable`)
- 🔗 **Registered Table:** `etl-pipeline.default.sample_ops_data_cleaned`
- ✅ **CSV Verified:** `sample_ops_data.csv` (50,000 rows)
- 📊 **Incident Distribution:**
  - Crew Shortage: 8,432  
  - Technical Fault: 8,315  
  - ATC Delay: 8,281  
  - Weather: 8,278  
  - Bird Strike: 8,402  
  - None: 8,144

---

## 🧠 ML-Powered Risk Detection – Databricks

**[Notebook: `Operational_Safety_ML_Module.ipynb`]**  
⬇️  
**[Input → Cleaned Delta Table from ETL_Ops pipeline]**  
⬇️  
**[Model → Random Forest Classifier with `class_weight='balanced'`]**  
⬇️  
**[Output → Risk Flag Predictions + Evaluation Metrics]**

### 🚨 ML Module Summary

- 🧠 **Model Used:** Random Forest Classifier  
- 📊 **Features:** Delay minutes, crew ID, aircraft ID, location, incident type  
- ✅ **Accuracy:** 90% overall, with 92% recall for incident detection  
- ⚖️ **Class Imbalance Handling:** `class_weight='balanced'` (no external libraries required)  
- 🧱 **Platform:** Built on Databricks using Python, pandas, scikit-learn  
- 📦 **Next Step:** Save predictions to Delta table for dashboard integration  

![ML Module](https://img.shields.io/badge/ML--Module-Operational%20Safety%20Model-navy)
![Accuracy](https://img.shields.io/badge/Accuracy-92%25-gray)

### 📈 ML Evaluation Snapshot

![Classification Report – Operational Safety ML](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/classification_report.png?raw=true)

---
## 🌐 Streamlit Dashboard – Hugging Face Spaces

[![Launch App](https://img.shields.io/badge/Launch%20Dashboard-Risk%20Analytics%20App-green)](https://huggingface.co/spaces/vthenge/risk-analytics)

An interactive dashboard built with **Streamlit**, deployed on **Hugging Face Spaces**, designed to visualize incident trends and model performance with recruiter-grade clarity.

### 🛡️ Dashboard Highlights

- 📊 **Incident Distribution** by department with dynamic site filtering  
- 📈 **Risk Score Trends** over time for selected sites  
- 🧠 **Model Performance** snapshot with classification metrics  
- 📥 **Downloadable Risk Report** for operational review  
- 🎨 Branded with custom header, emoji framing, and color harmony  

### ⚠️ Cold Start Notice

> ⚠️ **Heads up!**  
> If the app shows a “Zzzz” screen, it's just waking up from sleep.  
> Click “Yes” to load — it takes only a few seconds!

---

### 📸 Dashboard Preview

![Dashboard Screenshot](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/dashboard_preview.png?raw=true)

---

## 📎 Additional Assets

| Asset Type | Badge |
|------------|-------|
| 🚀 Hugging Face App | [![App](https://img.shields.io/badge/View%20App-Risk%20Analytics-green)](https://huggingface.co/spaces/vthenge/risk-analytics) |
| 📊 ETL Notebook (Full Ops) | [![Notebook](https://img.shields.io/badge/View%20Notebook-ETL_Ops.ipynb-navy)](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/ETL_Ops.ipynb) |
| 🧠 ML Notebook (Ops Safety) | [![Notebook](https://img.shields.io/badge/View%20Notebook-Operational_Safety_ML_Module.ipynb-red)](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/Operational_Safety_ML_Module.ipynb) |
| 🖼️ Incident Distribution Screenshot | [![Screenshot](https://img.shields.io/badge/View%20Screenshot-incident_distribution.png-green)](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/incident_distribution.png) |

---

> **“Where safety meets strategy. Where data drives action.”**

---

Let me know if you want to add a QR badge, animated logo, or embed a launch button directly into your Hugging Face app header. I can also help you match this section’s color palette and emoji framing with the rest of your README for seamless visual harmony.

## 🚀 How to Run

1. Upload `sample_ops_data.csv` to Unity Catalog volume `ops_data`  
2. Run `ETL_Ops.ipynb` in Databricks to clean and transform the data  
3. Output saved to `ops_data_cleaned` volume and registered as Delta table  
4. Run `Operational_Safety_ML_Module.ipynb` to train and evaluate the ML model  
5. Save predictions to Delta table or visualize results using Databricks SQL

---

## 📎 Additional Assets

| Asset Type | Badge |
|------------|-------|
| 📊 ETL Notebook (Full Ops) | [![Notebook](https://img.shields.io/badge/View%20Notebook-ETL_Ops.ipynb-navy)](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/ETL_Ops.ipynb) |
| 🧠 ML Notebook (Ops Safety) | [![Notebook](https://img.shields.io/badge/View%20Notebook-Operational_Safety_ML_Module.ipynb-red)](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/Operational_Safety_ML_Module.ipynb) |
| 🖼️ Incident Distribution Screenshot | [![Screenshot](https://img.shields.io/badge/View%20Screenshot-incident_distribution.png-green)](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-/blob/main/incident_distribution.png) |

---

## 🙌 Acknowledgments

Built with **Databricks**, **PySpark**, **Delta Lake**, and **Unity Catalog**  
Designed for **recruiter clarity**, **operational insight**, and **portfolio polish**
