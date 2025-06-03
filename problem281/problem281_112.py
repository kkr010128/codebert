def nCr(n, r, mod):
    x, y = 1, 1
    for r_ in range(1, r+1):
        x = x*(n+1-r_)%mod
        y = y*r_%mod
    return x*pow(y, mod-2, mod)%mod
 
x, y = map(int, input().split())
mod = 10**9+7
if (x+y)%3 or 2*x<y or 2*y<x:
    print(0)
else:
    print(nCr((x+y)//3,(2*x-y)//3, mod))