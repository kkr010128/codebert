n = input()
for i in range(n):
	a, b, c = map(int, raw_input().strip().split(' '))
	if a*a+b*b == c*c or a*a+c*c == b*b or c*c+b*b == a*a:
		print "YES"
	else:
		print "NO"