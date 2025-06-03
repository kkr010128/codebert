import sys
mod = 998244353

def solve():
    input = sys.stdin.readline
    N, S = map(int, input().split())
    A = [int(a) for a in input().split()]
    DP = [[0 for _ in range(S + 1)] for i in range(N)]
    DP[0][0] = 2
    if A[0] <= S: DP[0][A[0]] = 1
    ans = 0
    for i, a in enumerate(A[1:]):
        for s in range(S + 1):
            if DP[i][s] > 0:
                DP[i+1][s] += (DP[i][s] * 2) % mod
                DP[i+1][s] %= mod
                if s + a <= S:
                    DP[i+1][s+a] += DP[i][s]
                    DP[i+1][s+a] %= mod         
    print(DP[N-1][S])
    #print(DP)

    return 0

if __name__ == "__main__":
    solve()