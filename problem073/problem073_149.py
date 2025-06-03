
#!/usr/bin/python
# -*- coding: utf-8 -*-

# def
def int_mtx(N):
    x = []
    for _ in range(N):
        x.append(list(map(int,input().split())))
    return np.array(x)

def str_mtx(N):
    x = []
    for _ in range(N):
        x.append(list(input()))
    return np.array(x)

def int_map():
    return map(int,input().split())

def int_list():
    return list(map(int,input().split()))

def print_space(l):
    return print(" ".join([str(x) for x in l]))

# import
import numpy as np
import collections as col

N = int(input())

ans = 0

for i in range(1,N):
    if N%i != 0:
        ans += N//i
    else:
        ans += N//i -1

print(ans)



