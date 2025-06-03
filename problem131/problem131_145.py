a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if a <= b:
    print("YES" if a + v * t >= b + w * t else "NO")
else:
    print("YES" if b - w * t >= a - v * t else "NO")
