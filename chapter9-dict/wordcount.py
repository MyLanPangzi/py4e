name = input('enter a file name')
try:
    fin = open(name)
except:
    print('file cannot open ', name)
    exit()

r = dict()

for line in fin:
    line = line.rstrip()
    for w in line.split():
        r[w] = r.get(w, 0) + 1
print(r)