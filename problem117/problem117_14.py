n, m, k =map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
ta=sum(a)
a.append(0)
tb=0
ans=0
j=0
for i in range(n+1):
    ta -= a[n-i]
    if ta>k:
        continue
    while tb + ta<=k:

        if j ==m:
            ans=max(ans,n-i+j)
            break
        ans=max(ans,n-i+j)
        tb += b[j]
        j +=1

print(ans)
