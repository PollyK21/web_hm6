SELECT s.name AS student_name,
       t.name AS teacher_name,
       (SELECT STRING_AGG(s2.name, '; ') 
       FROM (SELECT DISTINCT s2.name
       FROM marks m
       JOIN subjects s2 ON m.subject_id = s2.id
       WHERE t.id = s2.teacher_id) AS s2) AS course_names
FROM students s
JOIN marks m ON s.id = m.student_id 
JOIN subjects s2 ON m.subject_id = s2.id
JOIN teachers t ON s2.teacher_id = t.id
GROUP BY s.name, t.name;