import math

a,b,n = list(map(int,input().split()))

if b <= n:
    x = b - 1
else:
    x = n

ans = math.floor(a * x / b)

print(ans)