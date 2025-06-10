price1 = 3.14159
price2 = -987.65
price3 =  12.34
price4 =  3000.14159
price5 =  -9870.65
price6 =  1200.34

print(f"Price 1 is ${price1:.2f}") # It will format to 2 decimals :. and f (f for float)
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

print(f"Price 1 is ${price1:10}") # It will complete 10 spaces for the string so we can justify the data to display the output
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

print(f"Price 1 is ${price1:010}") # It will complete witht the number 0 all spaces and will make a 10 lenght for the string so we can justify the data to display the output
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

print(f"Price 1 is ${price1:<10}") # It will letf justify the value
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

print(f"Price 1 is ${price1:>10}") # It will right justify the value
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

print(f"Price 1 is ${price1:^10}") # It will center justify the value
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

print(f"Price 1 is ${price1:+}") # It will show the values are positive 
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

print(f"Price 1 is ${price4:,}") # It will show the values in thousends
print(f"Price 2 is ${price5:,}")
print(f"Price 3 is ${price6:,}")

print(f"Price 1 is ${price4:+,.2f}") # We can mix the previous formatters to and add it to any string as well
print(f"Price 2 is ${price5:+,.2f}")
print(f"Price 3 is ${price6:+,.3f}")