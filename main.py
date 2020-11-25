# Module Imports
import mariadb
import sys
from prettytable import PrettyTable
from pprint import pprint

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="ifkarsyah",
        password="password",
        host="localhost",
        port=3306,
        database="employees"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

def print_menu():
    print("\n\n------------------------------------\nQUERY LIST")
    x = PrettyTable()
    x.field_names = ["QID", "Query"]
    x.add_row(["1", "Find employee"])
    print(x)
    print("Press CTRL + C to exit")



while True:
    print_menu()
    query_id = int(input("Query ID: "))

    if query_id == 1:
        cur.execute("""
        SELECT de.dept_no, dn.dept_name, COUNT(de.emp_no) as count_employee
        FROM employees e
            JOIN dept_emp de ON e.emp_no = de.emp_no
            JOIN departments dn ON de.dept_no = dn.dept_no
        WHERE de.from_date >= '1999-01-01' AND de.from_date <= '2000-01-01' 
        GROUP BY dn.dept_no

        """)
        x = PrettyTable()
        x.field_names = ["dept_no", "dept_name", "count_employee"]
        for c in cur:
            x.add_row(c)
        print(x)

    
