import string
ab = string.ascii_lowercase
bc = ab[1:] + 'a'
c = input()
for a, b in zip(ab, bc):
    if a == c:
        print(b)
