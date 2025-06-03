N,K=map(int,input().split())
A=list(map(lambda x:int(x)%K,input().split()))
cum=[0]*(N+1)
for i in range(N):
    cum[i+1]=(cum[i]+A[i])

x=[(cum[i]-i)%K for i in range(N+1)]
dic={}
ans=0
for i in range(N+1):
    if i>=K:
        dic[x[i-K]]-=1
    ans+=dic.get(x[i],0)
    if not x[i] in dic:
        dic[x[i]]=1
    else:
        dic[x[i]]+=1
print(ans)