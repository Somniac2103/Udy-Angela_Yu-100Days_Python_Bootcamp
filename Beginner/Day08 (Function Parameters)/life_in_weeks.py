def life_in_weeks(current_age):
    weeks_left = (90-current_age)*52
    return print(f'You have {weeks_left} weeks left.')

current_age = int(input("What is your current age? "))

life_in_weeks(current_age)