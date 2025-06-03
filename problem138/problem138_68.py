n,s=map(int,input().split())
a=list(map(int,input().split()))

#dp[n][s]
#nこめまで選んだ時の和がｓの組

dp=[[0]*(s+1) for _ in range(n)]
a.sort()
#for i in range(s+1):
#    dp[0][i]=2
if a[0]>s:
    print(0)
    exit()

mod=998244353
 

dp[0][0]=2
dp[0][a[0]]+=1

for i in range(1,n):
    for j in range(s+1):
        #i番目を入れて選択するパターン
        dp[i][j]=dp[i-1][j]*2%mod
        if j>=a[i]:
            dp[i][j]+=dp[i-1][j-a[i]]%mod

print(dp[-1][s]%mod)


    

    


