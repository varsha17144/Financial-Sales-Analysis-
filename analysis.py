import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Dataset
file_path = "Sample data (1).xlsx"
df = pd.read_excel(file_path)
print("="*60)
print("DATASET LOADED SUCCESSFULLY")
print("="*60)

# Dataset Information
print("\nFirst 5 Rows")
print(df.head())
print("\nShape")
print(df.shape)
print("\nColumns")
print(df.columns)
print("\nInfo")
print(df.info())
print("\nSummary Statistics")
print(df.describe())

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing text values with mode
text_cols = df.select_dtypes(include=['object']).columns
for col in text_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])
print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# Remove Duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate Rows :", duplicates)
df = df.drop_duplicates()

# Clean Column Names
df.columns = df.columns.str.strip()

# Create Output Folder
if not os.path.exists("Output"):
    os.makedirs("Output")

# Save Cleaned Dataset
df.to_excel("Output/Cleaned_Data.xlsx", index=False)
print("\nCleaned Dataset Saved")

# KPI Calculations
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_units = df["Units Sold"].sum()
average_profit = df["Profit"].mean()
print("\n========== KPI ==========")
print("Total Sales :", total_sales)
print("Total Profit :", total_profit)
print("Units Sold :", total_units)
print("Average Profit :", average_profit)

# Sales by Country
sales_country = df.groupby("Country")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Country")
print(sales_country)
sales_country.to_excel("Output/Sales_by_Country.xlsx")

# Profit by Product
profit_product = df.groupby("Product")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Product")
print(profit_product)
profit_product.to_excel("Output/Profit_by_Product.xlsx")

# Sales by Segment
sales_segment = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Segment")
print(sales_segment)
sales_segment.to_excel("Output/Sales_by_Segment.xlsx")

# Sales by Discount Band
discount_profit = df.groupby("Discount Band")["Profit"].sum()
discount_profit.to_excel("Output/Profit_by_Discount.xlsx")

# Monthly Sales
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%B")
monthly_sales = df.groupby("Month")["Sales"].sum()
month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]
monthly_sales = monthly_sales.reindex(month_order)
monthly_sales.to_excel("Output/Monthly_Sales.xlsx")

# Top 10 Products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)
top_products.to_excel("Output/Top10Products.xlsx")

# Charts
plt.figure(figsize=(10,5))
sales_country.plot(kind="bar")
plt.title("Sales by Country")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Output/Sales_by_Country.png")
plt.close()

plt.figure(figsize=(10,5))
profit_product.plot(kind="bar", color="green")
plt.title("Profit by Product")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("Output/Profit_by_Product.png")
plt.close()

plt.figure(figsize=(8,8))
sales_segment.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales by Segment")
plt.tight_layout()
plt.savefig("Output/Sales_by_Segment.png")
plt.close()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Output/Monthly_Sales.png")
plt.close()

plt.figure(figsize=(8,5))
discount_profit.plot(kind="bar")
plt.title("Profit by Discount Band")
plt.tight_layout()
plt.savefig("Output/Discount_Profit.png")
plt.close()

# Export Summary
summary = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Units Sold",
        "Average Profit"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_units,
        average_profit
    ]
})
summary.to_excel("Output/KPI_Summary.xlsx", index=False)

# Business Insights
print("\n==============================")
print("BUSINESS INSIGHTS")
print("==============================")

print("\nHighest Sales Country :", sales_country.idxmax())
print("Highest Profit Product :", profit_product.idxmax())
print("Highest Sales Segment :", sales_segment.idxmax())
print("Best Discount Band :", discount_profit.idxmax())

print("\nAll files saved inside Output folder.")

print("\nProject Completed Successfully!")