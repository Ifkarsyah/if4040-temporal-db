queries = [
    {},
    {
        "sql":"""
            SELECT de.dept_no, dn.dept_name, COUNT(de.emp_no) as count_employee
            FROM employees e
                JOIN dept_emp de ON e.emp_no = de.emp_no
                JOIN departments dn ON de.dept_no = dn.dept_no
            WHERE de.from_date >= '1999-01-01' AND de.from_date <= '2000-01-01' 
            GROUP BY dn.dept_no
        """,
        "fields": ["dept_no", "dept_name", "count_employee"],
    },
    {
        "sql": """
            SELECT dn.dept_no, dn.dept_name, COUNT(de.emp_no) as count_employee

            FROM employees e
                JOIN dept_emp de ON e.emp_no = de.emp_no
                JOIN departments dn ON de.dept_no = dn.dept_no

            WHERE de.to_date >= NOW() 
            GROUP BY dn.dept_no
            ORDER BY dn.dept_no 

        """,
        "fields": ["dept_no", "dept_name", "count_employee"],
    },
    {
        "sql": """
        SELECT dn.dept_no, dn.dept_name, COUNT(de.emp_no) as count_employee

        FROM employees e
        JOIN dept_emp de ON e.emp_no = de.emp_no
        JOIN departments dn ON de.dept_no = dn.dept_no
        JOIN dept_manager dm ON dm.dept_no = dn.dept_no

        WHERE de.to_date <= dm.from_date AND dm.to_date >= NOW()
        GROUP BY dn.dept_no
        ORDER BY dn.dept_no  

        """,
        "fields": ["dept_no", "dept_name", "count_employee"],
    },
    {
        "sql": """
        SELECT e.first_name, e.last_name, e.gender

        FROM employees e
            JOIN dept_emp de ON e.emp_no = de.emp_no
            JOIN departments dn ON de.dept_no = dn.dept_no
            JOIN dept_manager dm ON dm.dept_no = dn.dept_no

        WHERE de.to_date = dm.from_date AND dm.to_date >= NOW() 
        AND dn.dept_name = "Production"  

        """,
        "fields": ["first_name", "last_name", "gender"],
    },
    {
        "sql": """
        SELECT dn.dept_no, dn.dept_name, COUNT(de.emp_no) as count_employee

        FROM departments dn
            JOIN dept_manager dm ON dn.dept_no = dm.dept_no
            JOIN dept_emp de ON dn.dept_no = de.dept_no
            JOIN employees e ON de.emp_no = e.emp_no

        WHERE dm.to_date <= NOW()
        AND de.from_date <= dm.to_date
        AND de.to_date >= NOW()
        GROUP BY dn.dept_no

        """,
        "fields": ["dept_no", "dept_name", "count_employee"],
    },
    {
        "sql": "TODO",
        "fields": ["TODO"],
    },
    {
        "sql": "TODO",
        "fields": ["TODO"],
    },
]