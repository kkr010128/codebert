import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    if N == 0 and A[0] > 1:
        print(-1)
        return 0
    low, high = A[N], A[N]
    maxN = [0] * (N + 1)
    maxN[N] = A[N]
    Limit = [2 ** 50] * (N + 1)
    Limit[N] = A[N]

    for i in reversed(range(N)):
        leaf = A[i]
        Limit[i] = min(Limit[i], Limit[i+1] + leaf)
        if i <= 50: Limit[i] = min(pow(2, i), Limit[i])
        low = (low + 1) // 2 + leaf
        high += leaf
        if low > Limit[i]:
            print(-1)
            break
        else: 
            maxN[i] = min(high, Limit[i])
    else:
        for i in range(N):
            if (maxN[i] - A[i]) * 2 <= maxN[i+1]: maxN[i + 1] = (maxN[i] - A[i]) * 2
        print(sum(maxN))

    return 0

if __name__ == "__main__":
    solve()
