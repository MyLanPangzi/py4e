import re

fin = open('../mbox-short.txt')
for line in fin:
    line = line.rstrip()
    t = re.findall('^X\S.+: ([\d.]+)', line)
    if len(t) > 0:
        print(t)
