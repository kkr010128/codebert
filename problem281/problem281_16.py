x, y = map(int, input().split())
mod = 10**9 + 7
if (2*x-y)%3 == 0 and (2*y-x)%3 == 0 and 2*x-y >= 0 and 2*y-x >= 0:
    u = (2*x-y)//3
    v = (2*y-x)//3
    n = u + v
    x = 1
    y = 1
    for i in range(u):
        x = x*(n-i)%mod
        y = y*(i+1)%mod
    print((x * pow(y, mod-2, mod))%mod)
else:
    print(0)