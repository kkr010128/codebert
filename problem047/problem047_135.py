while True:
	s = raw_input().split()
	if '?' == s[1]:
		break
	if '+' == s[1]:
		print int(s[0])+int(s[2])
	if '-' == s[1]:
		print int(s[0])-int(s[2])
	if '*' == s[1]:
		print int(s[0])*int(s[2])
	if '/' == s[1]:
		print int(s[0])/int(s[2])