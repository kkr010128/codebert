def SelectionSort(A, n):
    sw = 0
    for i in xrange(n):
        minj = i
        for j in xrange(i, n):
            if A[j] < A[minj]:
                minj = j
        temp = A[minj]
        A[minj] = A[i]
        A[i] = temp
        if i != minj:
            sw += 1
    return sw

def printArray(A, n):
    for i in xrange(n):
        if i < n-1:
            print A[i],
        else:
            print A[i]

n = input()
arr = map(int, raw_input().split())
cnt = SelectionSort(arr, n)
printArray(arr, n) 
print cnt