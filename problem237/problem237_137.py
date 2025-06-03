n=int(input())
l=sorted([list(map(int,input().split())) for i in range(n)],key=lambda x:x[0]-x[1],reverse=1)
now=float("INF")
ans=0
for i in l:
    if sum(i)<=now:
        now=i[0]-i[1]
        ans+=1
print(ans)