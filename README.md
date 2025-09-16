# ✈️ Operational Safety & Risk Analytics

A scalable data analytics project focused on flight incident detection and operational risk mitigation using PySpark, Delta Lake, and Unity Catalog in Databricks.

---

## 📌 Project Highlights

- 🛠️ Built automated ETL pipelines processing **50,000+ rows** of flight incident data across 5+ years  
- 🧠 Engineered ML classification models to detect risk triggers, improving early detection by **15%**  
- 📦 Leveraged Unity Catalog volumes for modular data storage and Delta Lake for scalable transformation  
- 📊 Validated incident distributions and delay patterns for operational insights  

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

## 📂 Folder Structure
# Operational-Safety-Risk-Analytics-


---

## 🚀 How to Run

1. Upload `sample_ops_data.csv` to Unity Catalog volume `ops_data`
2. Run `ETL_Sample_Ops.ipynb` in Databricks
3. Output saved to `ops_data_cleaned` volume and registered as Delta table
4. Query using SQL or visualize in dashboards

---

## 📎 Additional Assets

- 📊 [Notebook Preview](#) *(optional: link to Databricks notebook preview or screenshot)*  
- 🖼️ [Incident Distribution Screenshot](#) *(optional: embed image for visual impact)*

---

## 🙌 Acknowledgments

Built with Databricks, PySpark, Delta Lake, and Unity Catalog.  
Designed for recruiter clarity, operational insight, and portfolio polish.

---

