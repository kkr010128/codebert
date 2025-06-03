#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    L,R,d=pin()
    cnt=0
    for i in range(L,R+1):
        if i%d==0:cnt+=1

    print(cnt)
#%%submit!
resolve()
