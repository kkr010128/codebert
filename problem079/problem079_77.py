# dp[i][j]:=(総和がiで長さがjの数列の個数)とする
# このままだとO(s^3)だが、全てのｊに対してΣ(k=0→i-3)dp[k][j]をあらかじめ持っておけばO(s^2)となる
# dpの遷移式立てたときはちゃんと紙に書いて眺めなきゃ（使命感）
s=int(input())
mod=10**9+7
dp=[[0]*(s+1) for _ in range(s+1)]
accum=[0]*(s+1)
dp[0][0]=1
for i in range(3,s+1):
    for j in range(s):
        accum[j]+=dp[i-3][j]
        dp[i][j+1]+=accum[j]
        dp[i][j+1]%=mod
print(sum(dp[s])%mod)