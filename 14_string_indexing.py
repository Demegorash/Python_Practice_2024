credit_number = "1234-5678-9012-3456"

# print(credit_number[4])   # If the data is only one, it means it will take and show the one added on the []
# print(credit_number[:4])  # It will show the data from index 0 to index 4
# print(credit_number[5:9]) # It will show the data from index 5 to 0
# print(credit_number[5:])  # It will show all data after the index 5
# print(credit_number[-1])  # It will start to show from the end of the string
# print(credit_number[::2]) # It will show every 2 charactes on the screen end step

# Practical excercise 1:  Lets show the last 4 digits of a card number.

last_digits= credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Practical excercise 2:  Lets work by reversing the card number

credit_number = credit_number[::-1]
print(credit_number)