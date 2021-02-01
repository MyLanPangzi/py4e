import string

print(string.punctuation)

fname = input('enter a file name')
try:
    fin = open(fname)
except:
    print('cannot opne file ', fname)
    exit()

r = dict()
for l in fin:
    l = l.rstrip()
    l = l.translate(l.maketrans('', '', string.punctuation))
    l = l.lower()
    for w in l.split():
        r[w] = r.get(w, 0) + 1

print(r)
