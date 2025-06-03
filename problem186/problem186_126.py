k,n = map(int,input().split())
a = list(map(int,input().split()))
ans = 10 ** 8
for i in range(n-1):
    a.append(a[i]+k)
for i in range(n):
    ans = min(ans,a[i+n-1] - a[i])
print(ans)