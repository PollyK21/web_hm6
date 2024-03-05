SELECT s.group_id, s2.name, AVG(m.grade) AS average_grade
FROM students AS s
JOIN marks AS m ON s.id = m.student_id
JOIN subjects AS s2 ON m.subject_id = s2.id
GROUP BY s.group_id, m.subject_id;