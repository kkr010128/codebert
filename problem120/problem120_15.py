n,k=map(int,input().split())
li=list(map(int,input().split()))
li_sort=sorted(li)
ans=0
for i in range(k):
    ans+=li_sort[i]
print(ans)