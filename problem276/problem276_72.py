def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    diff = 10 ** 10

    partA = 0
    partB = sum(A)

    for i in range(N):
        diff = min(diff, abs(partA-partB))
        partA += A[i]
        partB -= A[i]
    print(diff)
    return
resolve()