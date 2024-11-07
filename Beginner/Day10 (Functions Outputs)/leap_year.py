def is_leap_year(year):
  # div 4 no remainder True 
  if not(year % 4):
    if(year % 100):
      if(year % 400):
        return False  
      return True    
    return True
      
  else:
    return False
  # Return true or false

# input
print(is_leap_year(int(input("What year do you want to check as a leap year?"))))