mod = 998244353

n,s = map(int, input().split())
a = list(map(int, input().split()))

table = [0]*(s+1)
table[0] = 1
ans = 0
for ai in a:
    nxt = [0]*(s+1)
    if ai <= s:
        for j in range(ai, s+1):
            nxt[j] = table[j-ai]
    table = [(2*table[i] + nxt[i])%mod for i in range(s+1)]
ans += table[-1]
ans %= mod
print(ans)
