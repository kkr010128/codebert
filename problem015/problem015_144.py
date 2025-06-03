N = int(raw_input())
A = map(int, raw_input().split())

def selectionSort(A, N):
    count = 0
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            temp = A[i]
            A[i] = A[minj]
            A[minj] = temp
            count += 1
    return count

count = selectionSort(A, N)

print " ".join(map(str, A))
print count