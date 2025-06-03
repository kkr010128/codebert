MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)           

def main():
    n = int(input())
    a = list(enumerate(map(int,input().split())))
    a.sort(key = lambda x:x[1],reverse = True)

    dp = [[0] * (n + 1) for _ in range(1 + n)]
    for i in range(n + 1):
        for j in range(i + 1,n):
            dp[i][j] = -INF

    for j in range(n):
        i,num = a[j]
        i += 1
        for k in range(j + 2):
            if k == 0:
                dp[j + 1][k] = dp[j][k] + num * abs(i - n + j - k)
            else:
                dp[j + 1][k] = max(dp[j][k - 1] + num * abs(i - k),dp[j][k] + num * abs(i - n + j - k))
            
    print(max(dp[-1]))
if __name__ =='__main__':
    main()  