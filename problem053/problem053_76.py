# -*- coding: utf-8 -*-

n = int(raw_input())

num = map(int, raw_input().split())

for e in num[::-1]:
	if e == num[0]:
		print e
		break
	print e,