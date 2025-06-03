# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N=int(input())
    A=list(map(int,input().split()))
    B=[(A[i],i) for i in range(N)]
    B.sort(key=lambda t: -t[0])
    dp=[[0]*(N+1) for _ in range(N+1)]
    ans=0
    for i in range(N):
        for x in range(i+1):
            y=i-x
            dp[x+1][y]=max(dp[x+1][y],dp[x][y]+B[i][0]*abs(B[i][1]-x))
            dp[x][y+1]=max(dp[x][y+1],dp[x][y]+B[i][0]*abs(N-1-y-B[i][1]))
            ans=max(ans,dp[x+1][y],dp[x][y+1])
    print(ans)

if __name__ == '__main__':
    main()
