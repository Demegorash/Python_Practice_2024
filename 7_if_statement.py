# if = do some code only IF some condition is True, else do something else. This is a basic form of making a decision.

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You have not been born yet!")
else:
    print("You must be 18+ to sign up!")
    
# Exercise 2

response = input("Would you like food (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")
    

# Exercise 3

name= input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")
    
# Exercise 4

for_sale = True     # It might be False as well

if for_sale:
    print("This item is for sale!")
else:
    print("This item is NOT for sale!")
    

online = False     # It might be True as well

if online:
    print("The user is online!")
else:
    print("The user is offline!")