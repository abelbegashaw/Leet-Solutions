# Write your MySQL query statement below
SELECT customer_id
FROM (
    SELECT customer_id, COUNT(DISTINCT product_key) AS product_count
    FROM Customer
    GROUP BY customer_id
    ) AS c
WHERE c.product_count = (SELECT COUNT(Product.product_key) FROM Product)