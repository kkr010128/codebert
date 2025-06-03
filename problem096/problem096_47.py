n,d = map(int,input().split())
count = 0
for i in range(n):
	x,y = map(float,input().split())
	if(d*d >= x*x + y*y):
		count+=1
print(count)