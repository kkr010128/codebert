import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

if __file__=="test.py":
    f = open("./in_out/input.txt", "r", encoding="utf-8")
    read = f.read
    readline = f.readline

def main():
    R, C, K = map(int, readline().split())
    
    L_INF = int(1e17)
    dp = [[[-L_INF for _ in range(C+1)] for _ in range(R+1)] for _ in range(4)]
    cell = [[0 for _ in range(C+1)] for _ in range(R+1)]
    
    for i in range(K):
        x, y, c = map(int, readline().split())
        cell[x-1][y-1] = c
    
    dp[0][0][1] = dp[0][1][0] = 0
    
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            for k in range(4):
                if k > 0:
                    dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j])
                dp[k][i][j] = max(dp[k][i][j], dp[k][i][j-1])
                if k > 0:
                    dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j-1] + cell[i-1][j-1])
                if k == 1:
                    dp[1][i][j] = max(dp[1][i][j], dp[3][i-1][j] + cell[i-1][j-1])
 
    print(dp[3][R][C])

if __name__ == "__main__":
    main()
