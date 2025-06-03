import numpy as np
from numba import njit
@njit
def op(A, n):
    B = np.zeros_like(A)
    for i, a in enumerate(A[:n]):
        B[max(i - a, 0)] += 1
        B[min(n - 1, a + i) + 1] -= 1
    return np.cumsum(B)

def main():
    n, k = list(map(int, input().split()))
    A = np.array(list(map(int, input().split())) + [0, ], dtype = np.int)
    for _ in range(k):
        A_new = op(A, n)
        if all(A[:n] == A_new[:n]):
            break
        A = A_new
    print(' '.join(list(map(str, A[:n]))))

if __name__ == '__main__':
    main()
