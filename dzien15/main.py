MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffe": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffe": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffe": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffe": 100,
}

is_on = True
def robienie_kawy(choice):
    if (resources["coffe"] - MENU[choice]['ingredients']['coffe'] < 0) or (resources["milk"] - MENU[choice]['ingredients']['milk']) < 0 or (resources["water"]- MENU[choice]['ingredients']['coffe'] < 0):
            print("Przepraszam, ekspres nie ma wystarczajaco rzeczy :c")
    else:
        print("Prosze twoja kawka")
        resources['water'] = resources['water'] - MENU[choice]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[choice]['ingredients']['milk']
        resources['coffe'] = resources['coffe'] - MENU[choice]['ingredients']['coffe']    
        return resources

def liczenie_kaski(choice):
    penny = 0.01
    dime = 0.5
    nickel = 0.10
    quarter = 0.25
    try:
        print(f"twoja kawka kosztuje: {MENU[choice]['cost']}")
        ilosc_penny = int(input("ile masz monet 0.01: "))
        ilosc_dime = int(input("ile masz monet 0.05: "))
        ilosc_nickel = int(input("ile masz monet 0.1: "))
        ilosc_quarter = int(input("ile masz monet 0.25: "))
        
        calosc = penny * ilosc_penny + dime * ilosc_dime + nickel * ilosc_nickel + quarter * ilosc_quarter
        reszta = calosc - MENU[choice]["cost"]

        if reszta < 0:
            print(f"sorki, nie masz wystarczajco pieniazkow, prosze zwrot :{calosc} zl")
            return None
        else:
            print(f"prosze tutaj reszta: {reszta} zl")
            resources['money'] = calosc - reszta
            return reszta, resources
    except ValueError:
        print("blad! prosze podac liczbe")
try:
    while is_on:
        choice = input("chcialbys espresso/cappucinno/latte? \n").lower()
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            print(f"w ekspresie zostalo \n {resources['water']} ml wody \n {resources['milk']} ml mleka \n {resources['coffe']} gramow kawy \n {resources['money']}")
        elif choice == 'admin':
            admin_on = True
            while admin_on == True:
                admin_choice = input("co chcesaz zrobic?\n").lower()
                if admin_choice == 'uzupelnic':
                    resources['water'] = 300
                    resources["milk"] = 200
                    resources['coffe'] = 100
                elif admin_choice == 'wyjdz':
                    print("Wychodze z trybu serwisowego")
                    admin_on = False
        elif choice in MENU:
            liczenie_kaski(choice)
            robienie_kawy(choice)

except ValueError:
    print("bledne dane mi sie wydaje")
    