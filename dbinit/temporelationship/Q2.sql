SELECT dn.dept_no, dn.dept_name, COUNT(de.emp_no) as count_employee

FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments dn ON de.dept_no = dn.dept_no

WHERE de.to_date >= NOW() 
GROUP BY dn.dept_no
ORDER BY dn.dept_no 