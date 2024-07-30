height = float(input('Height: '))
weight = float(input('weight: '))

bmi = int(round((weight/height**2),0))

print(f"Your BMI is {bmi}")

if bmi < 18:
  print("Your are under weight.")
elif bmi < 25:
  print("Your are heathly weight.")
elif bmi < 30:
  print("Your are over weight.")
elif bmi < 35:
  print("Your are obese.")
else:
  print("Your are morbidly obese.")
