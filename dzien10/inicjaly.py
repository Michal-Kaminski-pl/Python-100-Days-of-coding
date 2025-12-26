def format_name(f_name, l_name):
    return f_name[0] +  l_name[0]

f_name = input("Podaj swoje imie\n").title()
l_name = input("Podaj swoje naziwsko\n").title()

inicjaly = format_name(f_name, l_name)
print(inicjaly)

