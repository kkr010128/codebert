import sys
readline = sys.stdin.readline
def insertionSort(n, A):
    print(*A)
    for i in range(1, n):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print(*A)
n = int(readline())
A = [int(j) for j in readline().split(" ")]
insertionSort(n, A)