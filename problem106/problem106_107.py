n=int(input())
vec=[0 for _ in range(10050)]
for x in range(1,105):
	for y in range (1,105):
		for z in range (1 , 105):
			sum= x*x + y*y + z*z + x*y +y*z + z*x
			if sum<10050:
				vec[sum]+=1
				
for i in range(1,n+1):
	print(vec[i])