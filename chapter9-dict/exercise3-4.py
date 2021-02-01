# Write a program to read through a mail log,
# build a histogram using a dictionary to count
# how many messages have come from each email address, and print the dictionary.
# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and print how many messages the person has.


fin = open('../mbox-short.txt')
r = dict()
for line in fin:
    if not line.startswith('From:'):
        continue
    line = line.rstrip()
    words = line.split()
    if words is None or len(words) < 2:
        continue
    r[words[1]] = r.get(words[1], 0) + 1

print(r)

email = None
tmp = None
for k in r:
    if email is None or r[k] > tmp:
        email = k
        tmp = r[k]
print(email, tmp)
