# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.


fin = open('../mbox-short.txt')
r = dict()
for line in fin:
    if not line.startswith('From:'): continue
    words = line.split()
    if words is None or len(words) < 2: continue
    hostname = words[1].split('@')[1]
    r[hostname] = r.get(hostname, 0) + 1
print(r)

