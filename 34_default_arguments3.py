# Arbitrary arguments
""" *args

def add(a, b):              # Normal way, however it will take only 2 parameter
    return a + b

print(add(1, 2))
"""

"""
def add(*args):            # It will take any argumens as we are using the *args parameter
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))
"""   

"""
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Master", "Felipe", "Demer", "III")
"""

# **kwargs = keyword arguments
"""

def print_address(**kwargs):                    # To print the values of the function
    for value in kwargs.values():
        print(value)


print_address(street="123 Lalo Ka Street", 
              city="San Zula", 
              state="IN", 
              zip="12345")
"""

"""
def print_address(**kwargs):                    # To print the keys of the function
    for key in kwargs.keys():
        print(key)


print_address(street="123 Lalo Ka Street", 
              city="San Zula", 
              state="IN", 
              zip="12345")
"""

"""
def print_address(**kwargs):                    # To print the keys and values of the function
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Lalo Ka Street", 
              city="San Zula", 
              state="IN", 
              zip="12345", 
              apt="100")
"""

# Excercise.  Lets print a shipping label

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr", "Doom", "Malo", "IV",
               street="123 Demonto Street.",
               apt="#250",
               city="Esperanza",
               state="CA",
               zip="65421")
