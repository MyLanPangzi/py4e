d = dict()
print(d)
d['hello'] = 'world'
print(d)
d = {'lake': 'hudi'}
print(d)
print(d['lake'])
# print(d['no'])
print(len(d))
print('lake' in d)
print('no' in d)
print(d.values())
for v in list(d.values()):
    print(v)
