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

# v 回目のじゃんけん
for v in range(1,N+1):
    # v 回目に出した手
    for w in range(3):
        # v-K 回目に出した手 
        for k in range(3):
            if w == k:
                continue
            # じゃんけんで勝ったとき
            if judge(T[v-1],w):
                dp[v][w] = max(dp[v][w],dp[v-K][k] + RSP[w])
            # じゃんけんで負けか引き分けたとき
            else:
                dp[v][w] = max(dp[v][w],dp[v-K][k])         
# K 個に分けた各グループの部分和の最大値の総和を求める
ans = 0
for a in range(1,K+1):
    ans += max(dp[-a])
print(ans)