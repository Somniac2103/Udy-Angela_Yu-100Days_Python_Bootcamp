# Intro
print("Welcome to the Coffee Express!")

# Data
machine = {
  'coffee' : 1000,
  'water' : 1000,
  'milk' : 1000,
}

Espresso = {
  'coffee' : 50,
  'water' : 50,
  'milk' : 0,
  'cost' : 0.25,
}

Latte = {
  'coffee' : 50,
  'water' : 50,
  'milk' : 100,
  'cost' : 1,
}

Cappuccino = {
  'coffee' : 50,
  'water' : 50,
  'milk' : 50,
  'cost' : 0.75,
}

# constants
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


# Functions
def check_resource(coffee, water, milk):
  print("Checking coffee supply...")
  if coffee <= machine['coffee']:
    print("Coffee ready.")
  else:
    print("Coffee not enough for selection")
    return
  print("Checking water supply...")
  if water <= machine['water']:
    print("Water ready.")
  else:
    print("Water not enough for selection")
    return
  print("Checking milk supply...")
  if milk <= machine['milk']:
    print("Milk ready.")
  else:
    print("Milk not enough for selection")
    return

def use_resources(coffee,water, milk):
  print(f'Preparing {option_name}...')
  print('Pouring milk...')
  machine[milk] = machine[milk] - milk
  print('Pouring coffee...')
  machine[coffee] = machine[coffee] - coffee
  print('Pouring water...')
  machine[water] = machine[water] - water
  print("Beverage Completed, enjoy")

# Prompt User
option = int(input("Please select your beverage?\n1: Espresso, 2: Latte or 3:Cappuccino\n"))

if option == 1:
  option_name = 'Espresso'
  cost = Espresso['cost']
  option_coffee = Espresso['coffee']
  option_water = Espresso['water']
  option_milk = Espresso['milk']
elif option == 2:
  option_name = 'Latte'
  cost = Latte['cost']
  option_coffee = Latte['coffee']
  option_water = Latte['water']
  option_milk = Latte['milk']
elif option == 3:
  option_name = 'Cappuccino'
  cost = Cappuccino['cost']
  option_coffee = Cappuccino['coffee']
  option_water = Cappuccino['water']
  option_milk = Cappuccino['milk']
print(f'You have selected {option_name}.')

#Check if enough resources to make selected option

check_resource(option_coffee,option_water ,option_milk )

#Payment Process
print(f'Your {option_name} will cost ${cost}.\nPlease insert coins:')
quarter_value = round(((float(input(f'Please enter the number of quarters you inserted? ')))*QUARTER),2)
print(f'You have inserted ${quarter_value} in quarters')
remainder = round((cost - quarter_value),2)
print(f'You still owe ${remainder}')
dime_value = round(((float(input(f'Please enter the number of dimes you inserted? ')))*DIME),2)
print(f'You have inserted ${dime_value} in dimes')
remainder = round((cost - _value),2)
print(f'You still owe ${remainder}')
nickel_value = round(((float(input(f'Please enter the number of nickels you inserted? ')))*NICKEL),2)
print(f'You have inserted ${nickel_value} in nickels')
remainder = remainder - nickel_value
print(f'You still owe ${remainder}')
pennies_value = round(((float(input(f'Please enter the number of pennies you inserted? ')))*PENNY),2)
print(f'You have inserted ${pennies_value} in pennies')
remainder = remainder - pennies_value
print(f'You still owe ${remainder}')

# Check transaction success
if remainder > 0:
  print("Insufficient funds")
else: print(f'You selected {option_name}.\nCost of {option_name}: ${cost}\nCash inserted ${cost - remainder}\nYour change is ${0 - remainder}')

#Make Coffee
use_resources(option_coffee, option_water,option_milk)

# Turn of coffee machine

#Show Status Report

