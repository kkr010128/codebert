"""
dp[i][j][k] => i行目、j列のマスまで見る。k個取る時の最高値。
"""
def main():
    import sys
    input = sys.stdin.readline
    R,C,K = map(int,input().split())
    items = [[0]*C for _ in range(R)]
    for _ in range(K):
        r,c,v = map(int,input().split())
        items[r-1][c-1] = v

    dp = [[0]*4 for _ in range(C)]

    for i in range(R):
        for j in range(C):
            v = items[i][j]
            if i == 0 and j == 0 and v != 0:
                dp[j][1] = v
                continue
            
            if i != 0:
                #上から降りてくる場合の価値を求める
                #i行目j列のアイテムを取らない場合
                dp[j][0] = max(dp[j])
                #i行目j列のアイテムを取る場合
                if v!=0:
                    dp[j][1] = dp[j][0] + v

            #左から入ってくる場合の価値を求める
            if j != 0:
                dp[j][0] = max(dp[j][0],dp[j-1][0])
                if v == 0:
                    for k in range(1,4):
                        dp[j][k] = max(dp[j][k],dp[j-1][k])
                else:
                    for k in range(1,4):
                        dp[j][k] = max(dp[j][k],dp[j-1][k],dp[j-1][k-1]+v)
    print(max(dp[-1]))
main()