""" # 1. Positional and 2. default

def net_price(list_price, discount=0, tax=0.05):           # By giving a value to the parameter, we can only list the variable price in order to get the net_price
    return list_price * (1 - discount) * (1 + tax)


# print(net_price(500))                    # It will return only the price as the list_price only argument
# print(net_price(500, 0.1))               # It will ignore the defautl value from the function second argument and will use the one provided here
# print(net_price(500, 0.1, 0))            # It will ignore the defautl value from the function second and thirg argument and will use the ones provided here

"""
# Exercise, count up timer

import time

def  count(end, start=0):                 # Default arguments must go after the ones are not
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")
    
# count(10)                               # From default value zero to 10 each second
count(30, 15)                             # From 15 to 30 as default value zero was overrided by the 15 added here