n, k = list(map(int, input().split()))
p = list(map(int, input().split()))
r = [0]*(n + 1)
for i in range(1,n + 1):
    r[i] += r[i - 1] + (p[i - 1] + 1) / 2
ans = 0
for j in range(n - k + 1):
    ans = max(ans, r[j+k] - r[j])
print(ans)
