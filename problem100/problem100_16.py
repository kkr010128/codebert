#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

sys.setrecursionlimit(10000)

R = int(input())

res = -1
if R <= 599:
   res = 8
elif R <= 799:
   res = 7
elif R <= 999:
   res = 6
elif R <= 1199:
   res = 5
elif R <= 1399:
   res = 4
elif R <= 1599:
   res = 3
elif R <= 1799:
   res = 2
elif R <= 1999:
   res = 1

   
print(res)
