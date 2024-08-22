import random

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

PLAYER_WINS = "Player Wins!"
COMPUTER_WINS = "Computer Wins!"

#get player input
player_choice = (input(f"\nSelect:\n-------\n{ROCK}\n{PAPER}\n{SCISSORS}\n\nSelection: ")).capitalize()
while (player_choice != ROCK and player_choice != PAPER and player_choice != SCISSORS):
  print("Invalid input, please try again:")
  player_choice = (input(f"\nSelect:\n-------\n{ROCK}\n{PAPER}\n{SCISSORS}\n\nSelection: ")).capitalize()

#get computer input
computer_choice = random.choice([ROCK,SCISSORS,PAPER])

#compare
if (computer_choice == player_choice):
  outcome = "It's a Draw"
elif (computer_choice == ROCK and player_choice == PAPER):
  outcome = PLAYER_WINS
elif (computer_choice == ROCK and player_choice == SCISSORS):
  outcome = COMPUTER_WINS
elif (computer_choice == PAPER and player_choice == ROCK):
  outcome = COMPUTER_WINS
elif (computer_choice == PAPER and player_choice == SCISSORS):
  outcome = PLAYER_WINS
elif (computer_choice == SCISSORS and player_choice == ROCK):
  outcome = PLAYER_WINS
elif (computer_choice == SCISSORS and player_choice == PAPER):
  outcome = COMPUTER_WINS
else:
  print("Unexpected Error has occurred")

#results
print( f'\nPlayer selected {player_choice}.')
print( f'\nComputer selected {computer_choice}.')
print( f'\n{outcome}')
