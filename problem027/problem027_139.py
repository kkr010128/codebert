from math import sqrt
from functools import reduce

N = int(input())

def koch(p1, p2, n):
	if n == 0:
		return [p1, p2]
	else:
		c1 = [(2*p1[0] + p2[0])/3, (2*p1[1] + p2[1])/3]
		c3 = [(p1[0] + 2*p2[0])/3, (p1[1] + 2*p2[1])/3]
		c2 = [(p1[0] + p2[0]) / 2 + 1/sqrt(3) * (p1[1] - p2[1])/2, (p1[1] + p2[1]) / 2 + 1/sqrt(3) * (p2[0] - p1[0])/2]
		return koch(p1, c1, n-1)[:-1] + koch(c1, c2, n-1)[:-1] + koch(c2, c3, n-1)[:-1] + koch(c3, p2, n-1)


for p in koch([0.0, 0.0], [100.0, 0.0], N):
	print('{:.6f} {:.6f}'.format(p[0], p[1]))

