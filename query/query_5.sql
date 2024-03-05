SELECT t.name,
    (SELECT STRING_AGG(s.name , ', ') AS course_names
    FROM subjects s
    WHERE t.id = s.teacher_id
    GROUP BY s.teacher_id) AS course_names
FROM teachers t