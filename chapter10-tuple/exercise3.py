# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.


import string
import math

fin = open('../remo-full.txt')
r = dict()
for line in fin:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    for w in line.split():
        for letter in w:
            r[letter] = r.get(letter, 0) + 1

t = list()
t2 = list()
for k, v in r.items():
    t.append((k, v))
    t2.append(v)
t.sort()
total = sum(t2)
for k, v in t:
    print(k, v, (v / total * 100).__round__(2))
