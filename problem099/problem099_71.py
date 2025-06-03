import math
N, K = map(int, input().split())
As = list(map(int, input().split()))


def cut_num(a, cut_length):
    return math.ceil(a/cut_length) - 1


"""cut length N binary search
if cut num > K, search more longer cut length,
"""
l = 1
r = max(As)
m = (l+r)//2
ans = r
while r > l + 1:
    current_cut_num = sum([cut_num(a, m) for a in As])
    if current_cut_num <= K:
        r = m
    else:
        l = m
    m = (l+r)//2

if sum([cut_num(a, l) for a in As]) <= K:
    print(l)
else:
    print(r)