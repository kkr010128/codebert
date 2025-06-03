a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

dist = abs(a - b)
vd = v - w

if vd > 0:
    if 0 <= dist/vd/t <= 1:
        print("YES")
    else:
        print("NO")
elif vd == 0 and dist == 0:
    print("YES")
else:
    print("NO")