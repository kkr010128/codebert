from scipy.special import comb
import copy

MOD = 10**9+7
s = int(input())
cnt = 0
ans = 1

if s <= 2:
    print(0)
else :
    s = s-3
    while s >= 3:
        s -= 3
        cnt += 1
        if s > 0:
            ans += comb(s+cnt, cnt, exact=True)
            ans %= MOD
        else :
            ans += 1
    ans %= MOD
    print(ans)
