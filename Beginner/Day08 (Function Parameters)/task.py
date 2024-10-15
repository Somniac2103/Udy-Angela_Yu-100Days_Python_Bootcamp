def greet(name, location):
  i = 0;
  for i in range(3): 
    print(f"Hello {name}, you are in {location}")
    i+=1

name = input("What is your name? ")
location = input("Where are you now? ")
greet(name = name, location = location)