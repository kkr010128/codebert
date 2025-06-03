import sys
input = sys.stdin.readline
import numpy as np
from collections import defaultdict

N,K = map(int,input().split())
# 全要素を-1する
A = [0] + [int(i)-1 for i in input().split()]

# Acum[i]: A[1]からA[i]までの累積和
Acum = np.cumsum(A)
Acum = [i%K for i in Acum]

answer = 0
counter = defaultdict(int)

# iの範囲で探索
# 1 <= j <= N
# j-K+1 <= i <= j-1
for j,x in enumerate(Acum):
    # (i-K+1)回目から(i-1)回目の探索において、xの出現回数
    answer += counter[x]
    # i回目の結果を辞書に追加
    counter[x] += 1
    # 辞書にK回追加した場合
    if j-K+1 >= 0:
        # 辞書から一番古い探索記録を削除
        counter[Acum[j-K+1]] -= 1

print(answer)