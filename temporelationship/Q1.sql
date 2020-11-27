SELECT de.dept_no, dn.dept_name, COUNT(de.emp_no) as count_employee

FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments dn ON de.dept_no = dn.dept_no

WHERE de.from_date >= '1999-01-01' AND de.from_date <= '1999-01-01' 
GROUP BY dn.dept_no
