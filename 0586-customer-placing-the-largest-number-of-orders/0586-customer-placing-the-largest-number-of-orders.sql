# Write your MySQL query statement below

SELECT customer_number
FROM Orders GROUP BY customer_number
HAVING COUNT(*) = (
    SELECT MAX(sub.order_count)
    FROM (
        SELECT customer_number, COUNT(*) AS order_count
        FROM Orders GROUP BY customer_number
    ) AS sub
)

