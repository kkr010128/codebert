n,m,q=map(int, input().split())
s=[list(map(int, input().split())) for i in range(q)]

import itertools
A = [i for i in range(1,m+1)]
k = list(itertools.combinations_with_replacement(A, n))


ma = 0
for i in k:
    su = 0
    for n in s:
        if i[n[1]-1] - i[n[0]-1] == n[2]:
            su += n[3]
    ma = max(ma,su)

print(ma)