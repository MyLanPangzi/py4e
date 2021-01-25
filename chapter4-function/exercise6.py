# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def computepay(hour, rate):
    if hour < 40:
        return hour * rate
    else:
        return 40 * rate + (hour - 40) * rate * 1.5


print(computepay(float(input('Enter Hours: ')), float(input('Enter Rate: '))))
