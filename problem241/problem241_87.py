from collections import deque 
from copy import deepcopy
# 初期入力
import sys
input = sys.stdin.readline
H,W = (int(i) for i in input().split())
map_initial =[["#"]*(W+2) for i in range(H+2)] #周囲を壁にするため＋２
for h in range(1,H+1):
    map_initial[h] =["#"] +list(input().strip()) +["#"]

def BSF(x,y):
    dist =0
    map =deepcopy(map_initial)
    if map[x][y] =="#":
        return dist 
    dq =set()
    dq.add((x,y))
    dq_sarch =set()
    while len(dq) >0:
        h,w =dq.pop()
        map[h][w] ="#" #通り済を壁にする
        if map[h+1][w]==".":
            dq_sarch.add((h+1,w))
        if map[h-1][w]==".":
            dq_sarch.add((h-1,w))
        if map[h][w+1]==".":
            dq_sarch.add((h,w+1))
        if map[h][w-1]==".":
            dq_sarch.add((h,w-1))
        if len(dq)==0:
            dq =deepcopy(dq_sarch)
            dq_sarch.clear()
            dist +=1
        #print(h,w,dist,end="\t")
    return dist-1

#スタート位置を全探索し、最長距離を探す
dist_all =[]
for i in range(1,H+1):
    for j in range(1,W+1):
        dist_all.append(BSF(i,j) )
print(max(dist_all))