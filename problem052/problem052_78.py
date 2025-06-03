# -*- coding: utf-8 -*-

def call(n):
	print '',
	for i in xrange(1, n+1):
		if check(i):
			print(i),
	print

def check(i):
	if i % 3 == 0:
		return True
	elif i % 10 == 3:
		return True
	elif i / 10 > 0:
		x = i
		x /= 10
		while (x > 0):
			if x % 10 == 3:
				return True
			else:
				x /= 10
	return False


n = int(raw_input())
call(n)