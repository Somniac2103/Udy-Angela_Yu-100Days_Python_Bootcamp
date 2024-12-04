# import
import random

# initialize
replay = 'y'


while replay == 'y':
  # reset
  mode = ''
  flag = False
  guesses = 10
  outcome = ""

  # Intro
  print("Welcome to the Number Guessing Game.\n")

  while flag == False:
    mode = str(input("Select your difficulty level Easy(10 chances) or Hard(5 chances)? E / H\n")).lower()
    if mode == 'e' or mode =='h':
      flag = True
    else:
      print("Invalid choice, try again")
  if mode == 'e':
    guesses = 10
  else:
    guesses = 5

  # Computer Generate Number
  computer_number = int(random.randint(0,100))

  # Player Guess
  while (outcome != 'same') and (guesses > 1):
    player_guess = int(input(f'Attempt to guess the seccret number.\nThe number is between 1 to and 100.\nYou have {guesses} guesses left.\n'))

    #Compare
    if player_guess == computer_number:
      outcome = "same"
    elif player_guess > computer_number:
      outcome = "higher"
      print("Your guess is higher than the secret number.")
      guesses -= 1
    elif player_guess < computer_number:
      outcome = "lower"
      print("Your guess is lower than the secret number.")
      guesses -= 1 

  #Results
  if outcome == 'same' and guesses > 0:
    print("You are a Winning!")
  else:
    print("Sorry, you lost.")

  #Outro
  replay = str(input("Would you like to play again? y/n\n")).lower()
