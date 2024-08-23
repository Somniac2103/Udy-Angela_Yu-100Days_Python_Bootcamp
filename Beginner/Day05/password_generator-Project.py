import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = "" 

while nr_letters > 0 or nr_numbers > 0 or nr_symbols > 0:
  selector = random.randint(1, 3)
  if selector == 1:
    if nr_letters > 0:
      password += random.choice(letters)
      nr_letters -= 1
  elif selector == 2:
    if nr_symbols > 0:
      password += random.choice(symbols)
      nr_symbols -= 1
  elif selector == 3:
    if nr_numbers >0:
      password += random.choice(numbers)
      nr_numbers -= 1

print(password)


