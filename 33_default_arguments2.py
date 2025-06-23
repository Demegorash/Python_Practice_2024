# 3. Keyword. Adding the keywords, we can enter the information on any order and the function will return the correct order. Positional arguments follows keyword arguments, so the Hello cannot be at the end.

"""
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")
    
hello("Hello", last="Raphael", first="Ninja", title="Mr.")

"""                                                     

"""                                                           
for x in range(1, 11):                                  # Another example
    print(x, end=" ")
print()

"""

"""    
print("1", "2", "3", "5", "6", sep="-")                 # Anoter example, separate number with dash

"""

# Exercise

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=506, area=123, first=456, last=789)
print(phone_num)