import sys

# C - Ubiquity
N = int(input())
all = 1
no_1 = 1
no_1_and_9 = 1
mod = 10 ** 9 + 7

for _ in range(N):
  all *= 10
  all %= mod

  no_1 *= 9
  no_1 %= mod

  no_1_and_9 *= 8
  no_1_and_9 %= mod

print((all - (no_1 * 2 - no_1_and_9)) % mod)