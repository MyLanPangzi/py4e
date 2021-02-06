import re

fin = open('../mbox-short.txt')
for line in fin:
    line = line.rstrip()
    t = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(t) > 0:
        print(t)
