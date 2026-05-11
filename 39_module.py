# print(help("modules"))       # This will show the available modules as reference

# print(help("math"))          # This will show the math module help and examples as reference

import math                    # Regular way to import
print(math.pi)

# import math as m             # You can get the module as an alias
# print(m.pi)

from math import pi            # You can import something specific from a module, not recomended as it can cause variables mix issues due to names
print(pi)

# We can create a personal module, in another file name as example.py, then we can download in a main as well by calling it as import example that will be our personalized module.

