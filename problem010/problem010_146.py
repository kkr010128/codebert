# coding=utf-8


def insertionSort(A, N):
    print ' '.join(map(str, A))
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print ' '.join(map(str, A))
    return A


n = int(raw_input().rstrip())
a = map(int, raw_input().rstrip().split())
insertionSort(a, n)