from itertools import accumulate
n, *A = map(int, open(0).read().split())
if A[0] != 0:
    if A[0] == 1 and n == 0:
        print(1)
    else:
        print(-1)
else:
    B = list(accumulate(A[::-1]))[::-1]
    C = [1] * (n+1)
    D = [1] * (n+1)

    for i in range(1, n+1):
        C[i] = min(B[i], 2*D[i-1])
        D[i] = C[i] - A[i]
        if D[i] < 0:
            print(-1)
            break
    else:
        print(sum(C))