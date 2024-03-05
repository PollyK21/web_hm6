SELECT g.group_code, s.name
FROM students s
JOIN groups g ON g.id = s.group_id 
ORDER BY g.id