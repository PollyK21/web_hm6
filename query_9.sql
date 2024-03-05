SELECT s.name,
       (SELECT STRING_AGG(s2.name, '; ')
        FROM (SELECT DISTINCT s2.name
              FROM marks m
              JOIN subjects s2 ON m.subject_id = s2.id
              WHERE s.id = m.student_id) AS s2) AS course_names
FROM students s;        