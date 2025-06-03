N,K=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7

if N==K: #全部
    ans=1
    for i in range(N):
        ans*=A[i]
        ans%=mod
    print(ans)
    exit()
if max(A)<0 and K%2==1: #答えがマイナス
    A.sort(reverse=True)
    ans=1
    for i in range(K):
        ans*=A[i]
        ans%=mod
    print(ans)
    exit()

plus=[]
minus=[]
for i in range(N):
    if A[i]>=0:
        plus.append(A[i])
    else:
        minus.append(A[i])
plus.sort(reverse=True) #5,3,1
minus.sort() #-5,-3,-1
plus_k=0
minus_k=0
if K%2==0:
    ans=1
else:
    ans=plus[0]
    plus_k=1

for _ in range(K):
    if plus_k+minus_k==K:
        break
    if plus_k>=len(plus)-1:
        ans*=minus[minus_k]*minus[minus_k+1]%mod
        ans%=mod
        minus_k+=2
        continue
    if minus_k>=len(minus)-1:
        ans*=plus[plus_k]*plus[plus_k+1]%mod
        ans%=mod
        plus_k+=2
        continue
    if plus[plus_k]*plus[plus_k+1]>minus[minus_k]*minus[minus_k+1]:
        ans*=plus[plus_k]*plus[plus_k+1]%mod
        ans%=mod
        plus_k+=2
        continue
    else:
        ans*=minus[minus_k]*minus[minus_k+1]%mod
        ans%=mod
        minus_k+=2
        continue
print(ans)
