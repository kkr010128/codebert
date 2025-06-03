a = 1
b = 1
op = ''
i = 0
while op!='?':
	a,op,b = [i for i in input().split()]
	a = int(a)
	b = int(b)
	if op!='?':
		if op=='+':
			print(a+b)
		elif op=='-':
			print(a-b)
		elif op=='*':
			print(a*b)
		elif op=='/':
			print(a//b)