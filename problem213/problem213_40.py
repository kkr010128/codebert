N = int(input())
X = list(map(int, input().split()))

ans = 1000000000

for i in range(1, max(X)+1):
    l = 0
    for j in range(N):
        l += (i - X[j]) ** 2
    ans = min(ans, l)

print(ans)