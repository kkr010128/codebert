from math import ceil
n=int(input())
s=100000
for i in range(n):
	s +=(s*0.05)
	s=int(int(ceil(s/1000)*1000))
print(s)