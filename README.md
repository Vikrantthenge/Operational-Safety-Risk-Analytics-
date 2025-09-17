# ✈️ Operational Safety & Risk Analytics

[![View Project](https://img.shields.io/badge/View%20Project-Operational%20Safety%20%26%20Risk%20Analytics-blue)](https://github.com/Vikrantthenge/Operational-Safety-Risk-Analytics-)

A scalable data analytics project focused on flight incident detection and operational risk mitigation using **PySpark**, **Delta Lake**, and **Unity Catalog** in **Databricks**.

---

## 📌 Project Highlights

- 🛠️ Automated ETL pipelines processing **50,000+ rows** of flight incident data across **5+ years**
- 🧠 ML classification models to detect risk triggers, improving early detection by **15%**
- 📦 Modular storage via Unity Catalog volumes; scalable transformation using Delta Lake
- 📊 Validated incident distributions and delay patterns for actionable operational insights

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

**[Notebook: `CrewOps_Risk_Model_Databricks.ipynb`]**  
⬇️  
**[Input → Cleaned Delta Table from ETL]**  
⬇️  
**[Model → Random Forest Classifier with `class_weight='balanced'`]**  
⬇️  
**[Output → Risk Flag Predictions + Evaluation Metrics]**

### 🚨 ML Module Summary

- 🧠 **Model Used:** Random Forest Classifier
- 📊 **Features:** Delay minutes, crew ID, aircraft ID, location
- ✅ **Accuracy:** 90% overall, with 92% recall for incident detection
- ⚖️ **Class Imbalance Handling:** `class_weight='balanced'` (no external libraries required)
- 🧱 **Platform:** Built on Databricks using Python, pandas, scikit-learn
- 📦 **Next Step:** Save predictions to Delta table for dashboard integration

![ML-Powered](https://img.shields.io/badge/ML--Powered-Risk%20Analytics-orange)

---

## 📂 Folder Structure

---

## 🚀 How to Run

1. Upload `sample_ops_data.csv` to Unity Catalog volume `ops_data`
2. Run `ETL_Sample_Ops.ipynb` in Databricks
3. Output saved to `ops_data_cleaned` volume and registered as Delta table
4. Run `CrewOps_Risk_Model_Databricks.ipynb` to train and evaluate ML model
5. Save predictions to Delta table or visualize using Databricks SQL

---

## 📎 Additional Assets

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

