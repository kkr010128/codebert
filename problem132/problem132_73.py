import numpy as np
from numba import njit

N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
a = np.array(A, dtype=int)


fin = [N] * N

@njit(cache=True)
def calc_b(a):
    b = np.zeros(N, dtype=np.int64)
    for i, _a in enumerate(a):
        l = max(0, i - _a)
        r = min(N - 1, i + _a)

        # imos hou
        b[l] += 1
        if r + 1 < N:
            b[r + 1] -= 1

    b = np.cumsum(b)
    # print('b_sum', b)
    return b


for k in range(min(K,100)):
    # print('a', a)
    a = calc_b(a)
    # if all(a == fin):
    #     break

a = [str(_) for _ in a]
print(' '.join(a))
# print('step=', k)