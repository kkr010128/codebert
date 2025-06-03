def nCr(n, r, mod):
    x, y = 1, 1
    for i in range(1, r+1):
        x = x*(n+1-i)%mod
        y = y*i%mod
    return x*pow(y, mod-2, mod)%mod
a,b = map(int,input().split())
s=2*a-b
t=2*b-a
if s%3!=0 or s<0 or t%3!=0 or t<0:
  print(0)
else:
  print(nCr((s+t)//3,(t//3),10**9+7))