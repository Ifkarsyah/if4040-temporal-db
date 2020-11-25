from prettytable import PrettyTable

def print_menu():
    print("\n\n------------------------------------\nQUERY LIST")
    x = PrettyTable()
    x.field_names = ["QID", "Query"]
    x.add_row(["1", "Find employee"])
    print(x)
    print("Press CTRL + C to exit")