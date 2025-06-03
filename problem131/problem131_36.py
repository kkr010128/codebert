import sys

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if (a == b):
    print('YES')
    sys.exit(0)
if (v <= w):
    print('NO')
    sys.exit(0)
res = abs(a - b) / (v - w)
if (res > t):
    print('NO')
else:
    print('YES')
sys.exit(0)

