def selection_sort(A, N):
    count = 0
    for i in range(N):
        min_j = i
        for j in range(i, N):
            if A[j] < A[min_j]:
                min_j = j
        if i != min_j:
            A[i], A[min_j] = A[min_j], A[i]
            count += 1
    print " ".join(map(str, A))
    print count

N = input()        
A = map(int, raw_input().split())
selection_sort(A, N)