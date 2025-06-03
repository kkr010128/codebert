import numpy as np
from numba import njit, i8


@njit(i8[:](i8, i8, i8[:]), cache=True)
def myfunc(n, k, A):
    for _ in range(k):
        l = np.zeros((n + 1,), dtype=np.int64)
        for i, a in enumerate(A[:-1]):
            l[max(0, i - a)] += 1
            l[min(n, i + a + 1)] -= 1
        A = np.cumsum(l)
        if np.all(A[:-1] == n):
            break
    return A


def main():
    n, k = map(int, input().split())
    A = np.array(list(map(int, input().split())), dtype=np.int64)
    A = np.append(A, 0)
    print(*myfunc(n, k, A)[:-1])


if __name__ == "__main__":
    main()