# Exercise 1: Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

s = "hello world"
length = len(s) - 1
while length > 0:
    print(s[length])
    length = length - 1
