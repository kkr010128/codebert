n = int(input())
a = [int(i) for i in input().split()]
s = 0
for i in a:
	s ^= i
for i in a:
	print(s^i,end = ' ')