# -*- coding: utf-8 -*-
# モジュールのインポート
import itertools

# 標準入力を取得
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

# 求解処理
p = 0
q = 0
order = 1
for t in itertools.permutations(range(1, N + 1), N):
    if t == P:
        p = order
    if t == Q:
        q = order
    order += 1

ans = abs(p - q)

# 結果出力
print(ans)
