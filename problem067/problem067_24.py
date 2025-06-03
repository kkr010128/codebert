# -*- coding: utf-8 -*-

import sys
import os


N = int(input())
score0 = 0
score1 = 0
for i in range(N):
    word0, word1 = input().split()
    if word0 < word1:
        score1 += 3
    elif word0 > word1:
        score0 += 3
    else:
        score0 += 1
        score1 += 1
print(score0, score1)