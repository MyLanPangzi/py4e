# Exercise 3: Encapsulate this code in a function named count,
# and generalize it so that it accepts the string and the letter as arguments.
def count(s, letter):
    r = 0
    for w in s:
        if w == letter:
            r = r + 1
    return r


print(count('banana', 'a'))
print(count('banana', 'b'))
print(count('banana', 'n'))
