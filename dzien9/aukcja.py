slownik = {}
def dodanie():
    imie = input("prosze podac swoje imie: ")
    cena = input("prosze podac swoja cene: $")
    slownik[imie] = cena
    return slownik 
dodanie()
while True:
    nastepny = input("czy jest kolejny hazardzista? 'tak' jezeli tak, a 'nie' jezeli nie\n")
    if nastepny == "tak":
        print("\n" * 50)
        dodanie()
    elif nastepny == "nie":
        wygrany_wynik = max(slownik.values())
        print(f"Wygrywa {max(slownik, key = slownik.get)} z cena {wygrany_wynik}")
        exit()
