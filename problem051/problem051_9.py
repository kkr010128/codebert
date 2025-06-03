# -*- coding: utf-8 -*-
import sys
point = '.'
sharp = '#'

while True:
	H, W = map(int, raw_input().split())
	if H == W == 0:
		break
	for h in xrange(H):
		for w in xrange(W):
			if h % 2 == 0:
				if w % 2 == 0:
					sys.stdout.write(sharp),
				else:
					sys.stdout.write(point),
			else:
				if w % 2 == 0:
					sys.stdout.write(point)
				else:
					sys.stdout.write(sharp)
		print
	print