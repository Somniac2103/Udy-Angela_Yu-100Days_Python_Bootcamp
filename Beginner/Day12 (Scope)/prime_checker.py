import math

def is_prime(num):
  if num > 1:
    for i in range(2, math.ceil((num/2)+1)):
    
      if (num%i) == 0:
        return True
      else:
        return False
      
num = int(input("Enter number to check for Prime? "))
if is_prime(num) == True:
  print(f'{num} is not prime')
else: 
  print(f'{num} is prime')