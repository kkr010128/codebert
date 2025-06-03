a, b = map(int, input().split())
if a < b:
    a, b = b, a

c = a
d = b
r = c // d
m = c % d

while True:
    if m == 0:
        break
    else:
        c = d
        d = m
        m = c % d

print(int(a * b / d))