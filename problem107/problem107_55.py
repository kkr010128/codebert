
import math
from collections import defaultdict,deque
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

def fast_expo(x,y,m):
    res=1
    while(y):
        if(y&1):
            res*=x
            res%=m
        x*=x
        x%=m
        y>>=1
    return res    

dp=defaultdict(int)
dp[1]=1
dp[2]=1
for i in range(3,200001):
    k=i
    cnt=0
    while(k):
        if(k%2): cnt+=1
        k>>=1
    dp[i]=dp[i%cnt]+1
n=ii()
a=ip()
a=a[::-1]
c=a.count('1')

min_1=0
max_1=0

for i in range(n):
    if(a[i]=='1'):
        if(c-1!=0):
            min_1+=fast_expo(2,i,c-1)
            min_1%=(c-1)
        max_1+=fast_expo(2,i,c+1)
        
        max_1%=(c+1)
    
ans=[]    

for i in range(n):
    if(a[i]=='1'):
        if(c-1==0):
            ans.append(0)
        else:    
            ans.append(dp[(min_1-fast_expo(2,i,c-1)+(c-1))%(c-1)]+1)
    else:
        ans.append(dp[(max_1+fast_expo(2,i,c+1))%(c+1)]+1)
ans=ans[::-1]
for i in ans:
    print(i)