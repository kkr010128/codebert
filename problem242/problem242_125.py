N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

M = 10**9+7

def pow(a,b,M):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return pow((a**2)%M,b//2,M) % M
    else:
        return ((a % M) * pow((a**2)%M,b//2,M)) % M

def inv(a,p):
    return pow(a,p-2,p)

ans,comb = 0,1
#i番目ではcomb = (K-1-i)_C_(K-1)
#max,min以外での選ぶ個数は常にK-1であることに注目すればcomb関数はいらなかった
for i in range(N-K+1):
    if i > 0:
        comb = (comb * (K-1+i) * inv(i,M)) % M
    ans = (ans + comb*((A[K-1+i]-A[N-K-i]) % M)) % M
print(ans)
