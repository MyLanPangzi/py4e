d = {'a': 1, 'b': 2}
for k, v in d.items():
    print(k, v)

d = {'a': 10, 'b': 2, 'c': 22}
t = list()
for k, v in d.items():
    t.append((v, k))
t.sort(reverse=True)
print(t)
