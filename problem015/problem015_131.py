#!/usr/bin/env python
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    N = int(raw_input())
    l = map(int, raw_input().split())
    cnt = 0
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if l[j] < l[minj]:
                minj = j
        if i != minj:
            l[i], l[minj] = l[minj], l[i]
            cnt += 1
    print ' '.join(map(str, l))
    print cnt
