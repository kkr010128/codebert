N = list(map(int, input().split(' ')))

W = N[0]
H = N[1]
x = N[2]
y = N[3]
r = N[4]

if r <= x < W and (x + r) <= W and r <= y < W and (y + r) <= H:
	print('Yes')
else:
	print('No')