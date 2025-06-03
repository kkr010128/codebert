n, k = [int(i) for i in input().split()]
h = sorted([int(i) for i in input().split()])
if k > len(h):
	print(0)
elif k == 0:
	print(sum(h))
else:
	print(sum(h[0:-k]))