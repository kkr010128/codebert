import sys
from collections import Counter
n = int(input())
a_ls = [int(i) for i in sys.stdin.readline().split()]
minus_a_ct = Counter([-a-i for i,a in enumerate(a_ls)])
a_ct = Counter([a-i for i,a in enumerate(a_ls)])
_sum = 0
for k, v in a_ct.items():
    _sum += v * minus_a_ct[k]
print(_sum)