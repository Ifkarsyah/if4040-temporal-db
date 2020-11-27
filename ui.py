from prettytable import PrettyTable

def print_menu():
    print("\n\nQUERY LIST")
    x = PrettyTable()
    x.field_names = ["QID", "Query", "Allen Relation"]
    x.add_row(["1", "Temukan daftar department dan jumlah employee-nya pada tahun 1999.", "contains"])
    x.add_row(["2", "Temukan jumlah employee untuk setiap departemen pada saat ini.", "finished by"])
    x.add_row(["3", "Temukan jumlah employee yang sudah keluar pada setiap departemen sebelum manajer saat ini menjadi manajer di departemen itu.", "preceded by"])
    x.add_row(["4", "Temukan employee yang keluar dari department “Production” pada saat manajer departemen tersebut menjabat", "meets"])
    x.add_row(["5", "Temukan jumlah employee pada setiap departemen yang sedang bekerja pada departemen tersebut namun pernah bekerja dengan manajer sebelumnya", "overlaps"])
    x.add_row(["6", "TODO", ""])
    x.add_row(["7", "TODO", ""])
    x.add_row(["8", "Temporal Delete", ""])
    x.add_row(["9", "Temporal Update", ""])
    x.add_row(["10", "Temporal Projection", ""])
    x.align = "l"
    print(x)
    print("Press CTRL + C to exit")