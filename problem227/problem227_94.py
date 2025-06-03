n,k=map(int,input().split())
h=list(map(int,input().split()))
h=sorted(h)
ans=0
for i in range(len(h)-k):
    ans+=h[i]
print(ans)