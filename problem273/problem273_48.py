N, K = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
s = [0] * (N+1)

for i in range(N):
    s[i+1] = s[i] + A[i]
    s[i+1] %= K
s.reverse()
for i in range(N+1):
    s[i] += (i%K)
    s[i] %= K

d = {}
ans = 0
for i in range(N+1):
    if s[i] not in d:
        d[s[i]] = 0
    if i >= K:
        d[s[i-K]] -= 1
    ans += d[s[i]]
    d[s[i]] += 1

print(ans)