print("PIZZAAAA")

size = input("podaj cz chcesz S M czy L\n")
pepperoni = input("chcesz pepperoni? Y or N\n")
extra_cheese = input("A serek? Y or N\n")
cena = 0
if size == "S":
    cena += 30 

elif size == "M":
    cena += 35

elif size == "L":
    cena += 40

if pepperoni == "Y":
    cena += 5
elif pepperoni == "N":
    cena = cena

if extra_cheese == "Y":
    cena += 8
if extra_cheese == "N":
    cena = cena

print(f"twoja pizza kosztuje: {cena}zl")