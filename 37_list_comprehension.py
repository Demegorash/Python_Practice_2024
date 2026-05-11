# List comprehension is a better way to create lists in Python [expression for value in iterable if condition]

"""
doubles = []                       # Standard list iteration example with append method
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)
"""

"""
doubles = [x * 2 for x in range(1,11)]    # Using the form:  [expression for value in iterable if condition]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]

print(doubles)
print(triples)
print(squares)
"""

"""
fruits = ["apple", "banana", "coconut", "tomato"]
fruits = [fruit.upper() for fruit in fruits]           # You can delete the fruits list and use ["apple", "banana", "coconut", "tomato"] in the section for fruits inside the expression

print(fruits)
"""

"""
fruits = ["apple", "banana", "coconut", "tomato"]
fruits_chars = [fruit[0] for fruit in fruits]           # Return the fist character on the list

print(fruits_chars)
"""

"""
numbers = [1, -2, 3, -4, 5, -6, -7 , 8]

positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print([positive_nums])
print([negative_nums])
print([even_nums])
print([odd_nums])
"""

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)