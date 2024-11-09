# Variable =  A container for a value (string, integer, float, boolean).
# A Variable behaves as if it was a value it contains.

first_name = "Felipe" # This in between "" is named a string.  A string is a series of characters.
food = "Pizza"
email = "demer@demer.com"
age = 46              # This is a integer type of data and it should not to be inside ""
price = 10.99         # This is a float type of data at it has decimals
is_student = True     # This is a boolean type of data, meaning True or False (for logic programs this is really important)

print(first_name) # Just printing the variable.

# We can use an f string with a placeholder {f"variable_here"}
print(f"Hi, my real name is {first_name}.")
print(f"I do really like {food}!")
print(f"My fake email in order to show this concept for you is: {email}!")
print(f"I am {age} years old.")
print(f"Next to my house, the pizza price I like is ${price}.")
print(f"Are you a Python student?: {is_student}.")