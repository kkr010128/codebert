# -*- coding: utf-8 -*-
# モジュールのインポート
import math
import itertools

# 標準入力を取得
N = int(input())
x, y = [], []
for n in range(N):
    x_n, y_n = list(map(int, input().split()))
    x.append(x_n)
    y.append(y_n)

# 求解処理
def get_distance(i: int, j: int) -> float:
    return math.sqrt(math.pow(x[i] - x[j], 2) + math.pow(y[i] - y[j], 2))

ans = 0
for path in itertools.permutations(range(N), N):
    distance = 0
    for i in range(N - 1):
        distance += get_distance(path[i], path[i + 1])
    ans += distance
ans /= math.factorial(N)

# 結果出力
print(ans)