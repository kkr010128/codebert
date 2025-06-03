p = 998244353
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    if m%2==1:
        return (x*(pow(x,(m-1)//2)**2)%p)%p
N,M,K = map(int,input().split())
A = [1 for _ in range(N+1)]
for i in range(2,N+1):
    A[i] = (A[i-1]*i)%p
B = [1 for _ in range(N+1)]
B[N] = pow(A[N],p-2)
for i in range(N-1,1,-1):
    B[i] = (B[i+1]*(i+1))%p
C = [1 for _ in range(N)]
C[0] = M
for i in range(1,N):
    C[i] = (C[i-1]*(M-1))%p
tot = C[N-1]
for k in range(1,K+1):
    cnt = (A[N-1]*B[k]*B[N-1-k])%p
    cnt = (cnt*C[N-1-k])%p
    tot = (tot+cnt)%p
print(tot)