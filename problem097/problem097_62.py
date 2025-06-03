# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 01:25:53 2020

@author: saito
"""

# %% import phase
#from collections import deque

# %% define phase


# %% input phase
K = int(input())

# %% process phase
r = 0
answer = -1
h = []

for cnt in range(K):
    r = (10*r+7) % K
    if r == 0:
        answer = cnt + 1
        break

# %%output phase
print(answer)