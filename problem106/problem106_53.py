# -*- coding: utf-8 -*-
# モジュールのインポート
import math
import itertools

# 標準入力を取得
N = int(input())

# メイン処理


def g(x: int, y: int, z: int) -> int:
    return x**2 + y**2 + z**2 + x*y + y*z + z*x


l = [0 for n in range(N)]
for x, y, z in itertools.product(range(1, int(math.sqrt(N)) + 1), repeat=3):
    v = g(x, y, z)
    if v <= N:
        l[v - 1] += 1

# 結果出力
for ans in l:
    print(ans)
