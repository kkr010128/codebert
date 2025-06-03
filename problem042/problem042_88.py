x = []
while True:
	if 0 in x:
		break
	x.append(int(input()))
x.pop()
for i, v in enumerate(x):
	print(('Case %d: %d') % (i+1, v))