
# No function use example, so we need to copy the code 3 times. Also we can use a loop, but we are going to use a function

"""
print("Happy birthday to you!")
print("You are old!")
print("Happy birthday to you!")
print()

print("Happy birthday to you!")
print("You are old!")
print("Happy birthday to you!")
print()

print("Happy birthday to you!")
print("You are old!")
print("Happy birthday to you!")
print()
"""

# Function example to repeat the code 3 times

def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()
    
happy_birthday()
happy_birthday()
happy_birthday()

# Function example to repeat the code with and arguments and make sure to take care of the order on it as it does matter.

def happy_birthday1(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()
    
happy_birthday1("Miniestriposita", 10)
happy_birthday1("Estriposita", 38)
happy_birthday1("Estriposito", 50)

# Another example

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("Demer", 54.35, "02/04")

# Return statement. The return = statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

# Another more complex example

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("feli", "demer")
print(full_name)