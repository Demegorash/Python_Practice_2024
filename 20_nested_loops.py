
"""  Basic theory explanation

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()
    
"""
# Example proyect, lets create a form.

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()


