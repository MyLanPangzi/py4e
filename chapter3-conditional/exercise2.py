# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
# Exercise 2: Rewrite your pay program using try and except
# so that your program handles non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:

try:
    h = float(input('Enter Hours: '))
    r = float(input('Enter Rate: '))
    p = 0
    if h > 40:
        p = 40 * r + (h - 40) * r * 1.5
    else:
        p = h * r
    print(p)
except ArithmeticError:
    print("Error, please enter numeric input")
