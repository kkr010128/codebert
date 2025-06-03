n,m=map(int,input().split())
sc=sorted([list(map(int,input().split())) for i in range(m)])
ans=[0 for i in range(n)]
res=True
for i in range(m):
    if (i>0 and sc[i][0]==sc[i-1][0] and sc[i][1]!=sc[i-1][1]) or (n>1 and sc[i][0]==1 and sc[i][1]==0):
        res=False
        break
    else:
        ans[sc[i][0]-1]=sc[i][1]

if n>1 and ans[0]==0:
    ans[0]=1

ans2=int("".join([str(i) for i in ans])) if res else -1
print(ans2)
