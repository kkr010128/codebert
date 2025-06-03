#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    X,Y=pin()
    t=10**5
    a=[0,t*3,t*2,t*1]+[0]*1000
    print(a[X]+a[Y]+4*t*(X==Y and X==1))
#%%submit!
resolve()
