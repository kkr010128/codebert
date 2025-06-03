#python2.7
N,M = raw_input().split()
time=0
flag=1
A=[]
for i in range(int(N)):
	A.append(raw_input().split())

while len(A)!=0:
	if(int(A[0][1])>int(M)):
		A[0][1]=str(int(A[0][1])-int(M))
		A.append(A[0])
		del A[0]
		time+=int(M)
	else:
		time+=int(A[0][1])
		print A[0][0]+" "+str(time)
		del A[0]