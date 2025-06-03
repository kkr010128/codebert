# -*- coding: utf-8 -*-
r, c = map(int, raw_input().split())
cl= [0] * c
for i in xrange(r):
	t = map(int, raw_input().split())
	for i, a in enumerate(t): cl[i] += a
	print ' '.join(map(str, t)), sum(t)
print ' '.join(map(str, cl)), sum(cl)