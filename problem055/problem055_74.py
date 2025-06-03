# -*- coding: utf-8 -*-

import sys
import os


def get_house():
    return [[0 for i in range(10)] for j in range(3)]

def print_house(h):
    for i in range(3):
        for j in range(10):
            print(' ', end='')
            print(h[i][j], end='')
        print()

houses = []
for i in range(4):
    houses.append(get_house())

N = int(input())
for i in range(N):
    b, f, r, v = list(map(int, input().split()))
    houses[b-1][f-1][r-1] += v

for i in range(4):
    print_house(houses[i])
    if i != 3:
        print('####################')