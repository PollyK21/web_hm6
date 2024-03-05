SELECT s.name, m.average_grade
FROM students AS s
JOIN (
    SELECT student_id, AVG(grade) AS average_grade
    FROM marks
    GROUP BY student_id
    ORDER BY average_grade DESC
    LIMIT 5
) AS m ON s.id = m.student_id;