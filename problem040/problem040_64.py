n = map(int,raw_input().split())
for i in range(0,3):
	for k in range(i,3):
		if n[i]>n[k]:
			temp = n[i]
			n[i] = n[k]
			n[k]= temp
for j in range(0,3):
	print str(n[j]),