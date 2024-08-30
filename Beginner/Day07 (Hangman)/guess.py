import random

word_lists = ["aardvark", "baboon", "camel"]

# TODO 1 - Randomnly select word from list and print

secretword = random.choice(word_lists)
print (secretword)

# TODO 2 - Ask user to guess number

guess = str(input("Guess a letter?\n")).lower()
# print(guess)

# TODO 3 - Check letter with each letter in word and return "Right" or "Wrong"

for letter in range(len(secretword)):
  if guess == secretword[letter]:
    print("Right")
  else:
    print("Wrong")