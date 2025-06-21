
capitals =  {"USA": "Washington D.C",
             "India": "New Delhi",
             "China": "Beijing",
             "Russia": "Moscow"}

# print(dir(capitals))                   # It will show all attributes and methods related to the dictionarie
# print(help(capitals))                  # It will show all help related to the dictionarie

# print(capitals.get("USA"))             # It will show the value related to the USA key


""" # If we enter non valid key
if capitals.get("Japan"):
    print("The capital is on the list")
else:
    print("The capital related to this country is not part of this list.")
"""

# capitals.update({"Germany": "Berlin"})  # It will insert a new key:value pair to the dictionarie
# capitals.pop("India")                   # It will remove a key:value pair from the dictionarie
# capitals.popitem()                      # It will remove the last key:value pair from the dictionarie
# capitals.clear()                        # It will clear the dictionarie

# print(capitals)

# To gey the key for the dictionarie
# keys = capitals.keys()                  # It will return all the keys we have in our dictionarie

# print(keys)

"""
for key in capitals.keys():               # The keys method is iterable
    print(key)
"""

# To get the values for our dictionarie

# values = capitals.values()                # It will return all the value we have in our dictionarie
# print(values)

"""
for value in capitals.values():           # The values method is iterable
    print(value)
"""

# To get the items for our dictionarie

items = capitals.items()                   # It will return all the items we have in our dictionarie
# print(items)

for key, value in capitals.items():        # The items method is iterable
    print(f"{key}: {value}")