# D - Prediction and Restriction 
N,K = map(int,input().split())
RSP = tuple(map(int,input().split()))
T = input()

# じゃんけんの勝敗を返す関数
def judge(a,b):
    if a == 'r' and b == 2:
        return True
    elif a == 's' and b == 0:
        return True
    elif a == 'p' and b == 1:
        return True
    return False

# dp[i][j]: i 回目のじゃんけんで j を出したときの最大値
# グー:0, チョキ:1, パー:2
dp = [[0]*3 for _ in range(N+1)]

# 初期条件 v < K のときは全て勝つ
for i in range(1,K+1):
    for j in range(3):
        if judge(T[i-1],j):
            dp[i][j] = RSP[j]

# K 以下の数字について
for v in range(1,K+1):
    # w = v, v+K, v+2K,...
    for w in range(v+K,N+1,K):
        # w 回目に出した手
        for l in range(3):
            # w-K 回目に出した手 
            for m in range(3):
                if l == m:
                    continue
                # じゃんけんで勝ったとき
                if judge(T[w-1],l):
                    if w-K>=0:
                        dp[w][l] = max(dp[w][l],dp[w-K][m] + RSP[l])
                # じゃんけんで負けか引き分けたとき
                dp[w][l] = max(dp[w][l],dp[w-K][m])
                     
# K 個に分けた各グループの部分和の最大値の総和を求める
ans = 0
for a in range(1,K+1):
    ans += max(dp[-a])
print(ans)