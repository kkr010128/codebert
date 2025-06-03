a, b, c = map(int, input().split())
d = abs(a)
count = min(d//c, b)
d -= c*count
b -= count
if b % 2 == 1:
    d -= c
print(abs(d))