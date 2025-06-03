# -*- coding: utf-8 -*-

S = [0] * 13
H = [0] * 13
C = [0] * 13
D = [0] * 13

n = int(raw_input())

for i in xrange(n):
	symbol, num = map(str, raw_input().split())
	if symbol == 'S':
		S[int(num)-1] = 1
	elif symbol == 'H':
		H[int(num)-1] = 1
	elif symbol == 'C':
		C[int(num)-1] = 1
	else:
		D[int(num)-1] = 1

cards = [S, H, C, D]
marks = ['S', 'H', 'C', 'D']

for card, mark in zip(cards, marks):
	for index, num in enumerate(card):
		if num < 1:
			print mark, index+1