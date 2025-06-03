def insertionSort(A, N):
    print " ".join([str(t) for t in A])
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print " ".join([str(t) for t in A])

if __name__ == "__main__":
    N = input()
    A = map(int, raw_input().split())
    insertionSort(A, N)