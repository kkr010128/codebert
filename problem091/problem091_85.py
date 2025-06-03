def check(a,b,c):
	if a==b or a==c or b==c:
		return False
	if a+b>c and b+c>a and c+a>b:
		
		return True
	return False

n=int(input())
c=list(map(int,input().split()))
count=0
for i in range(len(c)-2):
	for j in range(i+1,len(c)-1):
		for k in range(j+1,len(c)):
			if check(c[i],c[j],c[k]):
				count+=1
print(count)

				


			
