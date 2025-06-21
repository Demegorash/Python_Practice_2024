# fruit = "apple" # Simple String value
# print(fruit)

"""
fruits = ["apple", "orange", "banana", "coconut"] # This is a collecion of values, we use plural as many items are going to be saved on it
print(fruits) # To show all data on the collection
print(fruits[2]) # To show what value element is storage at index 2
print(fruits[0:3]) # Will show value elements from index 0 to 3
print(fruits[0:3:2]) # Will show every 2 values
print(fruits[::-1]) # Will Show all from the end

"""


"""
fruits = ["apple", "orange", "banana", "coconut"]

for fruit in fruits:                     # Will iterate over the list values collection
    print(fruit)
    
"""

"""

fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))                     # Will print a dir of the fruits collection
# print(help(fruits))                    # Will print a description of all the methods we can use wiht the fruits collection
# print(len(fruits))                     # Will show how many elements are on the collection
# print("apple" in fruits)               # Will show if he element is on the collection as a boolean value

"""

"""
fruits = ["apple", "orange", "banana", "coconut"]

# fruits[0] = "pineapple"        # Will add the pineapple value at index zero and will remove the original one for that index
# fruits.append("pineapple")     # Will add the pineapple at the end of the collection list
# fruits.remove("apple")         # Will remove the apple value from the collection list
# fruits.insert(2, "mango")      # Insert a value at the given index
# fruits.sort()                  # Sort will order the list as requested
# fruits.reverse()               # I will make the list reversed
# fruits.clear()                 # Clear will remove all elements from the collection
# print(fruits.index("apple"))   # It will return the index of a value
print(fruits.count("banana"))    # It will count how many values of the same are on the collection

for fruit in fruits:
    print(fruit)
    
"""

# Sets
"""
fruits = {"apple", "orange", "banana", "coconut"}
# print(dir(fruits))                     # Will print a dir of the fruits collection
# print(help(fruits))                    # Will print a description of all the methods we can use wiht the fruits collection
# print(len(fruits))                     # Will show how many elements are on the collection
# print("apple" in fruits)               # Will show if he element is on the collection as a boolean value

# fruits.add("pineapple")                #  We can add a new element to the set
# fruits.remove("coconut")               #  We can remove an element from the set
# fruits.pop()                           # We can pop an element that is fist, however it will be random
# fruits.clear()                           # Clear will remove all elements from the set

print(fruits)
"""

# Tuple

fruits = ("apple", "orange", "banana", "coconut")
# print(dir(fruits))                     # Will print a dir of the fruits collection
# print(help(fruits))                    # Will print a description of all the methods we can use wiht the fruits collection
# print(len(fruits))                     # Will show how many elements are on the collection
# print("apple" in fruits)               # Will show if he element is on the collection as a boolean value

# print(fruits.index("apple"))           #  It will print whaterver is the index of the value we added as string
# print(fruits.count("banana"))          # It will count how many times is the string on the tuple as a value

for fruit in fruits:                     # You can iterate on it
    print(fruit)