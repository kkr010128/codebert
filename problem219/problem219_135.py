import sys
import functools
# sys.setrecursionlimit(100000000)
n = input()
# import random
# n = ''.join(str(random.randint(1,9)) for _ in range(10**6))

#
# @functools.lru_cache(None)
# def doit(index: int, carry: int) -> int:
#     if index >= len(n):
#         return 0 if carry == 0 else 2
#     d = int(n[index])
#     if carry > 0:
#         return min(10 - d + doit(index + 1, 0), 9 - d + doit(index + 1, 1))
#     else:
#         return min(d + doit(index + 1, 0), d + 1 + doit(index + 1, 1))
#
#
# print(min(doit(0, 0), 1 + doit(0, 1)))


dp = [0, 2]
for d in reversed(n):
    d = int(d)
    dp = [min(d + dp[0], d + 1 + dp[1]), min(10 - d + dp[0], 9 - d + dp[1])]

print(min(dp[0], 1 + dp[1]))
