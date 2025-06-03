a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())

if v <= w:
    print('NO')
    exit(0)

n = abs(a - b)
m = abs(v - w)

if n / m <= t:
    print('YES')
else:
    print('NO')