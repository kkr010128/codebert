# coding: UTF-8
import sys
import numpy as np

# f = open("input.txt", "r")
# sys.stdin = f

s = str(input())
t = str(input())
ans = 0
for i, j in zip(s,t):
	if i != j:
		ans += 1

print(ans)
