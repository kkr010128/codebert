a, b, c = (int(x) for x in input().split())

tmp = 0

for i in range(2):
    if a > b:
        tmp = a
        a = b
        b = tmp
    if b > c:
        tmp = b
        b = c
        c = tmp
    if a > c:
        tmp = a
        a = c
        c = tmp

print(a, b, c)

