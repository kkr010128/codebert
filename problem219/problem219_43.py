S=input()
INF=10**12
# dp[i][j]: 下からi桁目まで決めた時の、くりさがりがjの時の最小値
# i: 0~N, j:2値, 前の桁でくりさがりが発生している場合に1
dp=[[INF for _ in range(2)] for _ in range(10**6+5)]
S=S[::-1]
S+="0"
N=len(S)
dp[0][0]=0
# 配るDP, 今の状態を見て次の状態を決めていく
for i in range(N):
    for j in range(2):
        # x: i桁目の数字, 前の桁でくりさがりが発生している場合はインクリメント
        x=int(S[i])
        x+=j
        for a in range(10):
            ni=i+1
            nj=0
            b=a-x
            if b<0:
                nj=1
                b+=10
            dp[ni][nj]=min(dp[ni][nj], dp[i][j]+a+b)
print(dp[N][0])