# Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average as an integer.

import re

fin = open('../mbox.txt')
count = 0
total = 0
for line in fin:
    line = line.rstrip()
    t = re.findall('^New Revision: (\d+)', line)
    if len(t) > 0:
        count += 1
        total += float(t[0])

print(total / count)
