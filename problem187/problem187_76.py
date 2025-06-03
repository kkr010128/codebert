def mlt(): return map(int, input().split())


x, a, b = mlt()

dp = [0 for n in range(x)]

for n in range(1, x+1):
    for k in range(n+1, x+1):
        d1 = k-n
        d2 = abs(a-n)+1+abs(b-k)
        ds = min(d1, d2)
        dp[ds] += 1

print(*dp[1:], sep='\n')
