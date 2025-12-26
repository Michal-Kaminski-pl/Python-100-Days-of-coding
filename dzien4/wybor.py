import random
lista = ["whiskey", "gin"]
## opcja
print(f"rachunek placi: {random.choice(lista)}")
## opcja 
random_index = random.randint(0, 1)

print(f"placi {lista[random_index]}")