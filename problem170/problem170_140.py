
n,k = map(int,input().split())
a = list(range(n))

ans = 0

for i in range(k,n+2):
    min1 = 0.5*i*(i-1)
    max1 = 0.5*(n*(n+1)-(n-i)*(n-i+1))
    sub1 = max1 - min1+1
    ans += sub1


print(int(ans%(10**9+7)))
