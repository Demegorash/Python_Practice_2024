import random

# print(help(random))                 # It will show the random mode information to better understand how to use it

low = 1
high = 100

number = random.randint(low, high)    # It will generate a random variable in between the variables provided
print(number)

number1 = random.randint(1, 20)       # It will generate a random # in between the paramethers provided
print(number1)

number2 = random.random()              # It will show a random floating number between 0 and 1
print(number2)     

options = ("rock", "paper", "scissors")   
option = random.choice(options)        # It will show a random key from a list
print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "As"]
random.shuffle(cards)                  # It will random shuffle a list
print(cards)