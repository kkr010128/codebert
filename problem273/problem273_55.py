import itertools, collections
N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
C = list(itertools.accumulate([0] + A))
D = [(v - i) % K for i, v in enumerate(C)]
#D[i]==D[j] and i-j<K
dp = collections.Counter(D[:K])
ans = 0
for i in range(N):
    dp[D[i]] -= 1
    ans += dp[D[i]]
    if i + K < len(D):
        dp[D[i + K]] += 1
print(ans)
