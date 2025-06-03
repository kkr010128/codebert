while 1:
	l=map(str,raw_input().split())
	answer = 0 
	if  l[1] == '+':
		answer = int (l[0]) + int (l[2])
	if  l[1] == '-':
		answer = int (l[0]) - int (l[2])
	if  l[1] == '*':
		answer = int (l[0]) * int (l[2])
	if  l[1] == '/':
		answer = int (l[0]) / int (l[2])
	if  l[1] == '?':
		break;
	print answer