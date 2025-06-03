# -*- coding: utf-8 -*-
# モジュールのインポート
import numpy as np

# 標準入力を取得
D = int(input())
c = list(map(int, input().split()))
s = []
for d in range(D):
    s_d = list(map(int, input().split()))
    s.append(s_d)
t = []
for d in range(D):
    t_d = int(input())
    t.append(t_d)

c = np.array(c)
s = np.array(s)
t = np.array(t)

# 求解処理
KIND = 26
last = np.array([0 for i in range(KIND)])
S = 0
for d in range(1, D + 1):
    S += s[d - 1][t[d - 1] - 1]
    last[t[d - 1] - 1] = d
    S -= sum(c * (d - last))
    print(S)
