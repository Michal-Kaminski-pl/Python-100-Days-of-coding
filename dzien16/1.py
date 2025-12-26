from prettytable import PrettyTable

table = PrettyTable()

table.add_column("pokemon", ["pikachu", "dragon", "squirrel"])
table.add_column("type", ["electric", "fire", "chuj"])
table.align = 'l'
print(table)
print(table.align)