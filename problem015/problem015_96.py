def selectionSort(A, N):
    count = 0
    for i in range(N - 1):
        minValue = 100
        minIndex = 0
        for j in range(i, N):
            if A[j] < minValue:
                minValue = A[j]
                minIndex = j
        if minIndex != i:
            temp = A[i]
            A[i] = minValue
            A[minIndex] = temp
            count = count + 1

    for i in range(N):
        print A[i],
    print
    print count

N = input()
A = map(int, raw_input().split())

selectionSort(A, N)