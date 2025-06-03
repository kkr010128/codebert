from collections import Counter

MOD = 2019
S = input()
S = tuple(map(int, reversed(S)))
counter = Counter([0])
digit = 1
cumsum = 0

for i in range(len(S)):
    cumsum += S[i] * digit % MOD
    cumsum %= MOD
    counter[cumsum] += 1
    digit = digit * 10 % MOD

print(sum([v * (v - 1) // 2 for v in counter.values()]))
