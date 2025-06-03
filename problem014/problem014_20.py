# encoding: utf-8

def bubble_sort(A, N):
    flag = 1
    count = 0
    while flag:
        flag = 0
        for j in xrange(N-1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
                count += 1
    return A, count

def main():
    N = input()
    A = map(int, raw_input().split())
    A, count = bubble_sort(A, N)
    print " ".join(map(str,A))
    print count

main()