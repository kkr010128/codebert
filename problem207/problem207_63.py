a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g, h, i = map(int, input().split())
n = int(input())
for j in range(n):
    x = int(input())
    if a == x:
        a = 0
    elif b == x:
        b == 0
    elif c == x:
        c = 0
    elif d == x:
        d = 0
    elif e == x:
        e = 0
    elif f == x:
        f = 0
    elif g == x:
        g = 0
    elif h == x:
        h = 0
    elif i == x:
        i = 0
y =[[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, g]]
print("Yes" if [0, 0, 0] in y else "No")