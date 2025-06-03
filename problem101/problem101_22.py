a=[input() for i in range(2)]
a1=[int(i) for i in a[0].split()]
a2=int(a[1])

count=0

while a1[1]<=a1[0]:
	a1[1]=a1[1]*2
	count+=1

while a1[2]<=a1[1]:
	a1[2]=a1[2]*2
	count+=1

if count<=a2:
	print("Yes")
else:
	print("No")
