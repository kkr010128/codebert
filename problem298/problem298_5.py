r=input().split()
N=int(r[0])
K=int(r[1])
d=[int(s) for s in input().split()]
ans=0
for i in range(N):
    if d[i]>=K:
        ans+=1
print(ans)