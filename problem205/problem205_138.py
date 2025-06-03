from operator import mul
from functools import reduce
import sys

def cmb(n,r):
    r=min(n-r,r)
    if r==0:
        return 1
    over=reduce(mul,range(n,n-r,-1))
    under=reduce(mul,range(1,r+1))
    return over//under

N,P=map(int,input().split())
S=list(map(int,list(input())))

if P==2:
    ans=0
    for i in range(N):
        if S[i]%2==0:
            ans+=i+1
    print(ans)
    sys.exit()

if P==5:
    ans=0
    for i in range(N):
        if S[i]==0 or S[i]==5:
            ans+=i+1
    print(ans)
    sys.exit()


data=[1]*N
for i in range(N-2,-1,-1):
    data[i]=data[i+1]*10%P

data[-1]=data[-1]*S[-1]%P

for i in range(N-2,-1,-1):
    data[i]=(data[i]*S[i]+data[i+1])%P

data.sort()
cnt=1
ans=data.count(0)
for i in range(1,N):
    if data[i]==data[i-1]:
        cnt+=1
    else:
        if cnt>=2:
            ans+=cmb(cnt,2)
        cnt=1
if cnt>=2:
    ans+=cmb(cnt,2)
    
print(ans)