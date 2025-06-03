import sys

def solve():
    input = sys.stdin.readline
    R, C, K = map(int, input().split())
    item = [[0 for _ in range(C)] for r in range(R)]
    for _ in range(K):
        r, c, k = map(int, input().split())
        item[r-1][c-1] = k
    
    DP = [[[-1 for _ in range(C)] for r in range(R)] for i in range(4)]
    DP[0][0][0] = 0
    for r in range(R):
        for c in range(C):
            for i in range(4):
                if DP[i][r][c] > -1:
                    if r + 1 < R: 
                        DP[0][r+1][c] = max(DP[0][r+1][c], DP[i][r][c])
                    if c + 1 < C: 
                        DP[i][r][c+1] = max(DP[i][r][c+1], DP[i][r][c])
                    if i < 3 and item[r][c] > 0:
                        if r + 1 < R: DP[0][r+1][c] = max(DP[0][r+1][c], DP[i][r][c] + item[r][c])
                        if c + 1 < C: DP[i+1][r][c+1] = max(DP[i+1][r][c+1], DP[i][r][c] + item[r][c])

    ans = DP[3][R-1][C-1]
    for i in range(3): ans = max(ans, DP[i][R-1][C-1] + item[R-1][C-1])
    print(ans)
    return 0

if __name__ == "__main__":
    solve()
