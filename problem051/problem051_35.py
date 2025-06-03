line = '#.'*150
while True:
	H, W = map(int, raw_input().split())
	if H == W == 0: break
	for i in range(H):
		print line[i%2:i%2+W]
	print ''