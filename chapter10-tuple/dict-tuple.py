d = {'hello': 1, 'world': 2}
print(d.items())
t = list(d.items())
for i in t:
    print(i)
d = {'b': 1, 'c': 2, 'a': 3}
t = list(d.items())
t.sort()
print(t)
