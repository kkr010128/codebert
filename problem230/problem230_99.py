import sys
import math
import fractions
import bisect
import queue
import heapq
from collections import deque
sys.setrecursionlimit(4100000)

MOD = int(1e9+7)
PI = 3.14159265358979323846264338327950288
INF = 1e18

'''
1行のint
N, K = map(int, input().split())

1行のstring
S, T = input().split()

1行の整数配列
P = list(map(int,input().split()))

改行あり
x = []
y = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)

N行M列の初期化
dp = [[INF] * M for i in range(N)]

'''

N, D, A = map(int, input().split())
XH = []

for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    XH.append([x1, y1])

    
def counting(hp):
    if hp < 0:
        return 0
    return hp//A + int(hp%A!=0)

XH.sort()


bombs = deque([]) # 有効な爆弾の威力と範囲を保存する
power = 0 # 有効な爆弾の威力の合計

ans = 0
for i in range(N):
    
    # 使えない爆弾を捨てる
    while len(bombs)>0 and bombs[0][0] < XH[i][0]:
        power -= bombs.popleft()[1]

    # パワーの不足分の爆弾
    add = counting(XH[i][1]-power) 
    ans += add
    
    # 追加した爆弾をキューに加える
    bombs.append((XH[i][0] + 2*D, add*A))
    power += add*A


print(ans)









"""
ATTENTION: Pythonで間に合うか？？

            <目安>
 文字列結合、再帰関数を含む→Python
 上を含まず時間が不安→PyPy3

"""