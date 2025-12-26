def calculate_love_score(name1, name2):
    love = "LOVE"
    true = "TRUE"
    love_scr = 0
    true_scr = 0
    for litera in love:
        love_scr = name1.count(litera) + name2.count(litera)
    for litera in true:
        true_scr = name1.count(litera) + name2.count(litera)

    love_score = str(love_scr) + str(true_scr)
    print(f"{love_score}")

name1 = input("Podaj swoje imie\n").upper()
name2 = input("Podaj imie swojej ukochanej\n").upper()

calculate_love_score(name1, name2)