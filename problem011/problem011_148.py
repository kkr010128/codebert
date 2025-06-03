
if __name__ == '__main__':
	s = input().split()
	if s[0] < s[1]:
		tmp = s[0]
		s[0] = s[1]
		s[1] = tmp
	while True:
		x = int(s[0]) % int(s[1])
		if x==0:
			break
		s[0] = s[1]
		s[1] = x

	print (s[1])


