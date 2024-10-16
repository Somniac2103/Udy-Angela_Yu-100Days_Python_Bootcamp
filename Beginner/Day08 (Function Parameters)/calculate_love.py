def calculate_love_score(name1, name2):
  combinename= name1 + name2
  true_score = 0
  love_score = 0
  for letter in combinename:
    for true_letter in "true": 
      if true_letter == letter:
        true_score += 1
    for love_letter in "love":
      if love_letter == letter:
        love_score += 1
  truelove_score = str(true_score) + str(love_score)
  print(f"Your True Love score is {truelove_score}")    


name1 = input("What is your name? ")
name2 = input("What is your partner's name? ")

calculate_love_score(name1,name2)