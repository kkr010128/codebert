# coding:utf-8

def insertionSort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        for i in A:
            print i,
        else:
            print

N = input()
A = map(int, raw_input().split())
for i in A:
    print i,
else:
    print
insertionSort(A,N)