# coding: utf-8
# Your code here!
N=int(input())
A=list(map(int,input().split()))

dp=[[[0,1000],[0,1000]] for i in range(N+1)]


def wa(lis,a):
    return lis[0]*a+lis[1]

for i in range(N):
    #0が株売り　1が株買い
    dp[i+1][0]=dp[i][0] if wa(dp[i][0],A[i])>=wa(dp[i][1],A[i]) else [0,dp[i][1][0]*A[i]+dp[i][1][1]]
    #株が多くなるように買う
    dp[i+1][1]=dp[i][1] if wa(dp[i][1],A[i])>wa(dp[i][0],A[i]) else [dp[i][0][1]//A[i],dp[i][0][1]-dp[i][0][1]//A[i]*A[i]]
    
    
print(dp[-1][0][-1])
