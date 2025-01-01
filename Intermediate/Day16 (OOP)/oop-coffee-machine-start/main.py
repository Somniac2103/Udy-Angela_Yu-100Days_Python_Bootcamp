from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#iniatialise
selection = ''
coffeemaker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

# User input

selection = input("Select desired coffee? " + menu.get_items()+"\n")

# Turn off function
if selection == "off":
  print("Switching Off...")
  exit

# Report Print Function
elif selection == "report":
  coffeemaker.report()
  exit

# cash Print Function
elif selection == "money":
  money_machine.report()
  exit

elif menu.find_drink(selection):
  coffee = menu.find_drink(selection)
  if coffeemaker.is_resource_sufficient(coffee):
    money_machine.money_received = money_machine.process_coins()
    if money_machine.make_payment(coffee.cost):
      coffeemaker.make_coffee(coffee)
   
  





    




# Resource Checker Function

# Coin Processor Function

# Transaction checker Function

# Make coffee
