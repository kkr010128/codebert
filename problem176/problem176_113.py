import sys
input=sys.stdin.readline
n,k=map(int,input().split())
INF=10**9+7
l=[0]*k
ans=0
for i in range(k-1,-1,-1):
    x=i+1
    temp=pow(k//x,n,INF)
    for j in range(2,k//x+1):
        temp=(temp-l[j*x-1])%INF
    l[i]=temp
    ans=(ans+x*temp)%INF
print(ans)









