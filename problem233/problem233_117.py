n=int(input())
a=list(map(int, input().split()))
m=a[0]
ans=0
for i in range(n):
    x=a[i]
    if x<=m:
        ans+=1
        m=x
print(ans)