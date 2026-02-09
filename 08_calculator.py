# We are going to build a Python Calculator

operator = input("Enter and operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))            # float to make the user input numbers
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))                              # round to make it round to the next 3 digits
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator! You might need to use only (+ - * /).  Try it again!")      # This will make the user to enter only the operators stated on the function