from scipy.special import comb
from collections import Counter

n = int(input())
A = [int(i) for i in input().split()]

count = Counter(A)
combs = {k:comb(count[k], 2) for k in count.keys()}
combs_minas_one = {k:comb(count[k]-1, 2) for k in count.keys()}
all = sum(combs.values())

for a in A:
    ans = all - combs[a] + combs_minas_one[a]
    print(int(ans))
