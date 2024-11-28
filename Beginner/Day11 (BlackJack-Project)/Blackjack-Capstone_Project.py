# Blackjack Capstone Project

#-----imports-----
import random 

#-----Variables-----
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

player_choice = 'h'

#-----functions-----

# def deal_card():
  

#-----Welcoming-----
print("Welcome to Barry's Blackjack Table")

#-----Deal-----
game_choice = str(input("Do you wish to play? y/n \n")).lower()
# player dealt cards
if game_choice == 'y':
  for i in range(2):
    player_cards.append(cards[random.randint(0,12)])
  print(player_cards)
# computer dealt cards
  for i in range(2):
    computer_cards.append(cards[random.randint(0,12)])
  print(computer_cards[0]) 

#-----Options------
#Player Options
while player_choice == 'h':
  player_choice = str(input("Hit (h) or stay (s)?\n").lower())

  # hit option
  if player_choice == 'h':
    player_cards.append(cards[random.randint(0,12)])
    print(player_cards)

#Computer Options

#Results

#Continue

