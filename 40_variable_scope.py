# variable scope

"""
def func1():            # scope only on the function, the other function cannot see inside it or know what is on the other function
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()
"""

"""
def func1():            # Local version of x at each function
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()
"""

"""
def func1():            # Enclosed version of x at each function
    x = 1

    def func2():
        print(x)
    func2()
    
func1()
"""

"""
def func1():            # Global version of x 
    print(x)

def func2():
    print(x)
    
x = 3

func1()
func2()
"""

from math import e

def func1():            # Built-in version of x 
    print(e)

# e = 3                  # This will create a different e version from the imported from math module

func1()
