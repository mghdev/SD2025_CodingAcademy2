# We are going to write an interactive calculator program using if-statements and the 'main loop' pattern from the while-loop exercises
# We will discuss the design of this program in class. I will show a working version as a reference for what it should do.

def main():
    #=======================
    # TODO
    # Establish a main loop
    # Implement subtraction -, multiplication * or x, division /, help h, quit q, clear c  (+ is already implemented below)
    # Bonus: implement extra operations of your choice. Perhaps try to use some functions from your geometry modules?
    
    number = 0.0
    print("Current number:",number)
    operation = input("What operation would you like to do? (h for help)")
    if operation == "+":
        operand = float(input("How much would you like to add? "))
        number += operand
    
    #=======================
    

if __name__ == "__main__":
    main()