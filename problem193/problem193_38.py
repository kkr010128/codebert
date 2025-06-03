# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

H,W,K=map(int, sys.stdin.readline().split())
S=[ sys.stdin.readline().strip() for _ in range(H) ]
#print H,W,K
#print S

ans=float("inf")
for bit in range(2**H):
    cnt=0
    group_num=0
    GROUP={}
    for i,s in enumerate(S):
        if i==0:
            GROUP[i]=group_num
        else:
            if bit>>i-1&1==1:
                cnt+=1      #境目のカウントに+1
                group_num+=1
            GROUP[i]=group_num
    #print "GROUP :: ",GROUP

    ok=None
    VALUE=defaultdict(lambda: 0)
    w=0
    for w in range(W):
        for h in range(H):
            VALUE[GROUP[h]]+=int(S[h][w])
        #現在の値がKを超えていないか
        for v in VALUE.values():
            if v<=K:
                pass
            else:
                #print "NG!",w
                if ok is None:      #okに値がない場合は、このパターンは成り立たない
                    #print "IMPOSSIBLE!"
                    cnt=float("inf")    #不可能なパターンなのでカウントに無限大を代入
                else:      #以前の列で成り立たっていた場合
                    cnt+=1      #境目のカウントに+1
                    VALUE=defaultdict(lambda: 0)    #NGの場合は値を初期化して入れなおし
                    for h in range(H):
                        VALUE[GROUP[h]]+=int(S[h][w])
                    break
        else:
            ok=w
    #print "w,ok,cnt,VALUE :: ",w,ok,cnt,VALUE
    ans=min(ans,cnt)
       
print ans