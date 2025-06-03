data = []
while 1:
	H, W = map(int, raw_input().split())
	if H == 0 and W == 0:
		break
	data.append([H, W])

for h, w in data:
	for i in xrange(h):
		print '#' * w
	print