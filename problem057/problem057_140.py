A=[]
while True:
	#midterm exam score(50) : m
	#final  exam score(50)  : f
	#retest score(100)      : r
	m,f,r = [int(i) for i in input().split()]
	if m == f == r == -1:
		break
	elif m==-1 or f==-1:
		A.append('F')	
	elif m+f >= 80:
		A.append('A')
	elif 65<=m+f<80:
		A.append('B')
	elif (50<=m+f<65) or ((30<=m+f<50) and (50<=r)):
		A.append('C')
	elif (30<=m+f<50):
		A.append('D')
	else:
		A.append('F')

for i in range(len(A)):
	print(A[i])