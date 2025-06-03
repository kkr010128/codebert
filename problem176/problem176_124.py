N,K=map(int,input().split())
mod=10**9+7
X=[0]+[pow(K//d,N,mod) for d in range(1,K+1)]
'''
Y=[[] for i in range(K+1)]
for i in range(1,K+1):
    for j in range(i,K+1,i):
        Y[j].append(i)
'''
#print(X)
isPrime=[1 for i in range(K+1)]
isPrime[0]=0;isPrime[1]=0
for i in range(K+1):
    if isPrime[i]==0:
        continue
    for j in range(2*i,K+1,i):
        isPrime[j]=0
Mebius=[1 for i in range(K+1)]
Mebius[0]=0
for i in range(2,K+1):
    if isPrime[i]==0:
        continue
    for j in range(i,K+1,i):
        Mebius[j]*=-1
for i in range(2,K+1):
    for j in range(i*i,K+1,i*i):
        Mebius[j]=0
Z=[0 for i in range(K+1)]
for i in range(1,K+1):
    for j in range(i,K+1,i):
        Z[i]+=X[j]*Mebius[j//i]
ans=0
for i in range(1,K+1):
    ans+=Z[i]*i
    ans%=mod
print(ans)
'''
P(G%d==0)
Gがd,2d,3d,...の可能性がある
P(d)-P(2d)-P(3d)-P(5d)+P(6d)-P(7d)
'''