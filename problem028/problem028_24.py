# dp[i][j](各マスの値) = i-1番目の品物の中からj円を支払うときの最小枚数
#  → 個数制限なし   
# <DP初期状態>
#   i\j  0   1   2    3   ...  n (お金(yen))
#   0    0  INF INF  INF  ... INF
#   1    0  INF INF  INF  ... INF
#                 ...
#   m-1  0  INF INF  INF  ... INF
#   m    0  INF INF  INF  ... INF
#  (i番目のコイン)
#
# <DP遷移式>
# if(j >= c_i):  c[i]のコイン採用可
#    dp[i+1] = min(dp[i][j-c[i]]+1     : c[i]を採用する(コイン枚数:1枚増える)
#                , dp[i][j])           : c[i]を採用しない
#                , dp[i+1][j-c[i]]+1)  : c[i]を重複を許して採用
# elif(j < c_j): money[i]のコイン採用不可
#    dp[i+1][j] = dp[i][j]              : c[i]を採用しない
 
n,m = map(int,input().split())
c = list(map(int,input().split()))
 
# DP配列の初期化    
dp = []
for i in range(m+100):
    tmp = [0]
    for j in range(n+99): tmp.append(float('inf'))
    dp.append(tmp)
    
# DP遷移    
for i in range(m):
  #print_dp(dp,i)  
  for j in range(n+1):
    if(j>=c[i]): # i番目のコイン採用可
      dp[i+1][j] = min(dp[i][j-c[i]]+1, 
                       dp[i][j],
                       dp[i+1][j-c[i]]+1)  
    else: # i番目のコイン採用不可
      dp[i+1][j] = dp[i][j]

#print_dp(dp,i+1)    
# 出力
print(dp[m][n])
