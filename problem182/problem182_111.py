import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
from collections import Counter
def resolve():
    N, K, C = lr()
    S = [i+1 for i, s in enumerate(sr()) if s == 'o']
    l = [S[0]]
    for i in S[1:]:
        if l[-1]+C >= i or len(l) > K:
            continue
        l.append(i)
    S = S[::-1]
    r = [S[0]]
    for i in S[1:]:
        if r[-1]-C <= i or len(r) > K:
            continue
        r.append(i)
    r = r[::-1]
    for i in range(K):
        if l[i] == r[i]:
            print(l[i])
resolve()