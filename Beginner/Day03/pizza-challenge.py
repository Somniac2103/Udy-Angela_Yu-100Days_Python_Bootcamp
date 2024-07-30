print("Thank you for choosing Python Pizza Deliveries")
size = input("What size pizza do you want? [S,M,L] ")
addPepperoni = input("Would you like pepperoni with your pizza? [Y,N] ")
extraCheese = input("Would you like extra cheese with your pizza? [Y,N] ")
bill = 0

#pizza size
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

#add pepperoni
if addPepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

#add cheese
if extraCheese == "Y":
  bill += 1

#final total
print(f'Your bill is : ${bill}')