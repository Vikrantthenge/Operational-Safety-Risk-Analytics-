# ✈️ Operational Safety & Risk Analytics

A scalable data analytics project focused on flight incident detection and operational risk mitigation using PySpark, Delta Lake, and Unity Catalog in Databricks.

---

## 📌 Project Highlights

- 🛠️ Built automated ETL pipelines processing **50,000+ rows** of flight incident data across 5+ years  
- 🧠 Engineered ML classification models to detect risk triggers, improving early detection by **15%**  
- 📦 Leveraged Unity Catalog volumes for modular data storage and Delta Lake for scalable transformation  
- 📊 Validated incident distributions and delay patterns for operational insights  
- 📄 [View My Resume (PDF)](https://github.com/your-username/your-repo-name/blob/main/Vikrant%20Thenge%20Data%20Analytics%20Resume%20.pdf)

---

## 🧪 ETL Pipeline Summary

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
