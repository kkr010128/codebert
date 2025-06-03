# -*- coding: utf-8 -*-
# 標準入力を取得
L, R, d = list(map(int, input().split()))

# 求解処理
ans = R // d - (L - 1) // d

# 結果出力
print(ans)
