
"""
Writer: SPD_9X2
https://atcoder.jp/contests/abc163/tasks/abc163_e

dpか？
なにを基準にdpすればよい？
まとめられる状態は？
小さいことを考えると貪欲かなぁ
かいてみるか

挿入dp?
前から決めていけば、累積和で減る量がわかる
&増える寄与も計算できる
O(N**2)

全探索はむり

======答えを見ました======
今より右に行く、左に行くの集合に分けたとすると
大きい奴をより左にする方が最適
よって、途中まで単調減少、途中から単調増加が最適であるとわかる

dp[大きい方からi番目まで見た][左にl個つめた] = 最大値
で解ける

"""


N = int(input())

A = list(map(int,input().split()))
ai = []
for i in range(N):
    ai.append([A[i],i])
ai.sort()
ai.reverse()

ans = 0

dp = [ [float("-inf")] * (N+1) for i in range(N+1) ]
dp[0][0] = 0

for i in range(N):

    na,nind = ai[i]

    for l in range(i+1):

        r = N-1-(i-l)
        dp[i+1][l+1] = max(dp[i+1][l+1] , dp[i][l] + na*abs(nind-l) )
        dp[i+1][l]   = max(dp[i+1][l] , dp[i][l] + na*abs(nind-r) )

print (max(dp[N]))
