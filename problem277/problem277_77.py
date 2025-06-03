H, W, K = map(int, input().split())
S = [''] * H
for i in range(H):
	S[i] = input()
A = [[0] * W] * H
bg = 1
inflg = 0
outcnt = 1
for i in range(H):
	if '#' not in S[i]:
		if inflg == 0:
			outcnt += 1
		else:
			A[i] = A[i-1]
			print(" ".join(str(k) for k in A[i]))
	else:
		inflg += 1
		for j in range(S[i].find('#')):
			A[i][j] = bg
		for j in range(S[i].find('#'),W):
			if S[i][j] == '#':
				A[i][j] = bg
				bg += 1
			else:
				A[i][j] = A[i][j-1]
		if inflg == 1:
			for s in range(outcnt):
				print(" ".join(str(k) for k in A[i]))
		else:
			print(" ".join(str(k) for k in A[i]))
