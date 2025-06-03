# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
R,C,K=map(int, sys.stdin.readline().split())

value=defaultdict(lambda: 0)
value=[ [0 for _ in range(C+1)] for __ in range(R+1) ]
for _ in range(K):
    r,c,v=map(int, sys.stdin.readline().split())
    value[r][c]=v

dp0=[0]*(C+1)
dp1=[0]*(C+1)
dp2=[0]*(C+1)
dp3=[0]*(C+1)

for r in range(1,R+1):
    for c in range(1,C+1):
        #今のマスにアイテムがある場合
        if 0<value[r][c]:
            dp3[c]=max( dp3[c-1], dp2[c-1]+value[r][c] )
            dp2[c]=max( dp2[c-1], dp1[c-1]+value[r][c] )
            #dp1[c]=max( dp1[c-1], dp0[c-1]+value[r][c], dp0[c]+value[r][c] )
            dp1[c]=max( dp1[c-1], dp0[c]+value[r][c] )
            #dp0[c]=max( dp0[c-1], dp0[c] )
            dp0[c]=dp0[c]
        #今のマスにアイテムがない場合
        else:
            #dp0[c]=max( dp0[c-1], dp0[c] )
            #dp1[c]=max( dp1[c-1], dp1[c] )
            #dp2[c]=max( dp2[c-1], dp2[c] )
            #dp3[c]=max( dp3[c-1], dp3[c] )
            dp0[c]=dp0[c]
            dp1[c]=dp1[c-1]
            dp2[c]=dp2[c-1]
            dp3[c]=dp3[c-1]

    #上の行にアイテムをコピー
    for c in range(1,C+1):
        dp0[c]=max( dp0[c], dp1[c], dp2[c], dp3[c] )
    dp1=[0]*(C+1)
    dp2=[0]*(C+1)
    dp3=[0]*(C+1)

print dp0[C]
