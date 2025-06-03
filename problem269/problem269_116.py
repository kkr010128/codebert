t1, t2 = (int(x) for x in input().split())
a1, a2 = (int(x) for x in input().split())
b1, b2 = (int(x) for x in input().split())

if a1 < b1:
    a1, b1 = b1, a1
    a2, b2 = b2, a2

if a1 * t1 + a2 * t2 > b1 * t1 + b2 * t2:
    print(0)
    exit()
elif a1 * t1 + a2 * t2 == b1 * t1 + b2 * t2:
    print("infinity")
    exit()

d1 = (a1 - b1) * t1
d2 = (b2 - a2) * t2
k = d1 // (d2 - d1)
if d1 % (d2 - d1) == 0:
    print(2 * k)
else:
    print(2 * k + 1)
