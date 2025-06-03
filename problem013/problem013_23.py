n = input()
minSeq = input()
maxv = -float("inf")
while True:
	try:
		R = input()
		if R - minSeq > maxv:
			maxv = R - minSeq
		if R < minSeq:
			minSeq = R
	except EOFError:
		break
print(maxv)