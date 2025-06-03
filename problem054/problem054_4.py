#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
??´?????????
"""

suits = {"S": 0, "H": 1, "C": 2, "D": 3}
nsuits = ["S", "H", "C", "D"]

cards = [[0 for i in range(13)] for j in range(4)]
n = int(input())

for i in range(n):
    inp = input().split(" ")
    s = inp[0]
    c = int(inp[1]) - 1
    cards[suits[s]][c] = 1

for i in range(4):
    for j in range(13):
        if cards[i][j] == 0:
            print("{0} {1}".format(nsuits[i], j+1))