l=[int(input()) for i in range(3)]

x=l[0]
y=l[1]
z=l[2]
if x<y:
	print(-(-z//y))
else:
	print(-(-z//x))