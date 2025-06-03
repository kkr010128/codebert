n=int(raw_input())
left=0
right=0
for i in range(n):
	x,y=raw_input().strip().split()
	
	
	if x==y:
		left+=1
		right+=1
	elif x<y:
		right+=3
	elif x>y:
		left+=3
print left,right