n,m=map(int,input().split())
sc=[list(map(int,input().split())) for _ in range(m)]
for i in range(10**n):
    ans=str(i)
    if len(ans)==n and all(ans[s-1]==str(c) for s,c in sc):
        print(ans)
        exit()
print(-1)