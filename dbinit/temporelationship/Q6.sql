SELECT e.emp_no, e.first_name, e.last_name, t.title

FROM departments dn
JOIN dept_manager dm ON dn.dept_no = dm.dept_no
JOIN dept_emp de ON dn.dept_no = de.dept_no
JOIN employees e ON de.emp_no = e.emp_no
JOIN titles t ON t.emp_no = e.emp_no

WHERE de.from_date = dm.from_date
AND dm.to_date >= NOW()
AND de.to_date >= NOW()
AND t.to_date >= NOW()
AND dn.dept_name = "Finance"