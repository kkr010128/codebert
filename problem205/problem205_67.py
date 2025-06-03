from copy import copy
from collections import defaultdict
n, p = map(int, input().split())

s = input()
ans = 0
if p == 2 or p == 5:
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i + 1
else:
    dp = [0] * p
    dp[0] = 1
    tmp = 0
    for i in range(n)[::-1]:
        tmp = (int(s[i]) * pow(10, n - i - 1, p) + tmp) % p
        # tmp = (int(s[i]) * 10 ** (n - i - 1) + tmp) % p
        # print(tmp, int(s[i]) * 10 ** (n - i - 1))
        ans += dp[tmp]
        dp[tmp] += 1 
    # print(dp)

print(ans)