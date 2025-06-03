import sys

sys.setrecursionlimit(1000000)


def solve(N, A):
    q = [(a, i) for i, a in enumerate(A)]
    q.sort(reverse=True)
    dp = [[-1 for _ in range(N + 1)] for __ in range(N + 1)]

    x = 0
    y = 0
    dp[x][y] = 0
    for a, i in q:
        dp[x+1][y] = dp[x][y] + a * abs(i - x)
        x += 1
    x = 0
    for a, i in q:
        dp[x][y+1] = dp[x][y] + a * abs(N - 1 - y - i)
        y += 1

    ans = 0
    for x in range(1, N+1):
        for y in range(1, N+1):
            if x + y > N:
                continue
            a, i = q[x+y-1]
            left = a * abs(i - (x - 1))
            right = a * abs(N - 1 - (y - 1) - i)
            dp[x][y] = max(dp[x-1][y] + left, dp[x][y-1] + right)
            ans = max(ans, dp[x][y])
    # [print(row) for row in dp]
    return ans

def slow_solve(N, A):
    import itertools
    ans = 0
    K = [i for i in range(N)]
    for p in itertools.permutations(K):
        tans = 0
        for i in range(N):
            tans += A[i] * abs(p[i] - i)
        ans = max(ans, tans)
    return ans

#
# assert (slow_solve(4, [1, 3, 4, 2]) == 20)
# assert (slow_solve(4, [1, 3, 4, 2]) == 20)
# assert (slow_solve(6, [5, 5, 6, 1, 1, 1]) == 58)
# assert (slow_solve(6, [8, 6, 9, 1, 2, 1]) == 85)
# print("OK")
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split(" ")))

    print(solve(N, A))
