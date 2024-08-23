print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice = (input("You'r at a cross road. Where do you want to go left or right?\n").capitalize())

if choice == "Right":
  print("Game Over.")
elif choice == "Left":
  choice = (input("You'r arrive at a river. Do you wait or do you swim across?\n")).capitalize()
  if choice == "Swim":
    print("Game Over.")
  elif choice == "Wait":
    choice = (input("You'r arrive at 3 doors which is colored blue, red and yellow. Which door do you open?\n")).capitalize()
    if choice == "Blue" or choice == "Red":
      print("Game Over.")
    elif choice == "Yellow":
      print("You Win")
    else:
      print("Invalid input")
      choice = (input("You'r arrive at 3 doors which is colored blue, red and yellow. Which door do you open?\n")).capitalize()
  else:
    print("Invalid input")
    choice = (input("You'r arrive at a river. Do you wait or do you swim across?\n")).capitalize()
else:
  print("Invalid input")
  choice = (input("You'r at a cross road. Where do you want to go left or right?\n").capitalize())
  
    #Which door?
      #Red = dead
      #Blue = dead
      #Yellow = win

