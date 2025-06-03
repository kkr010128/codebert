# -*- coding: utf-8 -*-
 
import math
import itertools
import sys
import copy
 
# 入力
#A, B, C, D = map(int, input().split())
#L = list(map(int, input().split()))
#S = list(str(input()))
#N = int(input())
X, Y = map(int, input().split())

sum = 0
if X == 1 :
  sum += 300000
elif X == 2 :
  sum += 200000
elif X == 3 :
  sum += 100000

if Y == 1 :
  sum += 300000
elif Y == 2 :
  sum += 200000
elif Y == 3 :
  sum += 100000

if X == 1 and Y == 1 :
  sum += 400000
  
print (sum)
