# -*- coding: utf-8 -*-
import sys
from collections import deque,defaultdict
sys.setrecursionlimit(10**5)

H,W,K=map(int, sys.stdin.readline().split())
ichigo=[]
cnt=0   #イチゴに番号を振るための変数
h_visit=[0 for h in range(H)]  #縦軸にイチゴがない箇所は0、ある箇所は1

L=[ [] for h in range(H) ]
for h in range(H):
    s=sys.stdin.readline().strip()
    for w,x in enumerate(s):
        if x==".":
            L[h].append(0)
        elif x=="#":
            cnt+=1
            L[h].append(cnt)
            ichigo.append((h,w))
            h_visit[h]=1

D=(1,-1)    #マスの横移動、または縦移動に使用

def yoko_dfs(h,w):  #縦座標、横座標
    for dw in D:
        if 0<=w+dw<=W-1 and L[h][w+dw]==0:
            L[h][w+dw]=L[h][w]
            yoko_dfs(h,w+dw)
    return

#横方向に空マスなら、自分のイチゴ番号で埋めていく
for h,w in ichigo:
    yoko_dfs(h,w)

def tate_dfs(h):  #縦座標
    for dh in D:
        if 0<=h+dh<=H-1:
            if h_visit[h+dh]==1: continue
            h_visit[h+dh]=1 #訪問済みにする
            L[h+dh]=L[h]    #行のコピー
            tate_dfs(h+dh)

#縦方向にdfs。イチゴがない行を探して、イチゴがある行を行ごとコピーする
for h,w in ichigo:
    tate_dfs(h)

for l in L:
    for x in l:
        print x,
    print