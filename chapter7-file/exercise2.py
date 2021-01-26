# Exercise 2: Write a program to prompt for a file name,
# and then read through the file and look for lines of the form:
# When you encounter a line
# that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.
# Test your file on the mbox.txt and mbox-short.txt files.

fname = input('enter a file name: ')
try:
    fin = open(fname)
except Exception:
    print("cannot open file ", fname)
    exit()
count = 0
total = 0
for line in fin:
    if line.startswith('X-DSPAM-Confidence:'):
        i = line.find(':')
        f = float(line[i + 1:].strip())
        total = total + f
        count = count + 1

print(count, total / count)
