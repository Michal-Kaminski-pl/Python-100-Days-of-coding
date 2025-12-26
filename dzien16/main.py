from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
ekspres = CoffeeMaker()
placenie = MoneyMachine()
while True:
    choice = input(f"co bys chcial {menu.get_items()}?\n").lower()
    if choice == 'report':
        print(f"{ekspres.report()} , profit: {placenie.report()}")
    if choice == 'off':
        break
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        mozna = ekspres.is_resource_sufficient(drink)
        if mozna == False:
            break
        else:
            koszt = drink.cost
            zaplata = placenie.make_payment(koszt)
            if zaplata == True:
                ekspres.make_coffee(drink)
            else:
                continue



