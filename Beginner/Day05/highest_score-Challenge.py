#database
student_scores = [150, 142, 156]

#variables
highest_score = 0

#find highest score
for score in student_scores:
  if score > highest_score:
    highest_score = score
  

#display highest score
print(f"The highest score is {highest_score}.")