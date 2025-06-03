a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if a == b:
    print("NO")

As = v * t + a
Bs = w * t + b

if v > w:
    if abs(a - b)/abs(v - w) <= t:
        print("YES")
    else:
        print("NO")
else:
    print("NO")