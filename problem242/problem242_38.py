N,K=map(int,input().split())
A=list(map(int,input().split()))
Nlist=[0]*(10**5+1)
P=10**9+7
Nlist[1]=1
for i in range(1, 10**5):
    Nlist[i+1]=(Nlist[i]*(i+1))%P
Ninv=[1]*(10**5+1)
Ninv[-1]=pow(Nlist[-1], P-2,P)
for i in range(0,10**5):
    Ninv[-1-i-1]=(Ninv[-1-i]*(10**5-i))%P
for i in range(N):
    A[i]=[A[i], i]
A.sort()
ans=0
for i in range(K-1,N):
    if A[i][0]>=0:
        ans+=(A[i][0]*Nlist[i]*Ninv[K-1]*Ninv[i-K+1])%P
    else:
        ans+=(A[i][0]*Nlist[i]*Ninv[K-1]*Ninv[i-K+1])%P-P
for i in range(0,N-K+1):
    if A[i][0]>=0:
        ans-=(A[i][0]*Nlist[N-i-1]*Ninv[K-1]*Ninv[N-i-K])%P
    else:
        ans-=(A[i][0]*Nlist[N-i-1]*Ninv[K-1]*Ninv[N-i-K])%P-P
print(ans%P)