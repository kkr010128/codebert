# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:55:33 2020

@author: Kanaru Sato
"""

a = list(map(int, input().split()))

if sum(a) >= 22:
    print("bust")
else:
    print("win")