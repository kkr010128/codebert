s = raw_input()
n1,  n2 = s.split()
n1 = int(n1)
n2 = int(n2)
flag = True
if n1 < 0 or n1 > 9:
	flag = False
if n2 < 0 or n2 > 9:
	flag = False
if flag:
	print n1 * n2
else:
	print -1