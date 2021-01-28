# Exercise 1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None.
# Then write a function called middle that takes a list
# and returns a new list that contains all but the first and last elements.


def chop(t):
    t.pop()
    t.pop(0)


def middle(t):
    return t[1:len(t) - 1]


arr = [0, 1, 2, 3]
chop(arr)
print(arr)

arr = [0, 1, 2, 3, 4]
print(middle(arr))
