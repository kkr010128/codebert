from collections import defaultdict
N, K = map(int,input().split())
A = list(map(int,input().split()))

a = [0]

for i in A:
    a.append((a[-1]+i-1)%K)

d = defaultdict(int)
ans = 0
for i in range(N+1):
    if i >= K:
        d[a[i-K]] -= 1
    ans += d[a[i]]
    d[a[i]] += 1

print(ans)
