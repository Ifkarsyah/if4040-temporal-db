# Module Imports
from prettytable import PrettyTable

from pprint import pprint
from time import sleep

from ui import print_menu
from dbconn import get_db_cursor
from queries import queries

cur = get_db_cursor()

rep = True
while rep:
    print_menu()
    query_id = int(input("Query ID: "))
    print("Result:")

    x = PrettyTable()
    if query_id >= 1 and query_id < len(queries):
        q = queries[query_id]

        if q["sql"] != "TODO":
            cur.execute(q["sql"])
            x.field_names = q["fields"]
            for c in cur:
                x.add_row(c)
            print(x)
    
    user_rep = input("Repeat? (y / n): ")
    while user_rep != "y" and user_rep != "n":
        user_rep = input("Repeat? (y / n): ")
    rep = (user_rep == "y")
