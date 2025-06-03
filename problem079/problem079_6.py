MOD = 1000000007


S = int(input())

#dp[i]:=i桁の数列で条件を満たすものの数
dp = [0]*(S+1)
dp_sum = [0]*(S+1)

for i in range(3,S+1):
    #dp[i]=sum(dp[0],..,dp[i-3])+1
    
    dp[i] = (dp_sum[i-3]+1)%MOD
    dp_sum[i] = (dp[i]+dp_sum[i-1])%MOD

print(dp[S])