from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#iniatialise
coffee = MenuItem(" ", 0, 0, 0, 0)
coffeemaker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

# User input

coffee.name = input("Select desired coffee? " + menu.get_items()+"\n")

# Turn off function
if coffee.name == "off":
  print("Switching Off...")
  exit

# Report Print Function
elif coffee.name == "report":
  coffeemaker.report()
  exit

if menu.find_drink(coffee.name):
  print("Coffee Option available")
  





    




# Resource Checker Function

# Coin Processor Function

# Transaction checker Function

# Make coffee
