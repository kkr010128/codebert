N,K =  map(int,input().split())
RST = list(map(int,input().split()))
#r:0 s:1 p:2
# a mod K != b mod Kならばaとbは独立に選ぶことができる。
# よってN個の手をmod KによるK個のグループに分け、各グループにおける最大値を求め、最終的にK個のグループの和が答え
T = [0 if i=="r" else 1 if i=="s" else 2 for i in input()]

dp = [[0]*3 for i in range(N)]

#直後の手を見て決める
for i in range(N):
    if i<K:
        for j in range(3):
            # j:1,2,0
            # j==0 -> RST[0]
            #初期値は勝つ手を出し続ける
            if (j+1)%3==T[i]:
                dp[i][j]=RST[j]
    else:
        #現在の出す手
        for j in range(3):
            #K回前に出した手
            for l in range(3):
                if j!=l:
                    if (j+1)%3 == T[i]:
                        dp[i][j] = max(dp[i][j],RST[j]+dp[i-K][l])
                    else:
                        dp[i][j] = max(dp[i][j],dp[i-K][l])

ans = 0
for i in range(N-K,N):
    ans += max(dp[i])

print(ans)