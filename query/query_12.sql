SELECT g.group_code, s2.name AS subject_name, s.name AS student_name, m.grade, m.date 
FROM students AS s
JOIN marks AS m ON s.id = m.student_id
JOIN subjects AS s2 ON m.subject_id = s2.id
JOIN groups AS g ON g.id = s.group_id 
JOIN (
    SELECT student_id, subject_id, MAX(date) AS max_date
    FROM marks
    GROUP BY student_id, subject_id
) AS latest_marks ON m.student_id = latest_marks.student_id 
                AND m.subject_id = latest_marks.subject_id
                AND m.date = latest_marks.max_date
GROUP BY g.group_code, s2.name, s.name
ORDER BY g.group_code, s2.name, s.name;