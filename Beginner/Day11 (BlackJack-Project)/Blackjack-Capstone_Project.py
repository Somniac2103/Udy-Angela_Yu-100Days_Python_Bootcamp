# Blackjack Capstone Project

#-----imports-----
import random 

#-----Variables-----
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

player_choice = 'h'
computer_choice = True

player_lose = False
computer_lose = False

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
  print(f'Your cards: {player_cards}')
  player_total = sum(player_cards)
  print(f'Your total is {player_total}')
# computer dealt cards
  for i in range(2):
    computer_cards.append(cards[random.randint(0,12)])
  print(f'Computer cards: {computer_cards[0]}') 
  computer_total = sum(computer_cards)

#-----Options------
#Player Options
  while player_choice == 'h':
    player_choice = str(input("Hit (h) or stay (s)?\n").lower())

    # hit option
    if player_choice == 'h':
      player_cards.append(cards[random.randint(0,12)])
      print(f'Your cards: {player_cards}')
      player_total = sum(player_cards)
      print(f'Your total is {player_total}')
      if player_total > 21:
        player_choice = 's'
        player_lose = True

#Computer Options
  while computer_choice == True:
    computer_cards.append(cards[random.randint(0,12)])
    computer_total = sum(computer_cards)
    print(f'Computer cards: {computer_cards}')
    print(f'The computer total is {computer_total}')
    if computer_total > 18:
        computer_choice = False
    elif computer_total > 21:
        computer_lose = True
       
#Results
  print(f'Your cards: {player_cards}\n Your total is {player_total}')
  print(f'Computer cards: {computer_cards}\n Computer total is {computer_total}')
  if player_total > computer_total and player_total < 22 or computer_lose == True:
    print('You win!')
  elif player_total < computer_total and computer_total < 22 or player_lose == True:
    print('You lose')
  else: print('It is a draw')
#Continue

