from art import logo
import os

# Add
def add(num1, num2):
  return num1 + num2
# Subtract
def subtract(num1, num2):
  return num1 - num2
# Multiply
def multiply(num1, num2):
  return num1 * num2
# Divide
def divide(num1, num2):
  return num1 / num2
def exponent(num1, num2):
  return num1 ** num2


# dict
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": exponent,
}



def calculator():
  print(logo)
  calculating = True
  num1 = float(input("What is the first number?: "))
  
  while calculating:
    
    num2 = float(input("What is the second number?: "))
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from above: ")
  
    answer = operations[operation_symbol](num1, num2)
  
    print(f"{num1}{operation_symbol}{num2} = {answer}")
    further_calculation = input(f"Type 'y' to continue calculating with {answer} or 'n' to exit or 'r' to restart: ").lower()
    if further_calculation == 'n':
      calculating = False
      print("Good Bye")
    elif further_calculation == 'y':
      num1 = answer
    elif further_calculation == 'r':
      os.system('cls')
      calculator()
      
    else:     
      if input("Oops! you hit another key. To rerun type 'r' or any key to exit: ") == 'r':
        os.system('cls')
        calculator()
      else:
        calculating = False    
calculator()