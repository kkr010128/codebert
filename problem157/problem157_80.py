def resolve():
    from collections import defaultdict
    N = int(input())
    A = [int(i) for i in input().split()]
    L = defaultdict(int)
    ans = 0
    for i in range(N):
        L[A[i] + i] += 1
        ans += L[i - A[i]]
    print(ans)


resolve()
