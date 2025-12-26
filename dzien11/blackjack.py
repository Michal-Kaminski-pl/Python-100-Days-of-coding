import random
karty = {'A': 11, '2': 2, '3': 3, '4': 4, '5':5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

def wyniki(karty_x):
    wynik = sum(karty[klucz] for klucz in karty_x)
    
    liczba_asow = karty_x.count('A')
    while wynik > 21 and liczba_asow > 0:
        wynik -= 10
        liczba_asow -= 1
    return wynik

def ogloszenie_wynikow(karty_gracza, karty_krupiera, wynik_gracza, wynik_krupiera):
    print(f"Twoje karty \n {karty_gracza} \n {karty_krupiera}")
    if wynik_gracza > 21:
        print("BUST!, przegrales")
    elif wynik_krupiera > 21:
        print("krupier bust, wygrales")
    elif wynik_gracza == 21 and wynik_krupiera != 21:
        print("BLACKJACK")
    elif wynik_krupiera == 21 and wynik_gracza != 21:
        print("Krupier ma blackjacka, przegrales")
    elif wynik_krupiera == wynik_gracza:
        print("REMIS")
    elif wynik_gracza < wynik_krupiera:
        print("Przegrales")
    elif wynik_gracza > wynik_krupiera:
        print("wygrales")


def hit_or_stand(karty_gracza, karty_krupiera):
    kontynuacja = input("'Hit' or 'Stand'(wpisz 'H' lub 'S')?\n").title()
    if kontynuacja == 'H':
        karty_gracza.append(random.choice(list(karty)))
        wynik_gracza = wyniki(karty_gracza)
        print(f"Twoje karty: [{karty_gracza}]")
        if wynik_gracza > 21:
            ogloszenie_wynikow(karty_gracza, karty_krupiera, wynik_gracza, wynik_krupiera = wyniki(karty_krupiera) )
        else:
            hit_or_stand(karty_gracza, karty_krupiera)
    elif kontynuacja == 'S':
        wynik_gracza = wyniki(karty_gracza)
        ruch_krupiera(karty_gracza, karty_krupiera, wynik_gracza)

def ruch_krupiera(karty_gracza, karty_krupiera, wynik_gracza):
    wynik_krupiera = wyniki(karty_krupiera)
    print(f"karty krupiera: [{karty_krupiera}]")
    while wynik_krupiera < 17:
        karty_krupiera.append(random.choice(list(karty)))
        wynik_krupiera = wyniki(karty_krupiera)
        print(karty_krupiera)
    ogloszenie_wynikow(karty_gracza, karty_krupiera, wynik_gracza, wynik_krupiera)

print("Witaj w blackjacku\n")
while True:
    karty_gracza = []
    while len(karty_gracza) < 2:
        karty_gracza.append(random.choice(list(karty)))
    karty_krupiera = []
    while len(karty_krupiera) < 2:
        karty_krupiera.append(random.choice(list(karty)))
    wynik_gracza = wyniki(karty_gracza)
    print(f"Twoje karty: [{karty_gracza}]")
    print(f"Karty krupiera [{karty_krupiera[0]}]")
    hit_or_stand(karty_gracza, karty_krupiera)

    wybor = input("Czy chcesz kontynuowac gre? enter jezeli tak, a jezeli nie, to cokolwiek innego\n").lower()

    if wybor == '':
        continue
    else:
        print("dzieki")
        exit()








