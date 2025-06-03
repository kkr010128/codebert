import itertools
import numpy as np

N_book, M_algo, X_skill = map(int, input().split())  

A = []
for _ in range(N_book):
    a = list(map(int, input().split()))
    A.append(a)

flg = False
ans = float('inf')
for selector in list(itertools.product([1, 0], repeat=N_book))[:-1]:
    C = []
    for i in range(N_book):
        if selector[i] == 1:
            C.append(A[i])
    
    D = list(np.array(C).sum(axis=0))
    if (False in [i >= X_skill for i in D[1:]]):
        continue
    else:
        flg = True
        ans = min(ans, D[0])

if flg:
    print(ans)
else:
    print(-1)