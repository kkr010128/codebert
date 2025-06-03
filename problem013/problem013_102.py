# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 18:45:04 2017

@author: syaga
"""

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max = a[1] - a[0]
    mini = a[0]
    for i in range(1, len(a)):
        diff = a[i] - mini
        if diff > max:
            max = diff
        if mini > a[i]:
            mini = a[i]
    print(max)