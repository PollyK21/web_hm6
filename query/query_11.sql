SELECT s2.name, t.name, AVG(m.grade)
FROM marks m 
JOIN subjects s ON m.subject_id = s.id 
JOIN teachers t ON t.id = s.teacher_id 
JOIN students s2 ON m.student_id =s2.id
GROUP BY s2.id, t.id 