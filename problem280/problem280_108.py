# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 02:04:12 2020

@author: liang
"""
import math

N = int(input())
d = list()
for i in range(N):
    x, y = map(int,input().split())
    d.append((x,y))
#print(d)
lis = list(range(N))
num = list()
perm_list = list()

def make_perm():
    if len(num) == N:
        perm_list.append(num.copy())
    for n in lis:
        a = lis.pop(0)
        num.append(a)
        make_perm()
        num.pop()
        lis.append(a)
        
make_perm()
#print(len(perm_list))
res = 0
for nums in perm_list:
    tmp = 0
    for i in range(N-1):
        tmp += math.sqrt((d[nums[i]][0]-d[nums[i+1]][0])**2 + (d[nums[i]][1] - d[nums[i+1]][1])**2)
    res += tmp
print(res/len(perm_list))