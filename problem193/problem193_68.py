"""

制約の小ささから見て全探索

"""

from itertools import product, accumulate
from bisect import *
import sys
input = sys.stdin.readline

H, W, K = map(int, input().split())
S = []
T = []
for i in range(H):
    S.append(list(map(int, input().strip())))
    T.append(list(accumulate([0] + S[-1])))

cnt_list = []
for a in product((0,1),repeat=H):
    past_a = a[0]
    T2 = [[0]*(W+1)]
    for i in range(H):
        if a[i] == past_a:
            for j, t in enumerate(T[i]):
                T2[-1][j] += t
        else:
            T2.append(T[i].copy())
        past_a = a[i]
    cnt = len(T2) - 1
    l = 0
    flg = False
    while True:
        temp = []
        for s in T2:
            temp.append(bisect_right(s[l+1:], K + s[l]) + l)
        if min(temp) == 0:
            flg = True
            break
        else:
            l = min(temp)
        if l >= W:
            break
        else:
            cnt += 1
    if not flg:
        cnt_list.append(cnt)

print(min(cnt_list))

