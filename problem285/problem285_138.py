#!/usr/bin/python3
#coding: utf-8

S = input()
ret = 0

# 山を下る
i = 0
while i < len(S) and S[i] == ">":
    i += 1
    ret += i

# 山を登って降りる
n_up = 0
n_down = 0
while i < len(S):
    n_up = 0
    n_down = 0
    while i < len(S) and S[i] == "<":
        n_up += 1
        i += 1
        if i >= len(S):
            break
    while i < len(S) and S[i] == ">":
        n_down += 1
        i += 1
        if i >= len(S):
            break
    if n_up < n_down:
        n_up, n_down = n_down, n_up

    ret += ((n_up+1) * n_up) // 2
    ret += (n_down * (n_down-1)) // 2
    
print(ret)