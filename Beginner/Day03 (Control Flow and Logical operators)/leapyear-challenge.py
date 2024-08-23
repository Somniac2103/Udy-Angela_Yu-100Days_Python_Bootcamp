year = int(input("Year: "))

# dividable by 4 without remainder then true
if year%4 == 0:
  #unless dividable by 100 with no remainder
  if year%100 == 0:
    #unless divivable by 400 with no remainder
    if year%400 == 0:
      print(f"{year} is a leapyear")   
    else:
      print(f"{year} is not a leapyear")    
  else:    
    print(f"{year} is a leapyear")    
else:
  print(f"{year} is not a leapyear")


