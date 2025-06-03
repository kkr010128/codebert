while True :
	char_line = raw_input().split()
	a = int(char_line[0])
	b = int(char_line[2])
	if char_line[1] == '?':
		break
	elif char_line[1] =='+':
		print(a+b)
	elif char_line[1]=='-':
		print(a-b)
	elif char_line[1]=='*':
		print(a*b)
	else:
		print(a/b)