def calculate():
  operation = input(
  '''
  Please type in the math operation you would like to complete:
  + for addition
  - for subtraction
  * for multiplication
  / for division
  % for modulus

''')

  if operation == '+':
    print("""
      Please input an integer
    """)
    number1 = int(input("Enter your first number: "))
    number2= int(input("Enter your second number: "))
    add= int(number1 + number2)
    print(f"{number1} + {number2} = {add}")
    

  elif operation =="-":
    print("""
      Please input an integer
    """)
    number1 = int(input("Enter your first number: "))
    number2= int(input("Enter your second number: "))
    sub =int(number1 - number2)
    print(f"{number1} - {number2} = {sub}")
    
    
  elif operation =="*":
    print("""
      Please input an integer
    """)
    number1 = int(input("Enter your first number: "))
    number2= int(input("Enter your second number: "))
    ans = int(number1 * number2)
    print(f"{number1} * {number2} = {ans}")
    
    
  elif operation =="/":
    print("""
      Please input an integer
    """)
    number1 = int(input("Enter your first number: "))
    number2= int(input("Enter your second number: "))
    ans= int(number1 / number2)
    print(f"{number1} / {number2} = {ans} ")
   
  
  elif operation =="%":
    print("""
      Please input an integer
    """)
    number1 = int(input("Enter your first number: "))
    number2= int(input("Enter your second number: "))
    mod = int(number1 % number2)
    print(f"{number1} % {number2} = {mod}")
    
  
  else:
    print("You have not typed a valid operator, please run the program again")
  

def again():
  calc_again = input(
  '''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
  '''
  
)
    
  if calc_again.upper() == 'Y':
    welcome()
    calculate()

  elif calc_again.upper() == 'N':
    print("""
    Thanks For Using My Calculator.
    See you Later!
    """)

  else:
    again()

def welcome():
  print(
    """
    ******************

    Welcome to Abdullahi's Calculator

    ******************
    """
  )

welcome()
calculate()
again()