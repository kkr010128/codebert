n,k,s=map(int,input().split())
ans=[0]*n
if s!=10**9:
    for i in range(k):
        ans[i]=s
    for i in range(k,n):
        ans[i]=10**9
else:
    for i in range(k):
        ans[i]=s
    for i in range(k,n):
        ans[i]=1
print(*ans)
