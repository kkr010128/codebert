import sys
input = sys.stdin.readline

H,W = list(map(int,input().split()))
S = [ input().rstrip() for _ in range(H)] #マップの読み込み
dp = [[float('inf')]*W for _ in range(H)] #コスト
if S[0][0] == '#':#はじめが'#'なら1,else 0
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:#スタート地点は無視
            continue
        a = float('inf')
        b = float('inf')
        # S[i][j]にくるには i-1 かj-1からくるしかない
        if i >= 1:
            a = dp[i-1][j] + ( S[i-1][j] =='.' and S[i][j] =='#') #i-1からくる
        
        if j >= j:
            b=  dp[i][j-1] + ( S[i][j-1] =='.' and S[i][j] =='#') #j-1からくる

        dp[i][j] = min(a,b)#a,bの小さいほうが最小コスト
print(dp[i][j])
