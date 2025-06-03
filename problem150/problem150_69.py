259
N,K=map(int,input().split())
A=[0]+list(map(int,input().split()))
m=1
towns=[1]
flg=[0]*(N+1)
flg[1]=1
while 1:
    m=A[m]
    towns.append(m)
    if flg[m]==1:
        l=len(towns)-towns.index(m)-1
        break
    flg[m]=1
pl=towns.index(m)
if K<=pl:
    print(towns[K])
else:
    print(towns[(K-pl)%l+pl])