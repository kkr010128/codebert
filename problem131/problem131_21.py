a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

d = abs(a - b)
u = abs(v - w)

if w >= v:
    print("NO")
else:
    if u * t >= d:
        print('YES')
    else:
        print('NO')