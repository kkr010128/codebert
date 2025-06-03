def bubbleSort(A, N):
    count = 0
    for j in range(N - 1):
        for i in reversed(range(j + 1, N)):
            if A[i - 1] > A[i]:
                temp = A[i]
                A[i] = A[i - 1]
                A[i - 1] = temp
                count = count + 1
    for i in range(N):
        print A[i],
    print
    print count

N = input()
A = map(int, raw_input().split())

bubbleSort(A, N)