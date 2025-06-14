

for x in range(1, 11):   # Normal loop
    print(x)

for backcounter in reversed(range(1, 11)):  # Reverse counter
    print(backcounter)

print("Happy New Year!!!")

for y in range(1, 11, 2):   # Count by 2 adding the , and the #2
    print(y)
    
credit_card = "1234-5678-9012-3456"   # Iterate over a string
for z in credit_card:
    print(z)
    
for b in range(1, 21):   # Skip a value with conditionals using the continue keyword
    if b == 13:
        continue
    else:
        print(b)

for c in range(1, 21):   # If it touch the equalized value, the program will end
    if c == 13:
        break
    else:
        print(c)