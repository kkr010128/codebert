# Bubble sort: ALDS1_2_A

def bsort(A, N):
    flag = 1
    swap = 0
    while flag:
        flag = 0
        for j in reversed(range(1, N)):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
                swap += 1
    return swap

N = int(raw_input())
A = [int(i) for i in raw_input().split()]

swap = bsort(A, N)
print " ".join([repr(i) for i in A])
print swap

