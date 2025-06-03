# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: print('Yes' if b else 'No')
YESNO=lambda b: print('YES' if b else 'NO')

def main():
    N,M=map(int,input().split())
    c=list(map(int,input().split()))
    dp=[[INF]*10**6 for _ in range(M+1)]
    dp[0][0]=0
    ans=INF
    for i in range(M):
        for money in range(N+1):
            dp[i+1][money]=min(dp[i+1][money],dp[i][money])
            if money-c[i]>=0:
                dp[i+1][money]=min(dp[i+1][money],dp[i][money-c[i]]+1,dp[i+1][money-c[i]]+1)
    print(dp[M][N])

if __name__ == '__main__':
    main()

