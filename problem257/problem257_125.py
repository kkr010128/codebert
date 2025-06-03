def resolve():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = [int(i) for i in input().split()]
    if 1 not in A:
        print(-1)
        return
    sumA = 0
    try:
        i = 1
        while sumA + i <= N:
            sumA += A.index(i, (sumA + i - 1)) - (sumA + i - 1)
            i += 1
        print(sumA)
    except BaseException:
        sumA += N - (sumA + i - 1)
        print(sumA)


resolve()
