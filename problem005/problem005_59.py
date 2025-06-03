#! /usr/bin/env python3

import sys

get = sys.stdin.read().split('\n')

for g in get:
	nums = list(map(int, g.split()))
	output = ''
	if (nums != []):
		# print(nums)
		[a, b] = nums
		while ((a != 0) and (b != 0)):
			larger = max([a, b])
			smaller = min([a, b])
			a = larger - smaller 
			b = smaller
		output += str(max([a, b])) + ' ' + str((nums[0]*nums[1])//max([a,b]))
		print(output)