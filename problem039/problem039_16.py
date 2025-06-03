l = input().split()

l = list(map(int, l))

a,b,c = l[0],l[1],l[2]

if a<b<c:
	print("Yes")
else:
	print("No")
