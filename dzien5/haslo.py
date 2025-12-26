import random
litery = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbole = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
    '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>',
    '/', '?'
]

print("witaj w generowaniu hasla")
ile_liter = int(input("Podaj ile chcesz miec liter w hasle\n"))
ile_cyfr = int(input("Podaj ile chcesz miec cyfr w hasle\n"))
ile_symboli = int(input("Podaj ile chcesz miec symboli w hasle\n"))

##easy
haslo = ""
for litera in range(ile_liter):
    haslo += random.choice(litery)
for cyfra in range(ile_cyfr):
    haslo += random.choice(cyfry)
for symbol in range(ile_symboli):
    haslo += random.choice(symbole)

n = len(haslo)
haslo_listownie = []
for i in range(n):
    haslo_listownie.append(haslo[i])

random.shuffle(haslo_listownie)
delimiter = ""
haslo_koncowe = delimiter.join(haslo_listownie)
print(haslo_koncowe)