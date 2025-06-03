h, a = input().split()
h = int(h)
a = int(a)
c = 0

while h > 0:
    h -= a
    c += 1

print(c)