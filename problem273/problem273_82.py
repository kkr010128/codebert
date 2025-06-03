from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))
delta_count = defaultdict(int)
sum = [0]
delta_count[0] += 1
for i in range(n):
    sum.append(sum[i] + A[i])
ans = 0
for i in range(1, min(n + 1, k)):
    x = (sum[i] - i) % k
    ans += delta_count[x]
    delta_count[x] += 1
for i in range(min(n + 1, k), n + 1):
    delta_count[(sum[i - k] - i - k) % k] -= 1
    x = (sum[i] - i) % k
    ans += delta_count[x]
    delta_count[x] += 1
print(ans)