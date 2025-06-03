s = []
for t in input().split():
	try:
		v = int(t)
	except ValueError:
		a = s.pop()
		b = s.pop()
		if t == '+': v = b + a
		elif t == '-': v = b - a
		elif t == '*': v = b * a
	s.append(v)
print(s.pop())
