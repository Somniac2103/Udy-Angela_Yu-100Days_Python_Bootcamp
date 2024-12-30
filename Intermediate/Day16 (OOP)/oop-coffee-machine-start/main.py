from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#iniatialise
machine = CoffeeMaker()
available_Coffee = Menu()

# User input
while True:
  selected_coffee = input("Select desired coffee? " + available_Coffee.get_items()+"\n")

  # Turn off function
  if selected_coffee == "off":
    print("Switching Off...")
    exit

  # Report Print Function
  elif selected_coffee == "report":
    machine.report()

  elif available_Coffee.find_drink(selected_coffee) == False:
      continue
  else:
      print("nuts")
  
    




# Resource Checker Function

# Coin Processor Function

# Transaction checker Function

# Make coffee
