n,m=map(int,input().split())
a=list(map(int,input().split()))

ans=n

for i in range(m):
    ans-=a[i]
    if ans<0:
        ans=-1
        break
print(ans)
