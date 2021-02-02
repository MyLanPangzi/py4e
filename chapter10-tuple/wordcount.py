import string

fin = open('../remo-full.txt')
r = dict()
for line in fin:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    for w in line.split():
        r[w] = r.get(w, 0) + 1

t = list()
for k, v in r.items():
    t.append((v, k))

t.sort(reverse=True)

print(t[:10])
