a, v = list(map(int, input().split()))
b, w = list(map(int, input().split()))
t = int(input())

x = abs(a-b)

y = (v - w) * t

if y >= x:
    print('YES')
else:
    print('NO')
