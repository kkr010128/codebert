# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 01:24:25 2020

@author: saito
"""

# %% import phase

# %% define phase

# %% input phase
N = int(input())

# %% process phase
answer = 1000-((N-1)%1000+1)

# %%output phase
print(answer)