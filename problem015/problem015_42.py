# -*- coding: utf-8 -*-


def selection_sort(A, N):
    change = 0
    for i in xrange(N):
        minj = i
        for j in xrange(i, N, 1):
            if A[j] < A[minj]:
                minj = j
        if minj != i:
            temp = A[minj]
            A[minj] = A[i]
            A[i] = temp
            change += 1
    return (A, change)


if __name__ == "__main__":
    N = input()
    A = map(int, raw_input().split())
    result, change = selection_sort(A, N)
    print ' '.join(map(str, result))
    print change