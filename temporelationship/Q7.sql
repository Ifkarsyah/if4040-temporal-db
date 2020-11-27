SELECT e2.emp_no, e2.first_name, e2.last_name, e2.gender

FROM dept_emp de1
JOIN employees e1 ON e1.emp_no = de1.emp_no
JOIN dept_emp de2
JOIN employees e2 ON e2.emp_no = de2.emp_no

WHERE e1.first_name = 'Georgi' AND e1.last_name = 'Facello'
AND de1.from_date = de2.from_date
AND de1.to_date = de2.to_date
AND !(e2.first_name = 'Georgi' AND e2.last_name = 'Facello')

