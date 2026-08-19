
"""
def main():
    # Your program goes here

if __name__ == '__main__':                        # dunder name or dunder main means double underscore
    main()             
    
"""

# This is an example, we need to create 2 scripts, so we can call each one depending of the request.

def favorite_food(food):
    print(f"Your favorite food is {food}")
    
def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")
    

if __name__ == '__main__':
    main()