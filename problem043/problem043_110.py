a = []
while True:
	b = list(map(int,input().split()))
	if b[0] == 0 and b[1]==0:
		break
	b.sort()
	a.append(b)

for i in a:
	print(i[0],i[1])