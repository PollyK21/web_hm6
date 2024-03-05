SELECT t.name, AVG(m.grade) AS average_grade
FROM teachers t 
JOIN subjects s ON s.teacher_id = t.id 
JOIN marks m ON m.subject_id = s.id
GROUP BY t.id;