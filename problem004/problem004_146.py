#! /usr/bin/env python3

noOfInputs = int(input())
for i in range(noOfInputs):
	numsInStr = input().split()
	nums = []
	for n in numsInStr:
		nums.append(int(n))

	largest = max(nums)	
	nums.remove(max(nums))
	#print(nums)

	if (largest**2 == sum([i**2 for i in nums])):
		print('YES')
	else:
		print('NO')