import re

fin = open('../mbox-short.txt')
for line in fin:
    line = line.rstrip()
    t = re.findall('^From .* (\d\d):', line)
    if len(t) > 0:
        print(t)
