N = int(input())

r = N
while  r >= 1000:
	r = r-1000

if r == 0:
	print(0)
else:
	print(1000-r)
