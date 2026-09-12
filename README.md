# 📊 Financial Sales Analysis

## 📌 Project Overview

Financial Sales Analysis is an end-to-end data analytics project that analyzes financial sales data to understand sales performance, profitability, product performance, customer segments, country-wise sales, monthly trends, and the impact of discount bands.

The project uses **Python, SQL, Excel, and Power BI** to clean, analyze, visualize, and present business insights from the dataset.

---

## 🎯 Project Objectives

- Clean and preprocess the financial sales dataset
- Calculate important business KPIs
- Analyze sales and profit by product
- Analyze sales across countries
- Compare customer segments
- Identify monthly sales trends
- Analyze the relationship between discount bands and profit
- Develop an interactive Power BI dashboard
- Generate actionable business insights

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **OpenPyXL**
- **SQL / MySQL**
- **Microsoft Excel**
- **Power BI**
- **Git & GitHub**

---

## 📂 Dataset

The dataset contains **700 sales records** with information including:

- Segment
- Country
- Product
- Discount Band
- Units Sold
- Manufacturing Price
- Sale Price
- Gross Sales
- Discounts
- Sales
- COGS
- Profit
- Date
- Month
- Year

---

## 🧹 Data Cleaning & Preprocessing

Python was used to prepare the dataset for analysis.

The following steps were performed:

- Loaded the Excel dataset using Pandas
- Inspected rows, columns, data types, and statistics
- Identified missing values
- Handled missing values in the Discount Band column
- Checked for duplicate records
- Verified that no duplicate records were present
- Standardized column names
- Exported the cleaned dataset as `Cleaned_Data.xlsx`

The cleaned dataset was then used for SQL analysis and Power BI dashboard development.

---

## 🔎 SQL Analysis

SQL was used to perform business analysis and calculate KPIs.

Key queries included:

- Total number of records
- Total Sales
- Total Profit
- Total Units Sold
- Sales by Country
- Profit by Product
- Sales by Customer Segment
- Monthly Sales Trends
- Top Products by Profit

The SQL analysis was performed using a `financial_sales` database and `financial_data` table.

---

## 📊 Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Sales | **118.73 Million** |
| Total Profit | **16.89 Million** |
| Units Sold | **1.13 Million** |
| Total Records | **700** |

---

## 📈 Power BI Dashboard

An interactive Power BI dashboard was developed to visualize the analysis.

### Dashboard Components

- Total Sales KPI
- Total Profit KPI
- Units Sold KPI
- Sales by Country
- Monthly Sales Trend
- Profit by Product
- Profit by Discount Band
- Sales by Customer Segment
- Year Slicer
- Country Slicer
- Segment Slicer

The dashboard allows users to dynamically explore business performance by **Year, Country, and Customer Segment**.

---

## 💡 Key Business Insights

### 1. Overall Sales
The business generated approximately **118.73 Million in total sales**.

### 2. Profitability
The total profit generated was approximately **16.89 Million**.

### 3. Top Product
**Paseo** generated the highest profit among the products analyzed.

### 4. Top Country
The **United States of America** recorded the highest sales among the countries in the dataset.

### 5. Customer Segment
The **Government segment** generated the highest overall sales, followed by the Small Business segment.

### 6. Monthly Trend
Sales varied across the year, with **October recording the highest monthly sales performance**.

### 7. Discount Analysis
Products in the **Low Discount Band** generated the highest overall profit compared with Medium and High discount bands.

These findings can help businesses improve product focus, market strategy, customer relationships, and discount policies.

---

## 📌 Business Recommendations

- Focus more on high-performing products such as **Paseo**
- Strengthen business operations in the **United States**
- Develop targeted strategies for lower-performing markets
- Maintain strong relationships with Government customers
- Review discount strategies to protect profitability
- Monitor monthly sales trends for inventory planning
- Use Power BI dashboards for continuous KPI monitoring

---

## 📁 Project Structure

Financial-Sales-Analysis/

├── Sample data (1).xlsx  
├── Cleaned_Data.xlsx  
├── analysis.py  
├── Queries.sql  
├── analysis.pbix  
│
├── KPI_Summary.xlsx  
├── Monthly_Sales.xlsx  
├── Profit_by_Product.xlsx  
├── Sales_by_Country.xlsx  
├── Sales_by_Segment.xlsx  
├── Top10Products.xlsx  
│
├── Dashboard_Profit.png  
├── Monthly_Sales.png  
├── Profit_by_Discount.png  
├── Profit_by_Product.png  
├── Sales_by_Country.png  
└── Sales_by_Segment.png  

---

## 🚀 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Python Data Analysis
- SQL Querying
- Data Visualization
- Microsoft Excel
- Power BI Dashboard Development
- KPI Analysis
- Business Intelligence
- Business Insight Generation

---

## 🔮 Future Scope

Possible improvements include:

- Real-time database integration
- Power BI Service deployment
- Automated ETL pipelines
- Sales and profit forecasting using Machine Learning
- Additional business KPIs
- Advanced Power BI drill-through and reporting features

---

## 👩‍💻 Author

**Varsha NG**

Aspiring Data Analyst | Python | SQL | Excel | Power BI
