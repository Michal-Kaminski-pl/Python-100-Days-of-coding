import random
from game_data import data
from art import logo, vs

def losowanie(poprzedni_zwyciezca = None):
    if poprzedni_zwyciezca:
        a_data = poprzedni_zwyciezca
        b_data = random.choice(data)
        while a_data == b_data:
            b_data = random.choice(data)
        return a_data, b_data
        
    
    else:
        a_data = random.choice(data)
        b_data = random.choice(data)
        while a_data == b_data:
            b_data = random.choice(data)
        return a_data, b_data
def more(A, B):
    if A['follower_count'] > B['follower_count']:
        return A
    else:
        return B
def game():
    score = 0
    A, B = losowanie()
    while True:
        print(logo)
        print(f"twoj wynik: {score}")
        print(f"A: {A['name']}, {A['description'].lower()}, {A['country']} \n {vs} \n B: {B['name']}, {B['description'].lower()}, {B['country']}")
        wieksze = more(A, B)
        try:
            wybor = input(f"{A['name']} czy {B['name']} ma wiecej milionow na ig? Wpisz 'A' lub 'B' \n").upper()
            if wybor == 'A':
                wybor = A
            elif wybor == 'B':
                wybor = B

            if wybor == wieksze:
                print("brawo!")
                score += 1
                A, B = losowanie(poprzedni_zwyciezca= wieksze)
                continue
            elif wybor != wieksze:
                print(f"przegrales! wynik = {score}")
                break
        except ValueError:
            print("bledne dane!!!")
            return None
game()