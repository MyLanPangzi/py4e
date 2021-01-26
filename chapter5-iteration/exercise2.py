# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead of the average.

maximum = None
minimum = None
while True:
    s = input("enter a num: ")
    if s == "done":
        break
    try:
        num = float(s)
        if minimum is None or minimum > num:
            minimum = num
        if maximum is None or maximum < num:
            maximum = num
    except Exception:
        print("please enter a num")
print(maximum, minimum)
