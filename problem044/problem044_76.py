[a,b,c]=raw_input().split()
x=int(a)
y=int(b)
z=int(c)
ans=[]
for n in range(x,y+1):
	if z%n==0:
		ans.append(n)
print len(ans)