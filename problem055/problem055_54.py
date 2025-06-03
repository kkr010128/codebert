# -*- coding: utf-8 -*-

class residence(object):
	def __init__(self):
		one = [0] * 10
		two = [0] * 10
		three = [0] * 10
		self.all = [one, two, three]

residences = [ ]

for i in xrange(4):
	residences.append(residence())

n = int(raw_input())

for i in xrange(n):
	b, f, r, v = map(int, raw_input().split())
	residences[b-1].all[f-1][r-1] += v

for i, residence in enumerate(residences):
	for floor in residence.all:
		print '',
		for index, num in enumerate(floor):
			if index == len(floor) - 1:
				print num
			else:
				print num,
	if i != len(residences) - 1:
		print '####################'