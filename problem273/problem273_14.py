from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]

ans = 0
d = defaultdict(int)
for j in range(n + 1):
    if j - k >= 0:
        d[(a_cs[j - k] - (j - k)) % k] -= 1

    # print(j, d, d[(a_cs[j] - j) % k])
    ans += d[(a_cs[j] - j) % k]

    d[(a_cs[j] - j) % k] += 1

print(ans)
