import numpy as np


def check_bingo(A):
    for i in range(3):
        if np.all(A[i] == -1) or np.all(A[:, i] == -1):
            return 'Yes'
    if np.all(A[list(range(3)), list(range(3))] == -1) \
            or np.all(A[list(range(3)), list(range(3))[::-1]] == -1):
        return 'Yes'

    return 'No'


def main():
    A = np.array([list(map(int, input().split())) for _ in range(3)])
    n = int(input())
    for i in range(n):
        b = int(input())
        A = np.where(A == b, -1, A)
    ans = check_bingo(A)
    print(ans)


if __name__ == '__main__':
    main()
