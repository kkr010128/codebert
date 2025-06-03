while True:
	a,op,b=input().split(" ")
	a,b=[int(i) for i in (a,b)]
	if op=="?":
		break
	print(a+b if op=="+" else a-b if op=="-" else a*b if op=="*" else int(a/b) if op=="/" else "")