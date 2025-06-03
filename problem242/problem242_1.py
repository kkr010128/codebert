def memfact(a,m):
    temp = 1
    yield temp
    for i in range(1,a+1):
        temp = temp * i % m
        yield temp
def comb(n,r,m):
    if r == 0: return 1
    return memf[n]*pow(memf[r],m-2,m)*pow(memf[n-r],m-2,m)

N,K,*a = map(int, open(0).read().split())
m = 1000000007
memf = []
mfappend = memf.append
for x in memfact(N-1,m):
    mfappend(x)
a.sort()
ans = 0
if K == 1:
    print(0)
else:
    for i in range(1,N-K+2):
        ans = (ans + a[-i] * comb(N-i,K-1,m)) % m
    for i in range(1,N-K+2):
        ans = (ans - a[i-1] * comb(N-i,K-1,m)) % m
    print(ans)