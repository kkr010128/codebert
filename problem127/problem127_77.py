X, Y = [int(v) for v in input().rstrip().split()]

r = 'No'
if Y % 2 == 0:
	for n in range(X + 1):
		cn = n
		tn = X - cn
		if cn * 2 + tn * 4 == Y:
			r = 'Yes'
			break

print(r)
