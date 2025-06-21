import random

# We are going to use unicode for this program  ● ┌ ─ ┐ │ └ ┘ in order to do some ascii art for this dice roller program
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") # Unicode ● ┌ ─ ┐ │ └ ┘

""" Dice diagram

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

"""

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│         │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│    ●    │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):                 # To create the random value depending of how many dies have the player choosen
    dice.append(random.randint(1, 6))
    
"""
for die in range(num_of_dice):                 # To show the dice_art on screen vertical
    for line in dice_art.get(dice[die]):
        print(line)
"""

for line in range(5):                          # To show the dice_art on screen horizontal
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()
    
for die in dice:                               # To have the total for the chosen die and computer generated value
    total += die
print(f"total: {total}")