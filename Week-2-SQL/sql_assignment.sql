SELECT * 
from sql_sales;

-- 1. Top Customers and Average Order Value
SELECT customer_name,
       SUM(total_price) AS total_sales,
       AVG(total_price) AS average_order_value
FROM sql_sales
GROUP BY customer_name
ORDER BY total_sales DESC;

-- 2. Average Order Value Across All Orders
SELECT AVG(total_price) AS average_order_value
FROM sql_sales;