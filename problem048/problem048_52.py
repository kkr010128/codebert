n= int(input())
l= list(map(int,input().split()))
s= 0
for i in range(n):
	if(l[i]<l[0]):
		l[0],l[i]= l[i],l[0]
for j in range(n):
	if(l[n-1]<l[j]):
		l[n-1],l[j]= l[j],l[n-1]
for k in range(n):
	s+= l[k]
print(l[0],l[n-1],s)