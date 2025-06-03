import itertools
import math

K = int(input())
nums = range(1, K + 1)
comb = itertools.combinations_with_replacement(nums, 3)
ans = 0

for v in comb:
    n1 = math.gcd(v[0], v[1])
    n2 = math.gcd(n1, v[2])
    l = len(list(set(v)))
    if l == 3:
        ans += 6 * n2
    elif l == 2:
        ans += 3 * n2
    elif l == 1:
        ans += n2
print(ans)
