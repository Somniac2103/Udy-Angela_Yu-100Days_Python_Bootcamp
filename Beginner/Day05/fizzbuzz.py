#Print 1 to 100
#if div by 3 print Fizz
#if div by 5 print Buzz
#if div by 3 and 5 print FizzBuzz

for number in range(1, 101):
  if number%3 ==0 and number%5 == 0:
    print("FizzBuzz")
  elif number%3 == 0:
    print("Fizz")
  elif number%5 == 0:
    print("Buzz")
  else:
    print(number)
