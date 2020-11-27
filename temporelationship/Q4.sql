SELECT e.first_name, e.last_name, e.gender

FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments dn ON de.dept_no = dn.dept_no
JOIN dept_manager dm ON dm.dept_no = dn.dept_no

WHERE de.to_date = dm.from_date AND dm.to_date >= NOW() 
AND dn.dept_name = "Production" 