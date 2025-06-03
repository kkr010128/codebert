import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    R,C,K = LI()

    m = [[0] * (C+1) for _ in range(R+1)]
    dp = [[0] * 4 for _ in range(C+1)]
    for _ in range(K):
        r,c,v = LI()
        m[r][c] = v

    for i in range(1,R+1):
        for j in range(1,C+1):
            b_max = max(dp[j])
            dp[j][0] = max(dp[j-1][0],b_max)
            if m[i][j] > 0:
                for k in range(1,4):
                    dp[j][k] = max(dp[j-1][k],dp[j-1][k-1]+m[i][j])
                dp[j][1] = max(dp[j][1],b_max+m[i][j])
            else:
                for k in range(1,4):
                    dp[j][k] = dp[j-1][k]
    print(max(dp[-1]))

if __name__ == '__main__':
    main()