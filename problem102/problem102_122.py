a=[input() for i in range(2)]
a1=[int(i) for i in a[0].split()]
a2=[int(i) for i in a[1].split()]
k=a1[1]
for i in range(a1[0]-a1[1]):
	if a2[i]<a2[i+k]:
		print("Yes")
	else:
		print("No")