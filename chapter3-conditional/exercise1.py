# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
h = float(input('Enter Hours: '))
r = float(input('Enter Rate: '))
p = 0
if h > 40:
    p = 40 * r + (h - 40) * r * 1.5
else:
    p = h * r

print(p)
