# Exercise 1: Write a program which repeatedly reads numbers
# until the user enters done. Once done is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and skip to the next number.


count = 0
total = 0
while True:
    s = input("enter a num: ")
    if s == 'done':
        break
    try:
        num = float(s)
        count = count + 1
        total = total + num
    except Exception:
        print("please enter a num")
print(total, count, total / count)
