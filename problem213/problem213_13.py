N = int(input())
X = list(map(int, input().split()))
ans = 10**12
for i in range(1,101):
    res = 0
    for j in range(N):
        res += (X[j]-i)**2
    ans = min(ans, res)
print(ans)