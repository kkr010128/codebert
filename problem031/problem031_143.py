import math
def standard_deviation() :
	while True :
		n = input()
		if n==0 :
			break
		s_d = [0]*n
		average = 0
		standard = 0
		s_d= map(float,raw_input().split())
		for i in range(n):
			average += s_d[i]
		average /= float(n)
		for i in range(n):
			standard += pow(s_d[i]-average,2) / float(n)
		print(math.sqrt(standard))
standard_deviation()