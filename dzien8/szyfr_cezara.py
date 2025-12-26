alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    direction = input("wpisz 'encode', zeby zakodowac lub 'decode' zeby odszyfrowac: \n").lower()
    text = input("Wpisz swoj tekst: \n").lower()
    zmiana = int(input("Wpisz o ile chcesz przesunac \n"))
    
    def szyfrowanie(text, zmiana):
        nowy_text = ""
        text_list = [litera for litera in text]
        for litera in text_list:
            if litera == ' ':
                nowy_text += ' '
            else: 
                y = alfabet.index(litera) + zmiana
                y %= len(alfabet)
                nowy_text += alfabet[y]
        print(f"{nowy_text}")

    def odszyfrowanie(text, zmiana):
        nowy_text = ""
        text_list = [litera for litera in text]
        for litera in text_list:
            if litera == ' ':
                nowy_text += ' '
            else: 
                y = alfabet.index(litera) - zmiana
                y %= len(alfabet)
                nowy_text += alfabet[y]
        print(f"{nowy_text}")

    if direction == "encode":
        szyfrowanie(text, zmiana)
    elif direction == "decode":
        odszyfrowanie(text, zmiana)
    kontynuacja = input("Wpisz 'yes', jezeli chcesz kontynuowac, a 'no' jezeli zakonczyc program\n")

    if kontynuacja == "yes":
        continue
    elif kontynuacja == "no":
        exit()