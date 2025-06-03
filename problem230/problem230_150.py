# -*- coding: utf-8 -*-
import sys
from collections import deque

N,D,A=map(int, sys.stdin.readline().split())
XH=[ map(int, sys.stdin.readline().split()) for _ in range(N) ]
XH.sort()

q=deque()   #（攻撃が無効となる座標、攻撃によるポイント）
ans=0
cnt=0

attack_point=0
for x,h in XH:
    while q:
        if x<q[0][0]:break  #無効となる攻撃がない場合はwhileを終了
        end_x,end_point=q.popleft()
        attack_point-=end_point #攻撃が無効となる座標<=現在の座標があれば、その攻撃のポイントを引く

    if h<=attack_point: #モンスターの体力よりも攻撃で減らせるポイントの方が大きければ新規攻撃は不要
        pass
    else:   #新規攻撃が必要な場合
        if h%A==0:
            cnt=(h-attack_point)/A  #モンスターの大量をゼロ以下にするために何回攻撃が必要か
        else:
            cnt=(h-attack_point)/A+1
        attack_point+=cnt*A
        q.append((x+2*D+1,cnt*A))   #（攻撃が無効となる座標、攻撃によるポイント）をキューに入れる
        ans+=cnt

print ans