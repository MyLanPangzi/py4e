import  re

fin = open('../mbox-short.txt')
for l in fin:
    l = l.rstrip()
    if re.search('From:',l):
        print(l)
