import sys

x, k, d = map(int,input().split())
x = abs(x)
ans = 0

if k <= x // d:
    ans = x - k*d
    print(ans)
    sys.exit()

if (k - (x // d)) % 2 == 0:
    print(x % d)
else:
    print(abs(x % d - d))