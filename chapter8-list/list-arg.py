def del_header(t):
    del t[0]


def tail(t):
    return t[1:]


arr = [1, 2, 3]
del_header(arr)
print(arr)

print(tail(arr))
print(arr)
