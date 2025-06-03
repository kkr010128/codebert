import math
while True:
	n = input()
	if n == 0:
		break
	s = map(int, raw_input().split())
	sumS = 0.0
	sum = 0.0
	for i in s:
		sumS += i**2
		sum += i
	v = sumS / n - (sum / n)**2
	print math.sqrt(v)