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
}

Latte = {
  'coffee' : 50,
  'water' : 50,
  'milk' : 100,
}

Cappuccino = {
  'coffee' : 50,
  'water' : 50,
  'milk' : 50,
}

# constants



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



# Prompt User
option = int(input("Please select your beverage?\n1: Espresso, 2: Latte or 3:Cappuccino\n"))

if option == 1:
  option_name = 'Espresso'
elif option == 2:
  option_name = 'Latte'
elif option == 3:
  option_name = 'Cappuccino'

print(f'You have selected {option_name}.')

#Check if enough resources to make selected option

if option == 1:
  check_resource(Espresso['coffee'], Espresso['water'], Espresso['milk'])
elif option == 2:
  check_resource(Latte['coffee'], Latte['water'], Latte['milk'])
elif option == 3:
  check_resource(Cappuccino['coffee'], Cappuccino['water'], Cappuccino['milk'])



#Payment Process

# Check transaction success

#Make Coffee

# Turn of coffee machine

#Show Status Report

