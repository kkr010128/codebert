x=[]
y=[]
n=list(map(int,input().split()))

for i in range(n[0]):
	x.append(list(map(int,input().split())))
for i in range(n[1]):
	y.append(list(map(int,input().split())))
	
for i in range(n[0]):
	a=[]
	for j in range(n[2]):
		b=0
		for k in range(n[1]):
			f=x[i][k]*y[k][j]
			b+=f
		a.append(b)
	print(' '.join(list(map(str,a))))
	
			
			
			
		
			
