while True:
	s = input()
	if s == "-":
		break
	m = int(input())
	for n in range(m):
		h = int(input())
		t = s[0:h]
		u = s[h:]
		s = u + t
	print(s)