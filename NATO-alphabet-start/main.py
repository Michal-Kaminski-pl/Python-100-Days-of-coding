import pandas as pd 
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
slownik = {f"{row.letter}":f"{row.code}" for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
wyraz = str(input("Prosze podaj swoj wyraz do przekonwertowania fonetycznego\n"))
wyraz_fonetycznie = [slownik[letter.upper()] for letter in wyraz]
print(wyraz_fonetycznie)
