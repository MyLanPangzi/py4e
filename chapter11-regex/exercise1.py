# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

import re

reg = input('enter a regex')
fin = open('../mbox.txt')
count = 0
for line in fin:
    if re.search(reg, line):
        count += 1
print('find ', count, 'lines')
