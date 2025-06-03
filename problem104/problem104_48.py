l,r,d=[int(x) for x in input().split()]
x=(r-l)//d	
if l%d==0 or r%d==0:
	x+=1

print(x)   	