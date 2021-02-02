# Exercise 1: Revise a previous program as follows:
# Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
#
# After all the data has been read,
# print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

fin = open('../mbox-short.txt')
r = dict()
for line in fin:
    if not line.startswith('From '):
        continue
    words = line.split()
    if words is None or len(words) < 2:
        continue
    r[words[1]] = r.get(words[1], 0) + 1

t = list()
for k, v in r.items():
    t.append((v, k))
t.sort(reverse=True)
print(t[0])
