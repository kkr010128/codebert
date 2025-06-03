#!/usr/bin python3
# -*- coding: utf-8 -*-

#######################################################################
# ナップサック
# 重さ：Wー10**5くらい
# 価値：N*max_Viー10**11くらい
# dp[w]:wの重さで可能な最大の価値
#   dp[w]とdp[w-wi]+vi(i番目のアイテムをとる場合)との大きいほうで更新
#######################################################################

n, t = map(int, input().split())
dp = [0] * (t+1)
itm = [list(map(int, input().split())) for _ in range(n)]
itm.sort()
for w_ , v_ in itm:
    for i in range(1,t+1):
        dp[max(0,i-w_)] = max(dp[max(0,i-w_)], dp[i] + v_)
print(dp[0])
