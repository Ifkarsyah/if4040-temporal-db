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
        "sql": """
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
        """,
        "fields": ["emp_no", "first_name", "last_name", "title"],
    },
    {
        "sql": """
        SELECT e2.emp_no, e2.first_name, e2.last_name, e2.gender

        FROM dept_emp de1
        JOIN employees e1 ON e1.emp_no = de1.emp_no
        JOIN dept_emp de2
        JOIN employees e2 ON e2.emp_no = de2.emp_no

        WHERE e1.first_name = 'Georgi' AND e1.last_name = 'Facello'
        AND de1.from_date = de2.from_date
        AND de1.to_date = de2.to_date
        AND !(e2.first_name = 'Georgi' AND e2.last_name = 'Facello')
        """,
        "fields": ["emp_no", "first_name", "last_name", "gender"],
    },
    {
        "sql": "CALL employees.DeleteTemporal(‘salaries’, ‘1986-06-26’,’1987-06-27);",
        "fields": [],
    },
    {
        "sql": """
        UPDATE salaries FOR PORTION OF valid_period
        FROM ‘1986-06-26'
        TO '1987-06-26'
        SET salary = 100000
        """,
        "fields": [],
    },
    {
        "sql": "CALL employees.projection('salaries','emp_no');",
        "fields": []
    },
    {
        "sql": """
        SELECT emp_no, dept_no, min(from_date) as from_date, max(to_date) as to_date
        FROM
        (SELECT * FROM dept_manager
        UNION
        SELECT * FROM dept_emp) AS u
        GROUP BY emp_no, dept_no LIMIT 20;
        """,
        "fields": ["emp_no", "dept_no", "from_date", "to_date"],
    },
    {
        "sql": """
        SELECT emp_no, dept_no, min(from_date) as from_date, max(to_date) as to_date
        FROM
        (SELECT * FROM dept_emp
        EXCEPT
        SELECT * FROM dept_manager) AS u
        GROUP BY emp_no, dept_no LIMIT 20;
        """,
        "fields": ["emp_no", "dept_no", "from_date", "to_date"],
    },
    {
        "sql": """
        SELECT dept_manager.emp_no, dept_manager.dept_no, salaries.salary,
            IF(dept_manager.from_date >= salaries.from_date, dept_manager.from_date, salaries.from_date) AS from_date,
            IF(dept_manager.to_date <= salaries.to_date, dept_manager.to_date, salaries.to_date) AS to_date
        FROM dept_manager INNER JOIN salaries
        ON dept_manager.emp_no = salaries.emp_no LIMIT 20;
        """,
        "fields": ["emp_no", "dept_no", "salary", "from_date", "to_date"],
    }
]