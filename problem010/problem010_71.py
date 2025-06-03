def insert_sort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v; print(*A)

N = int(input())
A = [int(n) for n in input().split()]; print(*A)
insert_sort(A, N)

