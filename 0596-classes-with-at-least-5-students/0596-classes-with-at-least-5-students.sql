# Write your MySQL query statement below

SELECT class
FROM (
    SELECT class, Count(*) AS enrolled_students
    FROM Courses
    GROUP BY class
) AS enrollment
WHERE enrollment.enrolled_students > 4