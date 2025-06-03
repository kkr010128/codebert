"""
dp[i][j][k] => i行目j列到達時点での最大価値。i行目において拾えるアイテムの数はK個。
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

            #上から入るパターン
            dp[j][0] = max(dp[j])
            if v:
                dp[j][1] = dp[j][0]+v
            
            #左から入ってくるパターン
            if j > 0:
                for k in range(4):
                    #このマスのアイテムをとらないパターン
                    dp[j][k] = max(dp[j][k],dp[j-1][k])
                    if v and k>0:
                        dp[j][k] = max(dp[j][k],dp[j-1][k-1]+v)

    print(max(dp[-1]))
main()