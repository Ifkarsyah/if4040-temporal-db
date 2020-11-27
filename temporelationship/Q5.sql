SELECT dn.dept_no, dn.dept_name, COUNT(de.emp_no) as count_employee

FROM departments dn
JOIN dept_manager dm ON dn.dept_no = dm.dept_no
JOIN dept_emp de ON dn.dept_no = de.dept_no
JOIN employees e ON de.emp_no = e.emp_no

WHERE dm.to_date <= NOW()
AND de.from_date <= dm.to_date
AND de.to_date >= NOW()
GROUP BY dn.dept_no

