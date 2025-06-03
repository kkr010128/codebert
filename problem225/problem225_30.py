h, a = list(map(int, input().split()))

b = h/a

if int(b) == b:
	print(int(b))
else:
	print(int(b)+1)