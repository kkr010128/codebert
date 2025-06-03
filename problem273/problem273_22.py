N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
sa = [0]
for a in A:
    sa.append((sa[-1] + a) % K)
d = {0: 1}
ans = 0
for i in range(1, N+1):
    if i >= K:
        d[sa[i-K]] -= 1
    v = d.get(sa[i], 0)
    ans += v
    d[sa[i]] = v + 1
print(ans)