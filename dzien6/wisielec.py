import random

word_list = [ "dom",
    "drzewo",
    "książka",
    "komputer",
    "słońce",
    "pies",
    "kot",
    "samochód",
    "miasto",
    "rzeka",
    "chodzić",
    "biegać",
    "czytać",
    "pisać",
    "mówić",
    "szybki",
    "zielony",
    "wesoły",
    "duży",
    "mały",
    "zawsze",
    "często",
    "teraz",
    "jutro",
    "gdzie",
    "kto",
    "jaki",
    "dlaczego",
    "ale",
    "i",
    "lub",
    "ponieważ"
    ]

choosen_word = random.choice(word_list)
display_list = ["_" for litera in choosen_word]
display = "".join(display_list)
wisielec = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(f"Gramy w wisielca, twoje slowo:")
zycia = 0
while "_" in display_list:
    print(f"{display}")
    guess = input("prosze podac swoja literke\n").lower()
    if guess in display_list:
        print("juz wpisales ta literke!")
        continue
    for i, litera in enumerate(choosen_word):
            if guess == litera:
                display_list[i] = guess
                display = "".join(display_list)
                print("dobrze chujku \n")
                print(wisielec[zycia])
    if guess not in choosen_word:
        zycia += 1
        print("zle chujku\n")
        
        print(wisielec[zycia])
        if zycia == 6:
            print("przegrales")
            break       

if not "_" in display and zycia < 0:
     print(f"wygrales, twoje slowo to {display}")
