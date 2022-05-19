
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokenmon name", ["Pikachu", "Squirt","Charmander"])
table.add_column("type" , ["Electric", "Water", "Fire"])
table.align = 'l'
print(table.align)
print(table)