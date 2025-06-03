while 1:
	S = raw_input()
	if (S == '-'):
		break

	N = input()


	for i in range(N):
		h = input()
		S = S[h : len(S)] +  S[0 : h]

	print S
