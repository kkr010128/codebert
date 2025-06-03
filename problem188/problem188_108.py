x,y,a,b,c=map(int,input().split())
p=sorted(list(map(int,input().split())),reverse=1)[:x]
q=sorted(list(map(int,input().split())),reverse=1)[:y]
r=sorted(list(map(int,input().split())),reverse=1)
pq=sorted(p+q,reverse=1)
ans=sum(pq)

n=len(r)
count=-1
for i in range(n):
    if r[i]>pq[count]:
        ans+=(r[i]-pq[count])
        count-=1
print(ans)