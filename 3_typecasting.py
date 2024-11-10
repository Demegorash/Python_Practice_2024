# Typecasting =  The process of converting a Variable from one data type to another for example str(), int(), float(), bool()

name = "Felipe Demer"
age = 46
gpa = 3.2
is_student = True

print(type(name))            # It returns <class 'str'>
print(type(age))             # It returns <class 'int'>
print(type(gpa))             # It returns <class 'float'>
print(type(is_student))      # It returns <class 'bool'>

# We can assign a new type by doing as follows:

gpa = int(gpa)
age = float(age)
age = str(age)
name = bool(name)

print(gpa)                   # It returns 3
print(age)                   # It returns 46.0
print(type(age))             # It returns <class 'str'>
print(name)                  # It returns True