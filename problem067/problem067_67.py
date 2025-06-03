point_a,point_b = 0,0
for i in range(int(input())):
	k =[]
	a,b = input().split()
	k = [[i,j] for i,j in zip(a,b) if i != j]
	if k == []:
		if len(a) < len(b):
			point_b+=3
		elif len(a) > len(b):
			point_a += 3
		else:
			point_a+=1
			point_b+=1
	elif ord(k[0][0]) < ord(k[0][1]):
		point_b += 3
	else :
		point_a += 3
print(point_a,point_b)