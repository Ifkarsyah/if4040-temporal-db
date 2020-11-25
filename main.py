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
        "sql": "TODO",
        "fields": ["TODO"],
    },
    {
        "sql": "TODO",
        "fields": ["TODO"],
    },
    {
        "sql": "TODO",
        "fields": ["TODO"],
    },
    {
        "sql": "TODO",
        "fields": ["TODO"],
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

    
