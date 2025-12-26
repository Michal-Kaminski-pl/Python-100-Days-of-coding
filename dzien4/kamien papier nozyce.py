import random 
slownik = {"kamien": 
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 
           
           
"papier": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", 
"nozyce": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""" }

while True:
    wybor_uzytkownik = (input("Prosze podac czy wybierasz papier kamien czy nozyce: "))
    if wybor_uzytkownik == "kamien" or wybor_uzytkownik == "papier" or wybor_uzytkownik == "nozyce":
        
        wybor_konkuter = random.choice([slownik.keys()])
        if wybor_uzytkownik == wybor_konkuter:
            print(f"{wybor_uzytkownik}\n{wybor_konkuter}")
            print("gramy dalej")
        
        elif (wybor_konkuter == slownik['kamien'] and wybor_uzytkownik == slownik['nozyce']) or (wybor_konkuter == slownik['papier'] and wybor_uzytkownik == slownik['kamien']) or (wybor_konkuter == slownik['nozyce'] and wybor_uzytkownik == slownik['papier']):
            print(f"{wybor_uzytkownik}\n{wybor_konkuter}")
            print("Przegrales, gramy dalej!")
        
        elif (wybor_konkuter == slownik['kamien'] and wybor_uzytkownik == slownik['papier']) or (wybor_konkuter == slownik['papier'] and wybor_uzytkownik == slownik['nozyce']) or (wybor_konkuter == slownik['nozyce'] and wybor_uzytkownik == slownik['kamien']): 
            print(f"{wybor_uzytkownik}\n{wybor_konkuter}")
            print("wygrales, gramy dalej")
        else:
            print("blad!")
            exit()  

    else:
        print("blad!")
