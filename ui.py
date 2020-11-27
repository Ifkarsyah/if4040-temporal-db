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
    x.add_row(["6", "Temukan semua employee dan jabatannya pada departemen Finance yang masuk bersamaan dengan manajer pada departemen tersebut", "start"])
    x.add_row(["7", "Temukan semua employee lain yang memiliki waktu kontrak kerja sama dengan ‘Georgi Facello’", "equal"])
    x.add_row(["8", "Temporal Delete", "*manipulation"])
    x.add_row(["9", "Temporal Update", "*manipulation"])
    x.add_row(["10", "Temporal Projection", "*temporal"])
    x.add_row(["11", "Temporal Union", "*temporal"])
    x.add_row(["12", "Temporal Difference", "*temporal"])
    x.add_row(["13", "Temporal Join", "*temporal"])
    x.align = "l"
    print(x)
    print("Press CTRL + C to exit")