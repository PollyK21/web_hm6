SELECT s.name, b.name, m.max_average_grade
FROM students AS s
JOIN(
    SELECT subject_id, student_id, MAX(average_grade) AS max_average_grade 
    FROM (
        SELECT subject_id, student_id, AVG(grade) AS average_grade
        FROM marks
        GROUP BY subject_id, student_id
    )
    GROUP BY subject_id) AS m ON s.id = m.student_id
 JOIN subjects AS b ON b.id = m.subject_id
 