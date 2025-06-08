# You can remove one comment for each example in order to run the required method

# Variable name and result examples

# name = input("Enter your full name: ")

# result = len(name) # It will show the length of the string
# print(result)

# result = name.find("F") # It will find the first occurrence on the find 
# print(result)

# result = name.rfind("q") #  It will find the last occurence on the find
# print(result)

# name = name.capitalize() # We can capitalize the first letter of the string
# print(name)

# name = name.upper() # All the letters on the string are going to be capitalized
# print(name)

# name = name.lower() # All the letters on the string are going to be lower cased
# print(name)

# result = name.isdigit() # Will return a boolean value, true or false depending of the input
# print(result)

# result = name.isalpha() # Will return a boolean value, true or false depending of the input is only alphabetic characters
# print(result)

# Variable phone_number

# phone_number = input("Enter your phone number: ")

# result = phone_number.count("-") # It will count how many characters are the same as the entered as request to check
# print(result)

# phone_number = phone_number.replace("-", " ") # Replace method can replace any character with another from the provided after the comma
# print(phone_number)

# In order to get list of methods you can do:
# print(help(str))

"""
Exercise: Validate user imput

1. username is no more than 12 characters
2. username must not contain spaces
3. username must not containt digits

"""

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain numbers")
else:
    print(f"Welcome {username}")