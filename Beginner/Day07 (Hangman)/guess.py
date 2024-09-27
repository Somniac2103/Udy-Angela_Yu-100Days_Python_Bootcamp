import random

word_lists = ["aardvark", "baboon", "camel"]

#Initialize
secretword = random.choice(word_lists)
print (secretword)
displayword = ""

for letter in range(len(secretword)):
  displayword += "_"
print("\n")

while displayword != secretword:
  print(displayword)
  guess = str(input("Guess a letter? ")).lower()

  #user input
  for letter in range(len(secretword)):
    if guess == secretword[letter]:
      displayword[letter] = secretword[letter]
    elif displayword[letter] != "_":
      continue
    else:
      displayword[1] = "_"