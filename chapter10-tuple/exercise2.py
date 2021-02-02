# Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by finding the time string and then splitting
# that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

fin = open('../mbox.txt')
r = dict()
for line in fin:
    if not line.startswith('From '):
        continue
    words = line.split()
    if words is None or len(words) < 6:
        continue
    h = words[5].split(':')[0]
    r[h] = r.get(h, 0) + 1

t = list()
for k, v in r.items():
    t.append((k, v))

t.sort()
# t.sort(reverse=True)

for k, v in t:
    print(k, v)
