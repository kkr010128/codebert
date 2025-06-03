n,k=map(int,input().split())
a=list(map(int,input().split()))
a.reverse()
ans=[]
for i in range(k,n):
    if a[i]<a[i-k]:
        ans.append("Yes")
    else:
        ans.append("No")
ans.reverse()
for s in ans:
    print(s)
