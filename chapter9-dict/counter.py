hello = 'hello'
d = dict()
for c in hello:
    d[c] = d.get(c, 0) + 1
print(d)
