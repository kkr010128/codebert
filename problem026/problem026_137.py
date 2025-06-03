n = int(raw_input())
a = map(int, raw_input().split())
count = 0

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [0 for i in range(n1+1)]
    R = [0 for i in range(n2+1)]
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L[n1] = 10**9 + 1
    R[n2] = 10**9 + 2
    i = 0
    j = 0
    for k in range(left, right):
        global count
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = int((left + right) /2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

mergeSort(a, 0, n)
print ' '.join(map(str, a))
print count