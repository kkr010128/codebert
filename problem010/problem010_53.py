def insersionSort(A, N):
    for i in range(1, N):
        print " ".join([str(k) for k in A])
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
    return A

if __name__ == "__main__":
    N = int(raw_input())
    A = map(int, raw_input().split())
    A = insersionSort(A, N)
    print " ".join([str(k) for k in A])