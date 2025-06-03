k,n = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n-1):
    a.append(k+a[i])
ans = a[n-1]-a[0]
for i in range(n,n*2-1):
    ans = min(ans,a[i]-a[i-n+1])
print(ans)