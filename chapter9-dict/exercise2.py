# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).
fin = open('../mbox-short.txt')
r = dict()
for l in fin:
    if not l.startswith('From'):
        continue
    words = l.split()
    if words is None or len(words) < 3:
        continue
    r[words[2]] = r.get(words[2], 0) + 1

print(r)
