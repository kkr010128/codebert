X,Y = list(map(int,input().split()))

MAXN = 2*(10**6)+10
p = 10**9+7
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % p)
def nCr(n, r, mod=p):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod


Z = (X+Y)//3
if Z*3!=X+Y:
    print(0)
else:
    P,Q = X-Z, Y-Z
    if P<0 or Q<0:
        print(0)
    else:
        print(nCr(Z,P))
