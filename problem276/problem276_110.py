n = int(input())
a = list(map(int,input().split()))
a_cumsum = [0]*(n+1)
for i in range(n):
    a_cumsum[i+1] = a_cumsum[i] + a[i]

ans = 10**18
for i in range(n):
    ans = min(ans, abs(a_cumsum[-1] - a_cumsum[i]*2))
print(ans)