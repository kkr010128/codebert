import math

while True:
	n = int(raw_input())
	if n==0:
	    break
	nums = [int(x) for x in raw_input().split(" ")]
	average = sum(nums) / float(n)

	a2 = sum([math.pow(x-average, 2.0) for x in nums]) / n
	print math.sqrt(a2)