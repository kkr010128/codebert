k,n=map(int,input().split())
dis=list(map(int,input().split()))
ans=[]
for i in range(n):
    if i>=1:
        ans.append(dis[i]-dis[i-1])
ans.append(dis[0]+(k-dis[n-1]))
print(k-max(ans))
