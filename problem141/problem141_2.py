def solve():
    N = int(input())
    lfs = list(map(int, input().strip().split()))
    ans = 0
    L = 1 << N
    lo = lfs[-1]
    hi = lfs[-1]
    memo = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        if lo > L:
            return -1
        memo[i + 1] = hi
        lo = (lo + 1) // 2 + lfs[i]
        hi = hi + lfs[i]
        L = L >> 1

    if lo > L:
        return -1
    memo[0] = hi
    
    curr = 1
    for i in range(N + 1):
        ans += min(memo[i], curr)
        curr = (curr - lfs[i]) << 1
    return ans

print(solve())