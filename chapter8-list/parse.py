fin = open('../mbox-short.txt')
for line in fin:
    s = line.strip()
    if s.startswith('From '):
        print(s.split()[2])
