#Query 1 – Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM financial_data;

#Query 2 – Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM financial_data;

#Query 3 – Total Units Sold
SELECT SUM(`Units Sold`) AS Total_Units_Sold
FROM financial_data;

#Query 4 – Sales by Country
SELECT Country,
       SUM(Sales) AS Total_Sales
FROM financial_data
GROUP BY Country
ORDER BY Total_Sales DESC;

#Query 5 – Profit by Country
SELECT Country,
       SUM(Profit) AS Total_Profit
FROM financial_data
GROUP BY Country
ORDER BY Total_Profit DESC;

#Query 6 – Sales by Product
SELECT Product,
       SUM(Sales) AS Total_Sales
FROM financial_data
GROUP BY Product
ORDER BY Total_Sales DESC;

#Query 7 – Profit by Product
SELECT Product,
       SUM(Profit) AS Total_Profit
FROM financial_data
GROUP BY Product
ORDER BY Total_Profit DESC;

#Query 8 – Sales by Segment
SELECT Segment,
       SUM(Sales) AS Total_Sales
FROM financial_data
GROUP BY Segment
ORDER BY Total_Sales DESC;

#Query 9 – Sales by Discount Band
SELECT `Discount Band`,
       SUM(Sales) AS Total_Sales
FROM financial_data
GROUP BY `Discount Band`
ORDER BY Total_Sales DESC;

#Query 10 – Monthly Sales
SELECT `Month Name`,
       SUM(Sales) AS Total_Sales
FROM financial_data
GROUP BY `Month Name`
ORDER BY MIN(`Month Number`);
