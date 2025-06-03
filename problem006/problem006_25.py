# coding: utf-8

import math

n = int(raw_input())

ans = 100000
for i in range(n):
	ans = ans * 1.05
	q = math.ceil(ans / 1000)
	ans = q * 1000
print int(ans)