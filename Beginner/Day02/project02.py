print("Weelcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("How much tip woild you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

print(f"Each person should pay: ${(round(((bill * (1 + tip/100))/people), 2))}")
