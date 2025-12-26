def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    return a / b

a = float(input("podaj pierwsza licze\n"))

while True:    
    operacja = input("wybierz operacje: \n + \n - \n * \n / \n")
    b = float(input("podaj druga liczbe\n"))
    if operacja == "+":
        a = dodawanie(a, b)
        print(a)
    elif operacja == "-":
        a = odejmowanie(a, b)
    elif operacja == "*":
        a = mnozenie(a, b)
    elif operacja == "/":
        a = dzielenie(a, b)
    seks = input(f"wpisz 'y', zeby kontynuowac obliczenia z {a}, 'n' zeby wpisac nowe liczby, albo 'chuj' zeby zakonczyc program")
    if seks == "y":
        continue
    elif seks == "n":
        a = float(input("podaj pierwsza licze\n"))
    elif seks == "chuj":
        exit()
    else:
        print("nie wiem o co ci chodzi xd\n")
        exit()