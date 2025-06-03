import sys
import math

n, k = map(int, sys.stdin.readline().split())

W = []
for _ in range(n):
    w = int(sys.stdin.readline())
    W.append(w)

r = sum(W)
l = max(W)
pre_p = 0


while l < r:

    current = 0
    num_tracks = 1

    p = (l + r) // 2  # 値を設定

    # 積み込めるか確認
    for w in W:
        if current + w > p:
            num_tracks += 1  # 次のトラックを持ってくる
            current = w
        else:
            current += w
    
    if num_tracks > k:  # 現在の p ではトラックが足りない場合
        l = p + 1  # 最少値を上げる
    else:
        r = p  # 最大値を下げる


print(l)
