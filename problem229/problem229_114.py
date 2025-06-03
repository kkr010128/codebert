from collections import defaultdict
(h,n),*ab = [list(map(int, s.split())) for s in open(0)]

mxa = max(a for a,b in ab)

dp = defaultdict(lambda: float('inf'))
dp[0] = 0

for i in range(1, h+mxa):
    dp[i] = min(dp[i-a] + b for a,b in ab)

print(min(v for k,v in dp.items() if k>=h))