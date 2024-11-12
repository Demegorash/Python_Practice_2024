# We are going to check some arithmetic and math code in Python.  Please remove the comment in order to turn on the excercise to check.

# Addition and substraction
# friends = 0

# friends = friends + 1          # Increase by 1
# friends += 1                     # Increase by 1 augmented
# friends = friends - 2          
# friends -= 2

# print(friends)

# Multiplication and division
# friends2 = 5

# friends2 = friends2 * 3         
# friends2 *= 3
# friends2 = friends2 / 2
# friends2 /= 2

# print(friends2)

# Exponents and modulus

# friends3 = 5

# friends3 = friends3 ** 2
# friends3 **= 2

#reminder = friends3 % 3

# print(friends3)
# print(reminder)

# Built in math functions in Python

x = 3.14
y = -4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(4, 3)       # The data to the power of meaning 4 to the power of 3
# result = max(x, y, z)
# result = min(x, y, z)

# print(result)

# Now we are going to work with the math module from Python by doing

# import math

# print(math.pi)
# print(math.e)

# a = 9
# b = -16
# c = 27.3

# result = math.sqrt(a)
# result = math.ceil(c)

# print(result)

# Excercise, we are going to calculate the circumference and area of a circle.

import math

radius  = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is: {round(circumference, 2)}cm")
print(f"The area of the circle is: {round(area, 2)}cm^2")


# Lets try to calculate the hypothenuse of a triangle c = a^2 + b^2 all under raiz cuadrada

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")