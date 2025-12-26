def life_in_weeks(current_age):
    remaining_weeks = ( 90 - current_age) * 52  
    print(f"You have {remaining_weeks} weeks left")

wiek = int(input("Prosze podac swoj wiek w latach"))

life_in_weeks(wiek)