# Write your MySQL query statement below
WITH another_table AS (
    SELECT 
        max(id) AS leaf, p_id
    FROM Tree
    GROUP BY p_id
),
tree_table AS (
    SELECT Tree.id, Tree.p_id, another_table.leaf
    FROM Tree LEFT JOIN another_table ON Tree.id = another_table.p_id
)

SELECT tree_table.id,

    CASE
        WHEN tree_table.p_id IS NULL THEN 'Root'
        WHEN tree_table.leaf IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END AS type

    FROM tree_table






/*
node  parent child
1      null    2,3
2       1      4,5
3       1       null
4       2       null
5       2       null

*/