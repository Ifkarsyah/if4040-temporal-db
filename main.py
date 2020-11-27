# Module Imports
from prettytable import PrettyTable
from pprint import pprint

from ui import print_menu
from dbconn import get_db_cursor

cur = get_db_cursor()

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
]

while True:
    print_menu()
    query_id = int(input("Query ID: "))

    x = PrettyTable()
    if query_id >= 1 and query_id < len(queries):
        q = queries[query_id]

        if q["sql"] != "TODO":
            cur.execute(q["sql"])
            x.field_names = q["fields"]
            for c in cur:
                x.add_row(c)
            print(x)

    
