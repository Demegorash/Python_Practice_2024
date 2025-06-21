# With variables on the lists names

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries)          # It will return the whole lists inside the groceries list
print(groceries[0])       # It will return a row
print(groceries[1][2])    # It will return the list at index 1 and the element at index 2 on that list


# On this example, it will show how to create a list as well without the variable declaration

groceries1 = [["strawberry", "lima", "melon", "coco"],
              ["tomato", "lettuce", "potatoes"],
              ["pork", "cow", "duck"]]

# print(groceries1)          # It will return the whole lists inside the groceries list
# print(groceries1[0])       # It will return a row
# print(groceries1[1][2])    # It will return the list at index 1 and the element at index 2 on that list

for collection in groceries1:        # We can use a for loop as well in order to print what is needed
    print(collection)
    
for collection in groceries1:        # We can use a for loop in order to iterate on the list
    for food in collection:
        print(food, end=" ")         # It will make the printing on a single line, then with the next print, we can have a new line so we can see it better and ordered
    print()
    
""" # Tuples single
groceries1 = [("strawberry", "lima", "melon", "coco"),
              ("tomato", "lettuce", "potatoes"),
              ("pork", "cow", "duck")]
"""

""" # 2D Tuples = Is a tuple made off of tuples
groceries1 = (("strawberry", "lima", "melon", "coco"),
              ("tomato", "lettuce", "potatoes"),
              ("pork", "cow", "duck"))
"""

""" # Tuple made of sets
groceries1 = ({"strawberry", "lima", "melon", "coco"},
              {"tomato", "lettuce", "potatoes"},
              {"pork", "cow", "duck"})
"""

# Exercice: 2D Keypad as the one found on a phone

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()