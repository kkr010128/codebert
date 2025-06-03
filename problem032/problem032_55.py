import math
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=[1,2,3,4]
for i in a:
	num=0
	if i==1:
		for j in range(len(x)):
			num+=abs(x[j]-y[j])
		print(num)
			
	elif i==2 or i==3:
		for j in range(len(x)):
			num+=(abs(x[j]-y[j]))**i
		num=math.pow(num,1/i)
		print(num)
	
	else:
		b=[]
		for j in range(len(x)):
			b.append(abs(x[j]-y[j]))
		print(float(max(b)))
		
	
			
		
		
