SELECT g.group_code , s2.name, s.name, m.grade
FROM students AS s
JOIN marks AS m ON s.id = m.student_id
JOIN subjects AS s2 ON m.subject_id = s2.id
JOIN groups g ON g.id = s.group_id 
ORDER BY g.id, s2.name 