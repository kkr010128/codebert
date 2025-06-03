n = int(input())
a = [int(i) for i in input().split()]
ans = 0

dp = dict()
dm = dict()

for i,ai in enumerate(a):
    dp[i+ai] = dp.get(i+ai,0)+1
    dm[i-ai] = dm.get(i-ai,0)+1

for wa,i in dm.items():
    ans += i*dp.get(wa,0)

print(ans)
