import math
n = input()
a = 100000
for val in range(1,n+1):
	a *= 1.05
	A = math.ceil(a/1000) * 1000
	a = A 
print int(a)