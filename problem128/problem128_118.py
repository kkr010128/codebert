def run():
	X, N = [int(v) for v in input().rstrip().split()]
	p = []
	if N > 0:
		p = [int(v) for v in input().rstrip().split()]

	i = -1
	try:
		i = p.index(X)
	except ValueError:
		pass

	if i == -1:
		# not contained	
		return X

	d1 = {}
	for k in range(0, 102):
		d1[k] = k

	for v in p:
		del d1[v]

	l2 = sorted(list(d1.keys()))

	l2.append(X)
	l2.sort()
	i = l2.index(X)

	r = 0
	if i == 0:
		r = l2[1]
	elif (i + 1) == len(l2):
		r = l2[-2]
	else:
		v1 = l2[i + 1] - X
		v2 = X - l2[i - 1]
		if v1 < v2 :
			r = l2[i + 1]
		elif v1 > v2 :
			r = l2[i - 1]
		else:
			# v1 == v2
			r = l2[i - 1]


	return r

r = run()
print(r)

