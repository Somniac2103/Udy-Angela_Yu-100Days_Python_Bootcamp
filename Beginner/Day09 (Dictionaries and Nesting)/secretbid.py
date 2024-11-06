#declarations
bidders = {}
next_user = 'y'
highest_bid = 0

# repeat
while next_user == 'y':
  #clear screen
  print("\n" * 100)
  # inputs
  name = str(input("What is your name: "))
  bid = int(input("What is your bid: $"))
  #database update
  bidders[name] = bid 
  #more inputs
  next_user = input("Add another bid: Y/N?\n").lower()
  
#compare bids
for user in bidders:
  if bidders[user] > highest_bid:
    highest_bid = bidders[user]
    winner = user

# output
print('\n' * 100)
print(f'The auction winner is {winner} at a bid of ${highest_bid}')

