N = int(input())
X = list(map(int, input().split()))
assert len(X) == N
# N人が点Xiに住んでいる
# 任意の整数値の点で集会を開く
# 2乗距離の体力を消耗

# 点yで集会
def sum_power(y):
  return sum([(x - y) * (x - y) for x in X])

import sys
minimum = sys.maxsize
for y in range(min(X), max(X)+1):
  minimum = min(minimum, sum_power(y))
print(minimum)