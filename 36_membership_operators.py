# in  

word = "APPLE"

"""
letter = input("Guess a letter in the secret word: ")  # String

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")
"""

"""
students = {"Charles","Xavier","Logan"}            # Set

student = input("Enter the name of the student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")
"""

"""
grades = {"Magneto": "A",            # Dictionary
          "Jean": "B",
          "Beast": "C",
          "Logan": "D"}  

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student} grade is {grades[student]}")
else:
    print(f"{student} was not found")
"""

email = "demer@demer.com"                 # Simple paramethers validation

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

# not in

"""
letter = input("Guess a letter in the secret word: ")  # String

if letter not in word:
    print(f"{letter} was not found") 
else:
    print(f"There is a {letter}")
"""

"""
students = {"Charles","Xavier","Logan"}                # Set

student = input("Enter the name of the student: ")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")
"""
