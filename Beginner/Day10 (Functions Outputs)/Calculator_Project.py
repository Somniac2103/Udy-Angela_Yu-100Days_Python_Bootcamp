# operators = {'+' : "plus", '-' : "minus", '*' : "multiply", '/' : "divide"}
choice = 'n'


def cal(num1, num2, opr):
  if opr == '+':
    return num1+num2
  elif opr == '-':
    return num1-num2
  elif opr == '*':
    return num1*num2
  elif opr == '/':
    return num1/num2

def cont(flag):

while choice == 'n':
  # Intro
  print("Welcome to my calculator")
  choice = "c"
  cont = False
  while choice == 'c':
    # First input
    num1 = if cont == True:
        float(input("Please select your first number? \n"))
    # operator choice
    opr = str(input("Select the operator (+ - * /) \n"))
    # second input
    num2 = float(input("Select the second number? \n"))
    # calculate
    result = float(cal(num1, num2, opr))
    # results
    print(f'{num1} {opr} {num2} is equal to {result}.')
    # continue, new or exit
    choice = ""
    cont = True
    choice = str(input("Would you like to continue (c), start new (n)or exit (enter)? ").lower())
