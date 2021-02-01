print((0, 1, 2) < (1, 2, 3))
print((1, 2, 3) > (2, 3, 4))

txt = 'but soft what light in yonder window breaks'
t = list()
for w in txt.split():
    t.append((len(w), w))

t.sort(reverse=True)

r = list()
for length, w in t:
    r.append(w)

print(r)
