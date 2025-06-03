n,k = map(int,input().split())
P = 10**9+7

ans = 1
nCl = 1
n1Cl = 1
for l in range(1,min(k+1,n)):
    nCl = nCl*(n+1-l)*pow(l,P-2,P)%P
    n1Cl = n1Cl*(n-l)*pow(l,P-2,P)%P
    ans = (ans+nCl*n1Cl)%P

print(ans)
