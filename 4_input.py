# input() = A function that prompts the user to enter data.  It returns the entered data as a string.

name = input("What is your name?: ")    # At the terminal, it shows you to enter the information required.
age = int(input("How old are you?: "))  # We make the age and int data type because the input makes it a string.
                      
age = age + 1

print(f"Hello {name}!")
print("Happy Brithday!")
print(f"You are {age} years old!")

# Exercise 1 rectagle Area Calculation

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The Area for this rectangle is: {area} cm squared!")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price for the item you purchased?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}.")