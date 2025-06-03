a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
ans = abs(b - a) - (v - w) * t
if ans > 0:
    print('NO')
else:
    print('YES')
