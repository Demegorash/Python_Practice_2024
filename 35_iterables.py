# Iterables = An object/collection that can return its elements one at the time, allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5]           # Use a descriptive name so anyone reading the code can understand what are you reffering to. This is a list.
# numbers = (1, 2, 3, 4, 5)             # Tuples are iterable as well

"""
for number in numbers:              # Normal iteration function
    print(number)
    
"""
"""
for number in reversed(numbers):   # Reversed iteration function
    print(number, end=" - ")       # We can close the line with a space instead new line or a dash after so each element will show the space or the dash in between numbers.
"""
"""
fruits = {"apple", "orange", "banana", "coconut"}   # This is a set, sets are not revesable

for fruit in fruits:              # Normal iteration function
    print(fruit)
"""

"""
name = "Albert Demer"             # Normal string

for character in name:
    print(character, end=" ")
"""

my_dictionary = {"A": 1, "B": 2, "C": 3}     # Dictionary

"""
for value in my_dictionary.values():         # Built-in values method in order to show the value for the dictionary, otherwise it will show the key
    print(value) 
"""

for key, value in my_dictionary.items():    # Built-in items method in order to show the value and the key for the dictionary
#    print(key, value)                      # Normal output   
    print(f"{key} = {value}")               # Formated output