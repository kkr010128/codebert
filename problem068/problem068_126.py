x = input()
for i in range(int(input())):
	o = input().split()
	a,b = map(int,o[1:3])
	b+=1
	t = o[0][2]
	if t == 'i':
		print(x[a:b])
	elif t =='p':
		x = x[:a] + o[3] + x[b:]
	else:
		x = x[:a] + x[a:b][::-1] + x[b:]
