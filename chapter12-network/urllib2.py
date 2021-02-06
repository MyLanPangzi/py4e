import urllib.request as req

txt = req.urlopen('http://data.pr4e.org/romeo.txt')
r = dict()
for line in txt:
    line = line.decode().strip()
    for w in line.split():
        r[w] = r.get(w, 0) + 1

print(r)